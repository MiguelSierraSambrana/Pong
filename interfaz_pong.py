# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/interfaz_pong.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_VentanaPrincipal(object):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName("VentanaPrincipal")
        VentanaPrincipal.resize(800, 600)
        VentanaPrincipal.setMinimumSize(QtCore.QSize(800, 600))
        VentanaPrincipal.setAutoFillBackground(False)
        VentanaPrincipal.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(VentanaPrincipal)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("QWidget#centralwidget{border-image: url(:/Bakground-main/images/background_main.jpg);}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titulo = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titulo.sizePolicy().hasHeightForWidth())
        self.titulo.setSizePolicy(sizePolicy)
        self.titulo.setMinimumSize(QtCore.QSize(500, 100))
        self.titulo.setMaximumSize(QtCore.QSize(500, 100))
        self.titulo.setStyleSheet("border-image: url(:/LabelPong/images/letras_titulo_pong.jpg);")
        self.titulo.setText("")
        self.titulo.setScaledContents(True)
        self.titulo.setObjectName("titulo")
        self.verticalLayout.addWidget(self.titulo, 0, QtCore.Qt.AlignHCenter)
        self.labelNombre = QtWidgets.QLabel(self.centralwidget)
        self.labelNombre.setEnabled(True)
        self.labelNombre.setMinimumSize(QtCore.QSize(170, 30))
        self.labelNombre.setMaximumSize(QtCore.QSize(170, 30))
        self.labelNombre.setStyleSheet("font: 75 12pt \"Monospace\";\n"
"color: rgb(204, 0, 0);")
        self.labelNombre.setObjectName("labelNombre")
        self.verticalLayout.addWidget(self.labelNombre, 0, QtCore.Qt.AlignHCenter)
        self.editNombre = QtWidgets.QTextEdit(self.centralwidget)
        self.editNombre.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.editNombre.sizePolicy().hasHeightForWidth())
        self.editNombre.setSizePolicy(sizePolicy)
        self.editNombre.setMinimumSize(QtCore.QSize(120, 50))
        self.editNombre.setMaximumSize(QtCore.QSize(120, 50))
        self.editNombre.setStyleSheet("QTextEdit#editNombre{\n"
"border-color: rgb(115, 210, 22);\n"
"font: 75 20pt \"Monospace\";}")
        self.editNombre.setDocumentTitle("")
        self.editNombre.setObjectName("editNombre")
        self.verticalLayout.addWidget(self.editNombre, 0, QtCore.Qt.AlignHCenter)
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setMinimumSize(QtCore.QSize(250, 60))
        self.startButton.setMaximumSize(QtCore.QSize(250, 60))
        self.startButton.setStyleSheet("QPushButton#startButton{\n"
"background-image: url(:/ButtonStart/images/start_button.jpg);\n"
";}\n"
"\n"
"\n"
"            \n"
"    \n"
"\n"
"")
        self.startButton.setText("")
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton, 0, QtCore.Qt.AlignHCenter)
        self.exitButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitButton.sizePolicy().hasHeightForWidth())
        self.exitButton.setSizePolicy(sizePolicy)
        self.exitButton.setMinimumSize(QtCore.QSize(240, 50))
        self.exitButton.setMaximumSize(QtCore.QSize(240, 50))
        self.exitButton.setStyleSheet("QPushButton#exitButton{\n"
"background-image: url(:/ButtonExit/images/exit_button.jpg);\n"
"}")
        self.exitButton.setText("")
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton, 0, QtCore.Qt.AlignHCenter)
        self.scoreButton = QtWidgets.QPushButton(self.centralwidget)
        self.scoreButton.setMinimumSize(QtCore.QSize(180, 50))
        self.scoreButton.setMaximumSize(QtCore.QSize(180, 50))
        self.scoreButton.setStyleSheet("background-image: url(:/ButtonScore/images/score_button.jpg);")
        self.scoreButton.setText("")
        self.scoreButton.setObjectName("scoreButton")
        self.verticalLayout.addWidget(self.scoreButton, 0, QtCore.Qt.AlignHCenter)
        self.infoButton = QtWidgets.QPushButton(self.centralwidget)
        self.infoButton.setMaximumSize(QtCore.QSize(50, 50))
        self.infoButton.setStyleSheet("background-image: url(:/ButtonInfo/images/info_button.jpg);")
        self.infoButton.setText("")
        self.infoButton.setObjectName("infoButton")
        self.verticalLayout.addWidget(self.infoButton)
        VentanaPrincipal.setCentralWidget(self.centralwidget)
        self.actionPuntuaciones = QtWidgets.QAction(VentanaPrincipal)
        self.actionPuntuaciones.setObjectName("actionPuntuaciones")
        self.actionAcerca_de = QtWidgets.QAction(VentanaPrincipal)
        self.actionAcerca_de.setObjectName("actionAcerca_de")
        self.actionVer_puntuaciones = QtWidgets.QAction(VentanaPrincipal)
        self.actionVer_puntuaciones.setObjectName("actionVer_puntuaciones")
        self.actionAcerca_de_2 = QtWidgets.QAction(VentanaPrincipal)
        self.actionAcerca_de_2.setObjectName("actionAcerca_de_2")
        self.action_Puntuaciones = QtWidgets.QAction(VentanaPrincipal)
        self.action_Puntuaciones.setObjectName("action_Puntuaciones")
        self.actionVer_puntuaciones_2 = QtWidgets.QAction(VentanaPrincipal)
        self.actionVer_puntuaciones_2.setObjectName("actionVer_puntuaciones_2")
        self.action_Acerca_de = QtWidgets.QAction(VentanaPrincipal)
        self.action_Acerca_de.setObjectName("action_Acerca_de")
        self.action_Acerca_de_2 = QtWidgets.QAction(VentanaPrincipal)
        self.action_Acerca_de_2.setObjectName("action_Acerca_de_2")
        self.action_Ver_puntuaciones = QtWidgets.QAction(VentanaPrincipal)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/icons/edit-paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Ver_puntuaciones.setIcon(icon)
        self.action_Ver_puntuaciones.setObjectName("action_Ver_puntuaciones")
        self.actionAcerca_de_3 = QtWidgets.QAction(VentanaPrincipal)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/icons/help-content.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAcerca_de_3.setIcon(icon1)
        self.actionAcerca_de_3.setObjectName("actionAcerca_de_3")

        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)

    def retranslateUi(self, VentanaPrincipal):
        _translate = QtCore.QCoreApplication.translate
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "MainWindow"))
        self.labelNombre.setText(_translate("VentanaPrincipal", "Escribe tu nombre"))
        self.actionPuntuaciones.setText(_translate("VentanaPrincipal", "Puntuaciones"))
        self.actionAcerca_de.setText(_translate("VentanaPrincipal", "Acerca de"))
        self.actionVer_puntuaciones.setText(_translate("VentanaPrincipal", "Ver puntuaciones"))
        self.actionAcerca_de_2.setText(_translate("VentanaPrincipal", "Acerca de"))
        self.action_Puntuaciones.setText(_translate("VentanaPrincipal", "$Puntuaciones"))
        self.actionVer_puntuaciones_2.setText(_translate("VentanaPrincipal", "Ver &puntuaciones"))
        self.action_Acerca_de.setText(_translate("VentanaPrincipal", "&Acerca de"))
        self.action_Acerca_de_2.setText(_translate("VentanaPrincipal", "&Acerca de"))
        self.action_Ver_puntuaciones.setText(_translate("VentanaPrincipal", "&Ver puntuaciones"))
        self.actionAcerca_de_3.setText(_translate("VentanaPrincipal", "Acerca de.."))
import test
