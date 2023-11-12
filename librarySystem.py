from PyQt6.QtWidgets import QMainWindow, QDialog, QMessageBox, QTableWidgetItem
import sys
from PyQt6.QtWidgets import QApplication
from maingui import Ui_MainWindow
from addlivro import AddLivro_Dialog
from addmembro import AddMembro_Dialog
from viewlivros import ViewLivros_Dialog
from viewmembros import ViewMembros_Dialog
import mysql.connector as mc

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_addLivro.clicked.connect(self.add_livro)
        self.toolButton_addMembro.clicked.connect(self.add_membro)
        self.toolButton_livros.clicked.connect(self.view_livros)
        self.toolButton_membros.clicked.connect(self.view_membros)

        self.toolButton_alugar.clicked.connect(self.alugar)
        self.lineEdit_livroID.returnPressed.connect(self.mostrar_livro)
        self.lineEdit_CPF.returnPressed.connect(self.mostrar_membro)

        self.listar_emprestimos()
        self.lineEdit_busca.returnPressed.connect(self.buscar_emprestimos)
        self.toolButton_renovar.clicked.connect(self.renovar_aluguel)
        self.toolButton_devolver.clicked.connect(self.devolver_livro)

    def devolver_livro(self):
        linha = self.tableWidget.currentRow() 
        if linha == -1:
            QMessageBox.about(self, "issue book", "selecione um item")
            return
        try:
            livroID = self.tableWidget.item(linha,0).text()
            livroID = livroID.replace('b0', '')
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )
            mycursor = mydb.cursor()
            query = "DELETE FROM emprestimos WHERE livroID ='"+livroID+"'"
            query2 = "UPDATE livros SET disponivel = 1 WHERE id ='"+livroID+"'"

            mycursor.execute(query2)
            mycursor.execute(query)
            mydb.commit()

            QMessageBox.about(self, "submit book", "success")
            self.listar_emprestimos()

        except mc.Error as e:
            print("Error")


    def renovar_aluguel(self):
        linha = self.tableWidget.currentRow() 
        if linha == -1:
            QMessageBox.about(self, "issue book", "selecione um item")
            return
        try:
            livroID = self.tableWidget.item(linha,0).text()
            livroID = livroID.replace('b0', '')

            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT renovacoes FROM emprestimos WHERE livroID='"+livroID+"'")
            res = mycursor.fetchone()
            interacoes = res[0] + 1

            query = "UPDATE emprestimos SET renovacoes = (%s) WHERE livroID='"+livroID+"'"
            mycursor.execute(query, (interacoes,))
            mydb.commit()

            QMessageBox.about(self, "issue book", "success")
            self.listar_emprestimos()

        except mc.Error as e:
            print("Error", e)

    def add_livro(self):
        dialog = QDialog()
        ui = AddLivro_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def add_membro(self):
        dialog = QDialog()
        ui = AddMembro_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def view_membros(self):
        dialog = QDialog()
        ui = ViewMembros_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def view_livros(self):
        dialog = QDialog()
        ui = ViewLivros_Dialog()
        ui.setupUi(dialog)
        dialog.exec()

    def alugar(self):
        livroID = self.lineEdit_livroID.text()
        membroCPF = self.lineEdit_CPF.text()
        if livroID=="" or membroCPF=="":
            return
        
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )
            mycursor = mydb.cursor()
            query = "INSERT INTO emprestimos (livroID, membroCPF) VALUES (%s,%s)"
            query2 = "UPDATE livros SET disponivel = FALSE WHERE id='"+livroID+"'"
            value = (livroID, membroCPF)

            mycursor.execute(query2)
            mycursor.execute(query, value)
            mydb.commit()

            QMessageBox.about(self, "issue book", "success")

            self.lineEdit_livroID.setText("")
            self.lineEdit_CPF.setText("")

        except mc.Error as e:
            print("Error", e)

    def listar_emprestimos(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )
            mycursor = mydb.cursor()
            mycursor.execute("SELECT livroID, membroCPF, dataEmprestimo, renovacoes FROM emprestimos")
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for num_linha, linha in enumerate(result):
                self.tableWidget.insertRow(num_linha)
                for num_col, item in enumerate(linha):
                    if num_col == 0:
                        item = 'b0'+str(item)
                    self.tableWidget.setItem(num_linha,num_col,QTableWidgetItem(str(item)))

        except mc.Error as e:
            print("Error",e)


    def buscar_emprestimos(self):
        string_busca = self.lineEdit_busca.text()
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )

            mycursor = mydb.cursor()
            if string_busca.find("b0") == 0:
                string_busca = string_busca.replace('b0', '')
                mycursor.execute("SELECT livroID, membroCPF, dataEmprestimo, renovacoes FROM emprestimos WHERE livroID = '"+string_busca+"'")

            # mycursor.execute("SELECT livroID, membroCPF, dataEmprestimo, renovacoes FROM emprestimos WHERE livroID = '"+string_busca+"'")
            result = mycursor.fetchall()

            self.tableWidget.setRowCount(0)
            for num_linha, linha in enumerate(result):
                self.tableWidget.insertRow(num_linha)
                for num_col, item in enumerate(linha):
                    if num_col == 0:
                        item = 'b0'+str(item)
                    self.tableWidget.setItem(num_linha,num_col,QTableWidgetItem(str(item)))

        except mc.Error as e:
            print("Error",e)








    def mostrar_livro(self):
        id = self.lineEdit_livroID.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )
            mycursor = mydb.cursor()
            query = "SELECT titulo, autoria, editora, disponivel FROM livros WHERE id = '"+id+"'"
            mycursor.execute(query)
            result = mycursor.fetchall() 

            for linha in result:
                self.label_livro_nome.setText(linha[0])
                self.label_livro_autoria.setText(linha[1])
            
        except mc.Error as e:
            print("Error", e)

    def mostrar_membro(self):
        cpf = self.lineEdit_CPF.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="biblioteca"
            )
            mycursor = mydb.cursor()
            query = "SELECT nome, email FROM membros WHERE cpf = '"+cpf+"'"
            mycursor.execute(query)
            result = mycursor.fetchall() 

            for linha in result:
                self.label_membro_nome.setText(linha[0])
                self.label_membro_contato.setText(linha[1])
            
        except mc.Error as e:
            print("Error", e)






app = QApplication(sys.argv)

window = LibrarySystem()

sys.exit(app.exec())