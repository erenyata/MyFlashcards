import mysql.connector
from PyQt5 import QtWidgets, QtCore, uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

import sys
import random
from connection import conncection

cursor = conncection.cursor()
class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui",self)
        self.btnAdd.clicked.connect(self.add_word)
        self.btnGetWord.clicked.connect(self.get_word)
        self.btnAnswer.clicked.connect(self.answer)
        self.setWindowIcon(QIcon("icon.ico"))

    def add_word(self):
        try:
            query = "insert into italian_flashcards(word,turkish) values(%s,%s)"
            flashcard = self.edit_word.text().split(",")
            params = (flashcard[0],flashcard[1])
            cursor.execute(query,params)
            conncection.commit()
            self.secondary_lbl.setText("Başarıyla kaydedildi.")
            self.secondary_lbl.show()
        except :
            self.secondary_lbl.setText(f"Bir hata oluştu")

    def get_column_len(self):
        cursor.execute("select * from italian_flashcards")
        columns = cursor.fetchall()
        return len(columns)

    def get_word(self):
        try:
            columns_lenght = self.get_column_len()
            id = random.randint(1,columns_lenght)
            if id == columns_lenght:  id -= 1
            query = "select * from italian_flashcards where id = %s"
            params = (id,)
            cursor.execute(query,params)
            word = cursor.fetchone()
            print(word)
            self.main_lbl.setText(word[1])
            self.secondary_lbl.setText(word[2])
            self.secondary_lbl.hide()

        except mysql.connector.Error as e:
            self.secondary_lbl.setText(f"Bir hata oluştu " + str(e))

    def answer(self):
        self.secondary_lbl.show()
        

                        


        
    

    



app = QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec())