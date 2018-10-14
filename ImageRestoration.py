# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ImageRestoration.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(765, 590)
        Dialog.setMaximumSize(QtCore.QSize(765, 590))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 430, 99, 29))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 480, 201, 29))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 550, 99, 29))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 520, 201, 29))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(330, 480, 201, 29))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 520, 201, 29))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.pushButton_7 = QtGui.QPushButton(Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(540, 480, 201, 29))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(130, 10, 121, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(520, 10, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton_8 = QtGui.QPushButton(Dialog)
        self.pushButton_8.setGeometry(QtCore.QRect(10, 470, 101, 31))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(Dialog)
        self.pushButton_9.setGeometry(QtCore.QRect(540, 520, 99, 29))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.pushButton_10 = QtGui.QPushButton(Dialog)
        self.pushButton_10.setGeometry(QtCore.QRect(650, 520, 99, 29))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.pushButton_12 = QtGui.QPushButton(Dialog)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 510, 99, 29))
        self.pushButton_12.setObjectName(_fromUtf8("pushButton_12"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 40, 331, 301))
        self.label_3.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(400, 40, 331, 301))
        self.label_4.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(590, 370, 81, 21))
        self.label_5.setStyleSheet(_fromUtf8(""))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(590, 400, 81, 21))
        self.label_6.setStyleSheet(_fromUtf8(""))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(500, 370, 67, 17))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(500, 400, 67, 17))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(590, 420, 81, 21))
        self.label_9.setStyleSheet(_fromUtf8(""))
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(500, 420, 67, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(500, 450, 67, 17))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(590, 450, 81, 21))
        self.label_12.setStyleSheet(_fromUtf8(""))
        self.label_12.setText(_fromUtf8(""))
        self.label_12.setObjectName(_fromUtf8("label_12"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "EE610 Assignment - 2", None))
        self.pushButton.setText(_translate("Dialog", " Load Image", None))
        self.pushButton_2.setText(_translate("Dialog", "Blur", None))
        self.pushButton_3.setText(_translate("Dialog", "Save Image", None))
        self.pushButton_4.setText(_translate("Dialog", "Full Inverse", None))
        self.pushButton_5.setText(_translate("Dialog", "Truncated Inverse", None))
        self.pushButton_6.setText(_translate("Dialog", "Wiener", None))
        self.pushButton_7.setText(_translate("Dialog", "Constrained LS", None))
        self.label.setText(_translate("Dialog", "   Original Image", None))
        self.label_2.setText(_translate("Dialog", "Restored Image", None))
        self.pushButton_8.setText(_translate("Dialog", "Load Kernel", None))
        self.pushButton_9.setText(_translate("Dialog", "Undo", None))
        self.pushButton_10.setText(_translate("Dialog", "Undo All", None))
        self.pushButton_12.setText(_translate("Dialog", "View Kernel", None))
        self.label_7.setText(_translate("Dialog", "PSNR", None))
        self.label_8.setText(_translate("Dialog", "SSIM", None))
        self.label_10.setText(_translate("Dialog", "PSNR1", None))
        self.label_11.setText(_translate("Dialog", "SSIM1", None))

# Class defining all GUI elements for Gamma input window
class InputDialogGuiClass(QtGui.QDialog):

    # define class variable to store  integer value of gamma entered by user
    gamma = 1.0

    def __init__(self, parent):
        super(InputDialogGuiClass, self).__init__(parent)
        self.setupUi(self)

        # link functions with OK and Cancel button clicks
        self.cancelButton.clicked.connect(lambda: self.close_window())
        self.okButton.clicked.connect(lambda: self.accept_value())

    def setupUi(self, InputDialogGuiClass):
        InputDialogGuiClass.setObjectName(_fromUtf8("InputDialogGuiClass"))
        InputDialogGuiClass.setWindowModality(QtCore.Qt.WindowModal)
        InputDialogGuiClass.setFixedWidth(360)
        InputDialogGuiClass.setFixedHeight(140)
        self.verticalLayout = QtGui.QVBoxLayout(InputDialogGuiClass)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(InputDialogGuiClass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.gammaInput = QtGui.QLineEdit(InputDialogGuiClass)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gammaInput.sizePolicy().hasHeightForWidth())
        self.gammaInput.setSizePolicy(sizePolicy)
        self.gammaInput.setObjectName(_fromUtf8("lineEdit"))
        self.gammaInput.setText('1.00')
        self.gammaInput.setValidator(QtGui.QDoubleValidator(0, 1000.0, 10, self.gammaInput))
        self.horizontalLayout_2.addWidget(self.gammaInput)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(InputDialogGuiClass)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.cancelButton = QtGui.QPushButton(InputDialogGuiClass)
        self.cancelButton.setObjectName(_fromUtf8("cancelButton"))
        self.horizontalLayout_3.addWidget(self.cancelButton)
        self.okButton = QtGui.QPushButton(InputDialogGuiClass)
        self.okButton.setObjectName(_fromUtf8("okButton"))
        self.horizontalLayout_3.addWidget(self.okButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(InputDialogGuiClass)
        QtCore.QMetaObject.connectSlotsByName(InputDialogGuiClass)

    # close window on Close or Cancel button click
    def close_window(self):
        self.close()

    # update class variable when OK button clicked and close the window
    def accept_value(self):
        if self.gammaInput.text() and float(self.gammaInput.text()) <= 1000.0:
            self.gamma = float(self.gammaInput.text())
            self.close()
            return True
        else:
            self.close() #self.label_2.setStyleSheet("color: rgb(255, 0, 0);")


    def retranslateUi(self, InputDialogGuiClass):
        InputDialogGuiClass.setWindowTitle(_translate("InputDialogGuiClass",
                                                      "Input Window", None))
        self.label.setText(_translate("InputDialogGuiClass", "Input", None))
        self.label_2.setText(_translate("InputDialog",
                                        "NB: Enter value > 0 ", None))
        self.cancelButton.setText(_translate("InputDialog", "Cancel", None))
        self.okButton.setText(_translate("InputDialog", "OK", None))


