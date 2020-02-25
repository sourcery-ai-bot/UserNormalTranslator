# -*- coding: utf-8 -*-


from Qt import QtCore
from Qt import QtGui
from Qt import QtWidgets


class Ui_userNormalTranslatorWindow(QtWidgets.QMainWindow):
    def setupUi(self, userNormalTranslatorWindow):
        userNormalTranslatorWindow.setObjectName("userNormalTranslatorWindow")
        userNormalTranslatorWindow.resize(540, 550)
        userNormalTranslatorWindow.setMinimumSize(QtCore.QSize(540, 550))
        userNormalTranslatorWindow.setMaximumSize(QtCore.QSize(540, 550))
        self.centralwidget = QtWidgets.QWidget(userNormalTranslatorWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.mainLayout.setObjectName("mainLayout")
        self.grpBoxUserNormalTranslator = QtWidgets.QGroupBox(self.centralwidget)
        self.grpBoxUserNormalTranslator.setObjectName("grpBoxUserNormalTranslator")
        self.userNormalTranslatorLayout = QtWidgets.QGridLayout(self.grpBoxUserNormalTranslator)
        self.userNormalTranslatorLayout.setObjectName("userNormalTranslatorLayout")
        self.grpBoxOffset = QtWidgets.QGroupBox(self.grpBoxUserNormalTranslator)
        self.grpBoxOffset.setObjectName("grpBoxOffset")
        self.offsetLayout = QtWidgets.QGridLayout(self.grpBoxOffset)
        self.offsetLayout.setObjectName("offsetLayout")
        self.labMode = QtWidgets.QLabel(self.grpBoxOffset)
        self.labMode.setObjectName("labMode")
        self.offsetLayout.addWidget(self.labMode, 0, 0, 1, 2)
        self.rdBtnAdd = QtWidgets.QRadioButton(self.grpBoxOffset)
        self.rdBtnAdd.setChecked(True)
        self.rdBtnAdd.setObjectName("rdBtnAdd")
        self.offsetLayout.addWidget(self.rdBtnAdd, 0, 3, 1, 1)
        self.rdBtnMultiply = QtWidgets.QRadioButton(self.grpBoxOffset)
        self.rdBtnMultiply.setChecked(False)
        self.rdBtnMultiply.setObjectName("rdBtnMultiply")
        self.offsetLayout.addWidget(self.rdBtnMultiply, 0, 5, 1, 1)
        self.pBtnX = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnX.setObjectName("pBtnX")
        self.offsetLayout.addWidget(self.pBtnX, 1, 0, 1, 1)
        self.dbsBoxX = QtWidgets.QDoubleSpinBox(self.grpBoxOffset)
        self.dbsBoxX.setMinimum(-100.0)
        self.dbsBoxX.setSingleStep(0.01)
        self.dbsBoxX.setObjectName("dbsBoxX")
        self.offsetLayout.addWidget(self.dbsBoxX, 1, 1, 1, 1)
        self.pBtnXValue1 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnXValue1.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnXValue1.setObjectName("pBtnXValue1")
        self.offsetLayout.addWidget(self.pBtnXValue1, 1, 2, 1, 1)
        self.pBtnXValue2 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnXValue2.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnXValue2.setObjectName("pBtnXValue2")
        self.offsetLayout.addWidget(self.pBtnXValue2, 1, 3, 1, 1)
        self.pBtnXValue3 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnXValue3.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnXValue3.setObjectName("pBtnXValue3")
        self.offsetLayout.addWidget(self.pBtnXValue3, 1, 4, 1, 1)
        self.pBtnXValue4 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnXValue4.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnXValue4.setObjectName("pBtnXValue4")
        self.offsetLayout.addWidget(self.pBtnXValue4, 1, 5, 1, 1)
        self.pBtnY = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnY.setObjectName("pBtnY")
        self.offsetLayout.addWidget(self.pBtnY, 2, 0, 1, 1)
        self.dbsBoxY = QtWidgets.QDoubleSpinBox(self.grpBoxOffset)
        self.dbsBoxY.setMinimum(-100.0)
        self.dbsBoxY.setSingleStep(0.01)
        self.dbsBoxY.setObjectName("dbsBoxY")
        self.offsetLayout.addWidget(self.dbsBoxY, 2, 1, 1, 1)
        self.pBtnYValue1 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnYValue1.setObjectName("pBtnYValue1")
        self.offsetLayout.addWidget(self.pBtnYValue1, 2, 2, 1, 1)
        self.pBtnYValue2 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnYValue2.setObjectName("pBtnYValue2")
        self.offsetLayout.addWidget(self.pBtnYValue2, 2, 3, 1, 1)
        self.pBtnYValue3 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnYValue3.setObjectName("pBtnYValue3")
        self.offsetLayout.addWidget(self.pBtnYValue3, 2, 4, 1, 1)
        self.pBtnYValue4 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnYValue4.setObjectName("pBtnYValue4")
        self.offsetLayout.addWidget(self.pBtnYValue4, 2, 5, 1, 1)
        self.pBtnZ = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnZ.setObjectName("pBtnZ")
        self.offsetLayout.addWidget(self.pBtnZ, 3, 0, 1, 1)
        self.dbsBoxZ = QtWidgets.QDoubleSpinBox(self.grpBoxOffset)
        self.dbsBoxZ.setMinimum(-100.0)
        self.dbsBoxZ.setSingleStep(0.01)
        self.dbsBoxZ.setObjectName("dbsBoxZ")
        self.offsetLayout.addWidget(self.dbsBoxZ, 3, 1, 1, 1)
        self.pBtnZValue1 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnZValue1.setObjectName("pBtnZValue1")
        self.offsetLayout.addWidget(self.pBtnZValue1, 3, 2, 1, 1)
        self.pBtnZValue2 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnZValue2.setObjectName("pBtnZValue2")
        self.offsetLayout.addWidget(self.pBtnZValue2, 3, 3, 1, 1)
        self.pBtnZValue3 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnZValue3.setObjectName("pBtnZValue3")
        self.offsetLayout.addWidget(self.pBtnZValue3, 3, 4, 1, 1)
        self.pBtnZValue4 = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnZValue4.setObjectName("pBtnZValue4")
        self.offsetLayout.addWidget(self.pBtnZValue4, 3, 5, 1, 1)
        self.labAbsoluteValue = QtWidgets.QLabel(self.grpBoxOffset)
        self.labAbsoluteValue.setObjectName("labAbsoluteValue")
        self.offsetLayout.addWidget(self.labAbsoluteValue, 4, 2, 1, 1)
        self.cBoxAbsoluteValue = QtWidgets.QCheckBox(self.grpBoxOffset)
        self.cBoxAbsoluteValue.setText("")
        self.cBoxAbsoluteValue.setObjectName("cBoxAbsoluteValue")
        self.offsetLayout.addWidget(self.cBoxAbsoluteValue, 4, 3, 1, 1)
        self.labWorldSpace = QtWidgets.QLabel(self.grpBoxOffset)
        self.labWorldSpace.setObjectName("labWorldSpace")
        self.offsetLayout.addWidget(self.labWorldSpace, 4, 4, 1, 1)
        self.cBoxWorldSpace = QtWidgets.QCheckBox(self.grpBoxOffset)
        self.cBoxWorldSpace.setText("")
        self.cBoxWorldSpace.setObjectName("cBoxWorldSpace")
        self.offsetLayout.addWidget(self.cBoxWorldSpace, 4, 5, 1, 1)
        self.pBtnOffsetApply = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnOffsetApply.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnOffsetApply.setObjectName("pBtnOffsetApply")
        self.offsetLayout.addWidget(self.pBtnOffsetApply, 5, 4, 1, 2)
        self.pBtnResetValue = QtWidgets.QPushButton(self.grpBoxOffset)
        self.pBtnResetValue.setObjectName("pBtnResetValue")
        self.offsetLayout.addWidget(self.pBtnResetValue, 4, 0, 1, 2)
        self.userNormalTranslatorLayout.addWidget(self.grpBoxOffset, 0, 0, 1, 1)
        self.grpBoxShperize = QtWidgets.QGroupBox(self.grpBoxUserNormalTranslator)
        self.grpBoxShperize.setObjectName("grpBoxShperize")
        self.spherizeLayout = QtWidgets.QGridLayout(self.grpBoxShperize)
        self.spherizeLayout.setObjectName("spherizeLayout")
        self.labRation = QtWidgets.QLabel(self.grpBoxShperize)
        self.labRation.setObjectName("labRation")
        self.spherizeLayout.addWidget(self.labRation, 0, 0, 1, 1)
        self.dbsBoxRatio = QtWidgets.QDoubleSpinBox(self.grpBoxShperize)
        self.dbsBoxRatio.setMinimum(-100.0)
        self.dbsBoxRatio.setSingleStep(0.01)
        self.dbsBoxRatio.setObjectName("dbsBoxRatio")
        self.spherizeLayout.addWidget(self.dbsBoxRatio, 0, 1, 1, 1)
        self.pBtnRatioValue1 = QtWidgets.QPushButton(self.grpBoxShperize)
        self.pBtnRatioValue1.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnRatioValue1.setObjectName("pBtnRatioValue1")
        self.spherizeLayout.addWidget(self.pBtnRatioValue1, 0, 2, 1, 1)
        self.pBtnRatioValue3 = QtWidgets.QPushButton(self.grpBoxShperize)
        self.pBtnRatioValue3.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnRatioValue3.setObjectName("pBtnRatioValue3")
        self.spherizeLayout.addWidget(self.pBtnRatioValue3, 0, 5, 1, 1)
        self.pBtnRatioValue4 = QtWidgets.QPushButton(self.grpBoxShperize)
        self.pBtnRatioValue4.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnRatioValue4.setObjectName("pBtnRatioValue4")
        self.spherizeLayout.addWidget(self.pBtnRatioValue4, 0, 6, 1, 1)
        self.pBtnRatioValue2 = QtWidgets.QPushButton(self.grpBoxShperize)
        self.pBtnRatioValue2.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnRatioValue2.setObjectName("pBtnRatioValue2")
        self.spherizeLayout.addWidget(self.pBtnRatioValue2, 0, 3, 1, 1)
        self.pBtnCreateCenter = QtWidgets.QPushButton(self.grpBoxShperize)
        self.pBtnCreateCenter.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnCreateCenter.setObjectName("pBtnCreateCenter")
        self.spherizeLayout.addWidget(self.pBtnCreateCenter, 1, 0, 1, 2)
        self.pBtnSpherizeApply = QtWidgets.QPushButton(self.grpBoxShperize)
        self.pBtnSpherizeApply.setMinimumSize(QtCore.QSize(0, 0))
        self.pBtnSpherizeApply.setObjectName("pBtnSpherizeApply")
        self.spherizeLayout.addWidget(self.pBtnSpherizeApply, 1, 5, 1, 2)
        self.userNormalTranslatorLayout.addWidget(self.grpBoxShperize, 1, 0, 1, 1)
        self.grpNormalEditingTools = QtWidgets.QGroupBox(self.grpBoxUserNormalTranslator)
        self.grpNormalEditingTools.setObjectName("grpNormalEditingTools")
        self.normalEditToolsLayout = QtWidgets.QGridLayout(self.grpNormalEditingTools)
        self.normalEditToolsLayout.setObjectName("normalEditToolsLayout")
        self.pBtnNormalize = QtWidgets.QPushButton(self.grpNormalEditingTools)
        self.pBtnNormalize.setObjectName("pBtnNormalize")
        self.normalEditToolsLayout.addWidget(self.pBtnNormalize, 0, 0, 1, 1)
        self.pBtnInvert = QtWidgets.QPushButton(self.grpNormalEditingTools)
        self.pBtnInvert.setObjectName("pBtnInvert")
        self.normalEditToolsLayout.addWidget(self.pBtnInvert, 0, 1, 1, 1)
        self.pBtnResetNormal = QtWidgets.QPushButton(self.grpNormalEditingTools)
        self.pBtnResetNormal.setObjectName("pBtnResetNormal")
        self.normalEditToolsLayout.addWidget(self.pBtnResetNormal, 0, 2, 1, 1)
        self.pBtnRemakeUserNormal = QtWidgets.QPushButton(self.grpNormalEditingTools)
        self.pBtnRemakeUserNormal.setObjectName("pBtnRemakeUserNormal")
        self.normalEditToolsLayout.addWidget(self.pBtnRemakeUserNormal, 1, 2, 1, 1)
        self.pBtnSmooth = QtWidgets.QPushButton(self.grpNormalEditingTools)
        self.pBtnSmooth.setObjectName("pBtnSmooth")
        self.normalEditToolsLayout.addWidget(self.pBtnSmooth, 1, 0, 1, 1)
        self.userNormalTranslatorLayout.addWidget(self.grpNormalEditingTools, 2, 0, 1, 1)
        self.grpEditValue = QtWidgets.QGroupBox(self.grpBoxUserNormalTranslator)
        self.grpEditValue.setObjectName("grpEditValue")
        self.editValueLayout = QtWidgets.QGridLayout(self.grpEditValue)
        self.editValueLayout.setObjectName("editValueLayout")
        self.pBtnNormalToVertexColor = QtWidgets.QPushButton(self.grpEditValue)
        self.pBtnNormalToVertexColor.setObjectName("pBtnNormalToVertexColor")
        self.editValueLayout.addWidget(self.pBtnNormalToVertexColor, 0, 0, 1, 1)
        self.pBtnVertexColorToNormal = QtWidgets.QPushButton(self.grpEditValue)
        self.pBtnVertexColorToNormal.setObjectName("pBtnVertexColorToNormal")
        self.editValueLayout.addWidget(self.pBtnVertexColorToNormal, 0, 1, 1, 1)
        self.userNormalTranslatorLayout.addWidget(self.grpEditValue, 3, 0, 1, 1)
        self.mainLayout.addWidget(self.grpBoxUserNormalTranslator, 0, 0, 1, 1)
        userNormalTranslatorWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(userNormalTranslatorWindow)
        self.statusbar.setObjectName("statusbar")
        userNormalTranslatorWindow.setStatusBar(self.statusbar)

        self.retranslateUi(userNormalTranslatorWindow)
        QtCore.QMetaObject.connectSlotsByName(userNormalTranslatorWindow)

    def retranslateUi(self, userNormalTranslatorWindow):
        userNormalTranslatorWindow.setWindowTitle("User Normal Translator Window")
        self.grpBoxUserNormalTranslator.setTitle("UserNormalTranslator")
        self.grpBoxOffset.setTitle("Offset")
        self.labMode.setText("Mode")
        self.rdBtnAdd.setText("Add")
        self.rdBtnMultiply.setText("Multiply")
        self.pBtnX.setText("X")
        self.pBtnXValue1.setText("-0.1")
        self.pBtnXValue2.setText("-0.5")
        self.pBtnXValue3.setText("+0.5")
        self.pBtnXValue4.setText("+0.1")
        self.pBtnY.setText("Y")
        self.pBtnYValue1.setText("-0.1")
        self.pBtnYValue2.setText("-0.5")
        self.pBtnYValue3.setText("+0.5")
        self.pBtnYValue4.setText("+0.1")
        self.pBtnZ.setText("Z")
        self.pBtnZValue1.setText("-0.1")
        self.pBtnZValue2.setText("-0.5")
        self.pBtnZValue3.setText("+0.5")
        self.pBtnZValue4.setText("+0.1")
        self.labAbsoluteValue.setText("Absolute Value")
        self.labWorldSpace.setText("World Space")
        self.pBtnOffsetApply.setText("Apply")
        self.pBtnResetValue.setText("Reset")
        self.grpBoxShperize.setTitle("Spherize")
        self.labRation.setText("Ratio")
        self.pBtnRatioValue1.setText("0.1")
        self.pBtnRatioValue3.setText("0.5")
        self.pBtnRatioValue4.setText("0.75")
        self.pBtnRatioValue2.setText("0.25")
        self.pBtnCreateCenter.setText("Create Center")
        self.pBtnSpherizeApply.setText("Apply")
        self.grpNormalEditingTools.setTitle("Normal Editing Tools")
        self.pBtnNormalize.setText("Normalize")
        self.pBtnInvert.setText("Invert")
        self.pBtnResetNormal.setText("Reset")
        self.pBtnRemakeUserNormal.setText("Remake UserNormal")
        self.pBtnSmooth.setText("Smooth")
        self.grpEditValue.setTitle("Edit Value(Use VertrxColor)")
        self.pBtnNormalToVertexColor.setText("Normal To VertexColor")
        self.pBtnVertexColorToNormal.setText("VertexColor To Normal")
