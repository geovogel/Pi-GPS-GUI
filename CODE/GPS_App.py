#!/usr/bin/env python3

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtWidgets import QTableWidget, QStatusBar, QTableWidgetItem, QMessageBox
from PyQt5 import Qwt
from ui_GPS_App import Ui_MainWindow
import googlemaps
import gpsd_PRN
import pyqtgraph as pg
import math
import numpy as np

import os
import time
import RPi.GPIO as GPIO

# ======= QT SETUP ================================================================================

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()   # Set up the user interface from Designer.
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        app.setStyle('cleanlooks')       # setup stylesheet

# ======= INITIALIZATION ==========================================================================

        global Cm
        Cm = 3.28084                      # Conversion factor meters to ft
        d = chr(176)                      # Symbol for degrees
        urlBase = "https://maps.googleapis.com/maps/api/staticmap?"
        APIkey = "AIzaSyAgfvdjj6C_IpfMh2tJNfKE3mYNreMp-1g"
        gmaps = googlemaps.Client(key=APIkey)
        gpsd_PRN.connect()
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN)

# ======= LOCAL WIDGET MODIFICATIONS ==============================================================

        # QT Widget name assignments
        global AltBox, spdMeter, compass, spdLCD, compLCD, climbThermo, gpsTable, statBar
        AltBox =      self.ui.AltBox
        spdMeter =    self.ui.SpeedDial
        compass =     self.ui.Compass
        spdLCD =      self.ui.SpeedLCD
        compLCD =     self.ui.CompassLCD
        climbThermo = self.ui.VertSpdThermo
        gpsTable =    self.ui.tableWidget
        statBar =     self.ui.statusBar
        # Speedometer setup
        palette2 = QPalette()
        palette2.setColor(QPalette.Base, Qt.black)
        palette2.setColor(QPalette.WindowText, QColor(Qt.darkBlue))
        palette2.setColor(QPalette.Text, Qt.yellow)
        palette2.setColor(QPalette.Dark, Qt.darkGray)       # Bezel ring color 1
        palette2.setColor(QPalette.Light, Qt.lightGray)     # Bezel Ring Color 2
        spdMeter.setPalette(palette2)
        needle = Qwt.QwtDialSimpleNeedle(Qwt.QwtDialSimpleNeedle.Arrow, True, Qt.red, QtGui.QColor(Qt.gray))
        spdMeter.setNeedle(needle)
        # Compass setup
        palette0 = QPalette()
        palette0.setColor(QPalette.Base, Qt.darkBlue)
        palette0.setColor(QPalette.WindowText, QColor(Qt.darkBlue))
        palette0.setColor(QPalette.Text, Qt.yellow)
        palette0.setColor(QPalette.Dark, Qt.darkGray)       # Bezel ring color 1
        palette0.setColor(QPalette.Light, Qt.lightGray)     # Bezel Ring Color 2
        compass.setPalette(palette0)
        # Tick marks for each degree
        CompSclDrw = Qwt.QwtCompassScaleDraw()
        CompSclDrw.enableComponent(Qwt.QwtAbstractScaleDraw.Ticks, True)
        CompSclDrw.enableComponent(Qwt.QwtAbstractScaleDraw.Labels, True)
        CompSclDrw.enableComponent(Qwt.QwtAbstractScaleDraw.Backbone, False)
        CompSclDrw.setTickLength(Qwt.QwtScaleDiv.MinorTick, 0)
        CompSclDrw.setTickLength(Qwt.QwtScaleDiv.MediumTick, 0)
        CompSclDrw.setTickLength(Qwt.QwtScaleDiv.MajorTick, 5)
        compass.setScaleDraw(CompSclDrw)
        compass.setNeedle(Qwt.QwtCompassMagnetNeedle(Qwt.QwtCompassMagnetNeedle.ThinStyle, Qt.darkBlue, Qt.red))
        # Thermo setup for vertical speed
        climbThermo.setFillBrush(Qt.red)
        climbThermo.setAlarmBrush(Qt.blue)
        climbThermo.setAlarmLevel(0.0)

# ======= PYQTGRAPH POLAR PLOT SETUP ==============================================================

        satMapPlt = self.ui.polarplot
        satMapPlt.showGrid(False, False, 0.8)
        satMapPlt.showAxis("left", False)
        satMapPlt.showAxis("bottom", False)
        satMapPlt.setAspectLocked()
        # Polar Plot colors
        br_1 = pg.mkBrush('g')
        pen_r = pg.mkPen(width=0, color=(255, 0, 0), style=QtCore.Qt.SolidLine)

# ======= PYQTGRAPH BAR PLOT SETUP ================================================================

        satBg = self.ui.barplot
        satBg.showGrid(True, False, 0.8)
        satBg.showAxis("left", False)
        satBg.showAxis("bottom", True)
        #satBg.setAspectLocked()
        #Change the colors of the LED's'
        palette1 = QPalette()
        palette1.setColor(QPalette.Dark, Qt.darkYellow)       # Digit color 1
        palette1.setColor(QPalette.Light, Qt.yellow)          # Digit Color 2
        spdLCD.setPalette(palette1)
        compLCD.setPalette(palette1)
        # Set the font for the PRN identifiers
        ssFont = QtGui.QFont('Monospace', 7, 1, False)

# ======= FUNCTIONS ===============================================================================

        def getGPS():
            global mode, satData, satTot, satValid, lat, lon, alt, hdg, Hspd, Vspd, gpsTim, geoCode
            packet = gpsd_PRN.get_current()  # Get gps position
            mode = packet.mode
            satData = packet.satData
            satTot = packet.sats
            satValid = packet.sats_valid
            lat = packet.lat
            lon = packet.lon
            alt = packet.alt * Cm
            hdg = packet.track
            Hspd = (packet.hspeed * Cm) * 0.681818
            Vspd = packet.climb * Cm
            gpsTim = str(packet.get_time(local_time=True))
            geoCode = (str(lat) + ',' + str(lon))


        def drawPolarGrid():
            # Add polar grid N-S & E-W lines
            satMapPlt.addLine(x=0, pen=0.2)
            satMapPlt.addLine(y=0, pen=0.2)
            # Add the elevation rings
            for r in range(0, 105, 15):
                circle = pg.QtGui.QGraphicsEllipseItem(-r, -r, r * 2, r * 2)
                circle.setPen(pg.mkPen(0.2))
                satMapPlt.addItem(circle)


        def polarPlot():
            satMapPlt.clear()
            satBg.clear()
            drawPolarGrid()
            # Calculate and plot satellite locations on polar graph and signal strength on bargraph
            for i in range(0, satTot):
                PRN =  [satData[i]['PRN']][0]  # Satellite identifier
                ss =   [satData[i]['ss']][0]  # Signal strength (dB)
                az =   [satData[i]['az']][0]  # Azimuth (0-360)
                el =   [satData[i]['el']][0]  # Elevation (0-90)
                used = [satData[i]['used']][0]
                az = math.radians(90 - az)    # Convert to radians
                xCoord = el * math.cos(az)    # Transform to cartesian and plot
                yCoord = el * math.sin(az)
                # Signal strength Bargraph
                satID = pg.TextItem(text=str(PRN))                   # Bargraph text item for PRN label
                satIDFont = QtGui.QFont('Monospace', 7, 1, False)    # Bargraph text item font
                satID.setFont(satIDFont)
                x_bg = np.array([i])          # Single point array for Bargraph
                bgHt =np.array([ss])          # Set bar height tro signal strength
                yOff = .7                     # Text item y location offset to align PRN labels to bars

                if used:  # Plot satellite locations by azimuth and elevation
                    spots = [{'pos': (xCoord, yCoord), 'symbol': 'o', 'size': 6, 'brush': br_1, 'pen': None}]
                    satID.setColor('g')
                    # Plot bar in green color
                    bg = pg.BarGraphItem(x=x_bg, height=bgHt, width=0.4, brush='g', pen='g')
                    bg.rotate(-90)
                    satBg.addItem(bg)
                    # Plot PRN identifier next to bar
                    ssBgVal = pg.TextItem(text=str(PRN))
                    ssBgVal.setFont(ssFont)
                    ssBgVal.setColor('w')
                    ssBgVal.setPos(-9, -i+yOff)
                    satBg.addItem(ssBgVal)
                else:  # Plot unused satellite locations by azimuth and elevation
                    spots = [{'pos': (xCoord, yCoord), 'symbol': 'o', 'size': 6, 'brush': None, 'pen': pen_r}]
                    satID.setColor('r')
                    # Plot bar in red color
                    bg = pg.BarGraphItem(x=x_bg, height=bgHt, width=0.4, brush='r', pen='r')
                    bg.rotate(-90)
                    satBg.addItem(bg)
                    # Plot PRN identifier next to bar
                    ssBgVal = pg.TextItem(text=str(PRN))
                    ssBgVal.setFont(ssFont)
                    ssBgVal.setColor('w')
                    ssBgVal.setPos(-8, -i+yOff)
                    satBg.addItem(ssBgVal)
                # Plot the satellite PRN labels
                pt1 = pg.ScatterPlotItem(spots=spots)
                satMapPlt.addItem(pt1)
                satID.setPos(xCoord+2, yCoord+10)
                satMapPlt.addItem(satID)

        def dispURL():
            getGPS()
            if gpsTim == 'No Data':
                print("No gps devices found")
                statBar.showMessage('Last Update: ' + gpsTim)
            else:
                # Google Maps parameters
                CENTER = 'center=' + geoCode
                MARKER_1 = '&markers=color:red%7Clabel:A%7C' + geoCode
                ZOOM = '&zoom=' + zoom()
                MAPTYPE = '&maptype=' + mapStyle()
                KEY = '&key=' + APIkey
                SIZE = '&size=640 x 400'
                # MARKER_1 = '&markers=color:red%7Clabel:A%7C'
                googleMapURL = urlBase + MARKER_1 + ZOOM + SIZE + MAPTYPE + KEY
                self.ui.webView.load(QUrl(googleMapURL))
                statBar.showMessage('Last Update: ' + gpsTim)

        def mapData():
            getGPS()
            gmapData = gmaps.reverse_geocode(geoCode)
            elev = "{0:.1f}".format((gmaps.elevation((lat, lon))[0]['elevation']) * Cm) + ' ft'
            county = gmapData[0]['address_components'][4]['short_name']
            longAddr = (gmapData[0]['address_components'][0]['short_name'] + " "
                        + gmapData[0]['address_components'][1]['short_name'] + '\r\n'
                        + gmapData[0]['address_components'][3]['short_name'] + ","
                        + gmapData[0]['address_components'][5]['short_name'] + " "
                        + gmapData[0]['address_components'][7]['short_name'])

            addLin_1 = (gmapData[0]['address_components'][0]['short_name'] + " "
                        + gmapData[0]['address_components'][1]['short_name'])

            addLin_2 = (gmapData[0]['address_components'][3]['short_name'] + ","
                        + gmapData[0]['address_components'][5]['short_name'] + " "
                        + gmapData[0]['address_components'][7]['short_name'])

            neighborhood = (gmapData[0]['address_components'][2]['long_name'])

            country = (gmapData[0]['address_components'][6]['long_name'])

            dtlText = ('Neighborhood: ' + neighborhood + '\r\n' + 'County: '
                        + county + '\r\n' + 'Elevation: ' + elev + '\r\n' + 'Country: ' + country)

            # Display the location data in a message box
            return longAddr, addLin_1, addLin_2, dtlText

        def dispData():
            txtData = mapData()
            msg = QMessageBox(self)
            msgFont = QtGui.QFont('PibotoLight', 10, 1, False)
            msg.setFont(msgFont)
            #msg.setIcon(QMessageBox.Information)
            msg.setText(txtData[0])
            #msg.setInformativeText(txtData[2])
            msg.setWindowTitle("Location")
            msg.setDetailedText(txtData[3])
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

        def setGPSpage():
            getGPS()  # Get gps position
            # Update the GPS Table data
            gpsTable.setItem(0, 1, QTableWidgetItem(str('{:6.0f}'.format(mode))))
            gpsTable.setItem(1, 1, QTableWidgetItem(str('{:6.0f}'.format(satTot))))
            gpsTable.setItem(2, 1, QTableWidgetItem(str('{:6.0f}'.format(satValid))))
            gpsTable.setItem(3, 1, QTableWidgetItem(str('{:6.2f}'.format(lat)) + d))
            gpsTable.setItem(4, 1, QTableWidgetItem(str('{:6.2f}'.format(lon)) + d))
            gpsTable.setItem(5, 1, QTableWidgetItem(str('{:6.1f}'.format(alt)) + ' ft'))
            gpsTable.setItem(6, 1, QTableWidgetItem(str('{:6.2f}'.format(hdg)) + d))
            gpsTable.setItem(7, 1, QTableWidgetItem(str('{:6.2f}'.format(Hspd * Cm)) + ' ft/s'))
            gpsTable.setItem(8, 1, QTableWidgetItem(str('{:6.2f}'.format(Vspd * Cm)) + ' ft/s'))
            statBar.showMessage('Last Update: ' + str(gpsTim))
            # Update the satellite position plot
            polarPlot()

        def mapStyle():
            TYPE = self.ui.MapStyle_comboBox.currentText()
            return TYPE

        def zoom():
            ZOOM = self.ui.ZoomSlider.value()
            return str(ZOOM)

        def update():
            if GPIO.input(4):          # Look for leading edge of PPS pulse
                #print(datetime.now())
                time.sleep(.950)       # Wait for GPS acquisition
                getGPS()
                AltBox.setText(str("{0:.1f}".format(alt)))
                climbThermo.setValue(Vspd)
                spdMeter.setValue(Hspd)
                spdLCD.display(Hspd)
                compass.setValue(hdg)
                compLCD.display(hdg)
                try:
                    file.write((str(gpsTim) + "," + str(lat) + "," + str(lon) + "," + str(alt) + ","
                                + str(Hspd) + "," + str(Vspd) + "," + str(hdg) + "\n"))
                    file.flush()
                except:
                    pass
            #file.close()
            QTimer.singleShot(0, update)    # Repeat

# ======= WIDGET CONNECTIONS ======================================================================

        self.ui.ShowMap_pushbtn.clicked.connect(dispURL)
        self.ui.ShowData_pushbtn.clicked.connect(dispData)
        self.ui.UpdateGPS_pushbtn.clicked.connect(setGPSpage)
        self.ui.MapStyle_comboBox.currentIndexChanged.connect(mapStyle)
        self.ui.ZoomSlider.valueChanged.connect(zoom)

        # Setup labels in GPS table
        gpsTable.setItem(0, 0, QTableWidgetItem("Mode"))
        gpsTable.setItem(1, 0, QTableWidgetItem("Satellites"))
        gpsTable.setItem(2, 0, QTableWidgetItem("Sats Valid"))
        gpsTable.setItem(3, 0, QTableWidgetItem("Latitude"))
        gpsTable.setItem(4, 0, QTableWidgetItem("Longitude"))
        gpsTable.setItem(5, 0, QTableWidgetItem("Altitude"))
        gpsTable.setItem(6, 0, QTableWidgetItem("Track"))
        gpsTable.setItem(7, 0, QTableWidgetItem("H Speed"))
        gpsTable.setItem(8, 0, QTableWidgetItem("V Speed"))

        # Setup data logging
        global file
        try:
            file = open("/media/pi/PIDISK/gps_logs/gps_data_log.csv", "a")
            if os.stat("/media/pi/PIDISK/gps_logs/gps_data_log.csv").st_size == 0:
                file.write("Time,Lat,Lon,Elev,Hspeed,VSpeed,Heading\n")
        except:
            pass
        drawPolarGrid()
        getGPS()            # Initialize the GPS data
        update()            # Start the loop function

# ======= MAIN CODE ===============================================================================

# Create the Qt application
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
