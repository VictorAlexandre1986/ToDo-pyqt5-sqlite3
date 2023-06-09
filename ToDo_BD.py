# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ToDo_BD.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(334, 547)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_AddItem = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.adicionar())
        self.btn_AddItem.setGeometry(QtCore.QRect(10, 40, 75, 23))
        self.btn_AddItem.setObjectName("btn_AddItem")
        self.btn_DeleteItem = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.remover())
        self.btn_DeleteItem.setGeometry(QtCore.QRect(90, 40, 75, 23))
        self.btn_DeleteItem.setObjectName("btn_DeleteItem")
        self.btn_Clear = QtWidgets.QPushButton(self.centralwidget, clicked=lambda:self.limpar())
        self.btn_Clear.setGeometry(QtCore.QRect(170, 40, 75, 23))
        self.btn_Clear.setObjectName("btn_Clear")
        self.txb_item = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_item.setGeometry(QtCore.QRect(10, 10, 311, 20))
        self.txb_item.setObjectName("txb_item")
        self.View_minhaLista = QtWidgets.QListWidget(self.centralwidget)
        self.View_minhaLista.setGeometry(QtCore.QRect(10, 80, 311, 441))
        self.View_minhaLista.setObjectName("View_minhaLista")
        self.btn_bd = QtWidgets.QPushButton(self.centralwidget, clicked= lambda: self.salvar_bd())
        self.btn_bd.setGeometry(QtCore.QRect(250, 40, 75, 23))
        self.btn_bd.setObjectName("btn_bd")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 334, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.grab_all()


    def grab_all(self):
        conn = sqlite3.connect('mylist.db')

        c = conn.cursor()

        # c.execute(""" CREATE TABLE if not exists todo_list(
        #     list_item text
        # )""")
        c.execute("SELECT * FROM todo_list")
        records = c.fetchall()

        conn.commit()

        conn.close()
        
        for record in records:
            self.View_minhaLista.addItem(str(record[0]))
        
    def adicionar(self,):
        
        #Pegando o valor do textbox
        item = self.txb_item.text()
        #Armazenando na View
        self.View_minhaLista.addItem(item)
        #Limpando o textbox
        self.txb_item.setText("")
        

    
    def remover(self):
        #Pegando o indice do selecionado
        clicked = self.View_minhaLista.currentRow()
        #Deletando linha
        self.View_minhaLista.takeItem(clicked)
    
    def limpar(self):
        self.View_minhaLista.clear()
        
    def salvar_bd(self):
        conn = sqlite3.connect('mylist.db')

        c = conn.cursor()
        
        c.execute("DELETE FROM todo_list;",)
        
        items = []
        #Armazenando os dados na lista
        for index in range(self.View_minhaLista.count()):
            items.append(self.View_minhaLista.item(index))
            
        for item in items:
            c.execute("INSERT INTO todo_list VALUES (:item) ",
                      {
                          'item': item.text(),
                      })
        conn.commit()

        conn.close()
        
        msg = QMessageBox()
        msg.setWindowTitle("Salvo na base de dados!!")
        msg.setText("Sua ToDo list foi salva!")
        msg.setIcon(QMessageBox.Information)
        x = msg.exec_()
            
        
            
        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "To do List"))
        self.btn_AddItem.setText(_translate("MainWindow", "Add"))
        self.btn_DeleteItem.setText(_translate("MainWindow", "Delete"))
        self.btn_Clear.setText(_translate("MainWindow", "Clear List"))
        self.btn_bd.setText(_translate("MainWindow", "Save BD"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
