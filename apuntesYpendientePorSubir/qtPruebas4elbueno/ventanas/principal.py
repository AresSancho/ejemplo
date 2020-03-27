# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'principal.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 140, 161, 71))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menucamisetas = QtWidgets.QMenu(self.menubar)
        self.menucamisetas.setObjectName("menucamisetas")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionregistro = QtWidgets.QAction(MainWindow)
        self.actionregistro.setObjectName("actionregistro")
        self.actionlistado = QtWidgets.QAction(MainWindow)
        self.actionlistado.setObjectName("actionlistado")
        self.menucamisetas.addAction(self.actionregistro)
        self.menucamisetas.addAction(self.actionlistado)
        self.menubar.addAction(self.menucamisetas.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "APP GESTION"))
        self.label.setText(_translate("MainWindow", "bienvenido"))
        self.menucamisetas.setTitle(_translate("MainWindow", "camisetas"))
        self.actionregistro.setText(_translate("MainWindow", "registro"))
        self.actionlistado.setText(_translate("MainWindow", "listado"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
