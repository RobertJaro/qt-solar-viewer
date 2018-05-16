# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(864, 610)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        MainWindow.setDockOptions(
            QtWidgets.QMainWindow.AllowNestedDocks | QtWidgets.QMainWindow.AllowTabbedDocks | QtWidgets.QMainWindow.AnimatedDocks | QtWidgets.QMainWindow.GroupedDragging)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 864, 26))
        self.menubar.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.menuFile.setTitle("File")
        self.menuFile.setObjectName("menuFile")
        self.openMap = QtWidgets.QMenu(self.menuFile)
        self.openMap.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.openMap.setTitle("Open SunPy Map")
        self.openMap.setObjectName("openMap")
        self.open2D = QtWidgets.QMenu(self.menuFile)
        self.open2D.setTitle("Open 2D FITS")
        self.open2D.setObjectName("open2D")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuOpen_SunPy_Composite_Map = QtWidgets.QMenu(self.menuFile)
        self.menuOpen_SunPy_Composite_Map.setObjectName("menuOpen_SunPy_Composite_Map")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setTitle("Edit")
        self.menuEdit.setObjectName("menuEdit")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setTitle("Help")
        self.menuHelp.setObjectName("menuHelp")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        self.menuToolbar = QtWidgets.QMenu(self.menuView)
        self.menuToolbar.setObjectName("menuToolbar")
        MainWindow.setMenuBar(self.menubar)
        self.status_bar = QtWidgets.QStatusBar(MainWindow)
        self.status_bar.setObjectName("status_bar")
        MainWindow.setStatusBar(self.status_bar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setCheckable(False)
        self.actionOpen.setText("Open")
        self.actionOpen.setIconText("Open")
        self.actionOpen.setToolTip("Open")
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setText("Save")
        self.actionSave.setIconText("Save")
        self.actionSave.setToolTip("Save")
        self.actionSave.setObjectName("actionSave")
        self.openSeries = QtWidgets.QAction(MainWindow)
        self.openSeries.setObjectName("openSeries")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionDownload_Data = QtWidgets.QAction(MainWindow)
        self.actionDownload_Data.setObjectName("actionDownload_Data")
        self.actionChange_DB = QtWidgets.QAction(MainWindow)
        self.actionChange_DB.setObjectName("actionChange_DB")
        self.actionHEK = QtWidgets.QAction(MainWindow)
        self.actionHEK.setObjectName("actionHEK")
        self.openMapMPL = QtWidgets.QAction(MainWindow)
        self.openMapMPL.setText("MPL")
        self.openMapMPL.setObjectName("openMapMPL")
        self.openMapGinga = QtWidgets.QAction(MainWindow)
        self.openMapGinga.setText("Ginga")
        self.openMapGinga.setObjectName("openMapGinga")
        self.open2DMPL = QtWidgets.QAction(MainWindow)
        self.open2DMPL.setText("MPL")
        self.open2DMPL.setObjectName("open2DMPL")
        self.open2DGinga = QtWidgets.QAction(MainWindow)
        self.open2DGinga.setText("Ginga")
        self.open2DGinga.setObjectName("open2DGinga")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionContrast = QtWidgets.QAction(MainWindow)
        self.actionContrast.setCheckable(True)
        self.actionContrast.setObjectName("actionContrast")
        self.actionFITS = QtWidgets.QAction(MainWindow)
        self.actionFITS.setObjectName("actionFITS")
        self.actionImage = QtWidgets.QAction(MainWindow)
        self.actionImage.setObjectName("actionImage")
        self.actionOpen_SV_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_SV_Project.setObjectName("actionOpen_SV_Project")
        self.default_toolbar = QtWidgets.QAction(MainWindow)
        self.default_toolbar.setCheckable(True)
        self.default_toolbar.setObjectName("default_toolbar")
        self.actionFrom_File = QtWidgets.QAction(MainWindow)
        self.actionFrom_File.setObjectName("actionFrom_File")
        self.actionFrom_Active = QtWidgets.QAction(MainWindow)
        self.actionFrom_Active.setObjectName("actionFrom_Active")
        self.openMap.addAction(self.openMapMPL)
        self.openMap.addAction(self.openMapGinga)
        self.open2D.addAction(self.open2DMPL)
        self.open2D.addAction(self.open2DGinga)
        self.menuExport.addAction(self.actionFITS)
        self.menuExport.addAction(self.actionImage)
        self.menuOpen_SunPy_Composite_Map.addAction(self.actionFrom_File)
        self.menuOpen_SunPy_Composite_Map.addAction(self.actionFrom_Active)
        self.menuFile.addAction(self.actionOpen_SV_Project)
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.openMap.menuAction())
        self.menuFile.addAction(self.menuOpen_SunPy_Composite_Map.menuAction())
        self.menuFile.addAction(self.openSeries)
        self.menuFile.addAction(self.open2D.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDownload_Data)
        self.menuFile.addAction(self.actionHEK)
        self.menuFile.addAction(self.actionChange_DB)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuTools.addAction(self.actionContrast)
        self.menuToolbar.addAction(self.default_toolbar)
        self.menuView.addAction(self.menuToolbar.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Solar Viewer"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuOpen_SunPy_Composite_Map.setTitle(_translate("MainWindow", "Open SunPy Composite Map"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.menuToolbar.setTitle(_translate("MainWindow", "Toolbar"))
        self.openSeries.setText(_translate("MainWindow", "Open SunPy Timeseries"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As.."))
        self.actionDownload_Data.setText(_translate("MainWindow", "Download Data"))
        self.actionChange_DB.setText(_translate("MainWindow", "Change DB Settings"))
        self.actionHEK.setText(_translate("MainWindow", "HEK"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionContrast.setText(_translate("MainWindow", "Contrast"))
        self.actionFITS.setText(_translate("MainWindow", "FITS"))
        self.actionImage.setText(_translate("MainWindow", "Image"))
        self.actionOpen_SV_Project.setText(_translate("MainWindow", "Open SV Project"))
        self.default_toolbar.setText(_translate("MainWindow", "Default"))
        self.actionFrom_File.setText(_translate("MainWindow", "From File"))
        self.actionFrom_Active.setText(_translate("MainWindow", "From Active"))
