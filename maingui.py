# Form implementation generated from reading ui file 'MainGui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 493)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.toolButton_addLivro = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton_addLivro.setGeometry(QtCore.QRect(620, 50, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_addLivro.setFont(font)
        self.toolButton_addLivro.setStyleSheet("QToolButton{\n"
"background: rgb(85, 170, 0)\n"
"\n"
"}\n"
"")
        self.toolButton_addLivro.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_addLivro.setObjectName("toolButton_addLivro")
        self.toolButton_addMembro = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton_addMembro.setGeometry(QtCore.QRect(620, 150, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_addMembro.setFont(font)
        self.toolButton_addMembro.setStyleSheet("QToolButton{\n"
"background: rgb(170, 85, 255)\n"
"\n"
"}\n"
"")
        self.toolButton_addMembro.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_addMembro.setObjectName("toolButton_addMembro")
        self.toolButton_livros = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton_livros.setGeometry(QtCore.QRect(620, 250, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_livros.setFont(font)
        self.toolButton_livros.setStyleSheet("QToolButton{\n"
"background: rgb(85, 170, 255)\n"
"\n"
"}\n"
"")
        self.toolButton_livros.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_livros.setObjectName("toolButton_livros")
        self.toolButton_membros = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton_membros.setGeometry(QtCore.QRect(620, 350, 121, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.toolButton_membros.setFont(font)
        self.toolButton_membros.setStyleSheet("QToolButton{\n"
"background: rgb(255, 170, 0)\n"
"\n"
"}\n"
"")
        self.toolButton_membros.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_membros.setObjectName("toolButton_membros")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 601, 451))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(parent=self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 571, 401))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalWidget = QtWidgets.QWidget(parent=self.layoutWidget)
        self.horizontalWidget.setStyleSheet("QWidget{\n"
"background-color:rgb(218,218,218)\n"
"}")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.lineEdit_livroID = QtWidgets.QLineEdit(parent=self.horizontalWidget)
        self.lineEdit_livroID.setGeometry(QtCore.QRect(9, 49, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_livroID.setFont(font)
        self.lineEdit_livroID.setText("")
        self.lineEdit_livroID.setObjectName("lineEdit_livroID")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.horizontalWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(400, 30, 136, 71))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_livro_nome = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_livro_nome.setFont(font)
        self.label_livro_nome.setObjectName("label_livro_nome")
        self.verticalLayout.addWidget(self.label_livro_nome)
        self.label_livro_autoria = QtWidgets.QLabel(parent=self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_livro_autoria.setFont(font)
        self.label_livro_autoria.setObjectName("label_livro_autoria")
        self.verticalLayout.addWidget(self.label_livro_autoria)
        self.verticalLayout_3.addWidget(self.horizontalWidget)
        self.horizontalWidget_2 = QtWidgets.QWidget(parent=self.layoutWidget)
        self.horizontalWidget_2.setStyleSheet("QWidget{\n"
"background-color:rgb(218,218,218)\n"
"}")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.lineEdit_CPF = QtWidgets.QLineEdit(parent=self.horizontalWidget_2)
        self.lineEdit_CPF.setGeometry(QtCore.QRect(9, 49, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_CPF.setFont(font)
        self.lineEdit_CPF.setObjectName("lineEdit_CPF")
        self.layoutWidget2 = QtWidgets.QWidget(parent=self.horizontalWidget_2)
        self.layoutWidget2.setGeometry(QtCore.QRect(400, 20, 121, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_membro_nome = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_membro_nome.setFont(font)
        self.label_membro_nome.setObjectName("label_membro_nome")
        self.verticalLayout_5.addWidget(self.label_membro_nome)
        self.label_membro_contato = QtWidgets.QLabel(parent=self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        self.label_membro_contato.setFont(font)
        self.label_membro_contato.setObjectName("label_membro_contato")
        self.verticalLayout_5.addWidget(self.label_membro_contato)
        self.verticalLayout_3.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.toolButton_alugar = QtWidgets.QToolButton(parent=self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.toolButton_alugar.setFont(font)
        self.toolButton_alugar.setStyleSheet("QToolButton{\n"
"background: rgb(255, 170, 127)\n"
"}\n"
"")
        self.toolButton_alugar.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        self.toolButton_alugar.setObjectName("toolButton_alugar")
        self.horizontalLayout_4.addWidget(self.toolButton_alugar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lineEdit_busca = QtWidgets.QLineEdit(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_busca.setFont(font)
        self.lineEdit_busca.setStyleSheet("QLineEdit{\n"
"background-color:rgb(218,218,218)\n"
"}")
        self.lineEdit_busca.setObjectName("lineEdit_busca")
        self.verticalLayout_4.addWidget(self.lineEdit_busca)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet("QTableWidget{\n"
"background-color:rgb(218,218,218)\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.toolButton_renovar = QtWidgets.QToolButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.toolButton_renovar.setFont(font)
        self.toolButton_renovar.setStyleSheet("QToolButton{\n"
"background: rgb(255, 170, 127)\n"
"}")
        self.toolButton_renovar.setObjectName("toolButton_renovar")
        self.horizontalLayout_5.addWidget(self.toolButton_renovar)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.toolButton_devolver = QtWidgets.QToolButton(parent=self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.toolButton_devolver.setFont(font)
        self.toolButton_devolver.setStyleSheet("QToolButton{\n"
"background: rgb(255, 170, 127)\n"
"}")
        self.toolButton_devolver.setObjectName("toolButton_devolver")
        self.horizontalLayout_5.addWidget(self.toolButton_devolver)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolButton_addLivro.setText(_translate("MainWindow", "Inserir Livro"))
        self.toolButton_addMembro.setText(_translate("MainWindow", "Inserir Membro"))
        self.toolButton_livros.setText(_translate("MainWindow", "Livros"))
        self.toolButton_membros.setText(_translate("MainWindow", "Membros"))
        self.lineEdit_livroID.setPlaceholderText(_translate("MainWindow", "Insira o ID do Livro"))
        self.label_livro_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_livro_autoria.setText(_translate("MainWindow", "Autoria:"))
        self.lineEdit_CPF.setPlaceholderText(_translate("MainWindow", "Insira o CPF do Membro"))
        self.label_membro_nome.setText(_translate("MainWindow", "Nome:"))
        self.label_membro_contato.setText(_translate("MainWindow", "Contato:"))
        self.toolButton_alugar.setText(_translate("MainWindow", "Alugar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Alugar Livro"))
        self.lineEdit_busca.setPlaceholderText(_translate("MainWindow", "Buscar..."))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "LivroID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "CPF"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "DataAluguel"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Renovacoes"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Livro"))
        self.toolButton_renovar.setText(_translate("MainWindow", "Renovar Aluguel"))
        self.toolButton_devolver.setText(_translate("MainWindow", "Devolver Livro"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Renovar/Devolver Livros"))

