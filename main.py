from PySide2.QtWidgets import QMainWindow, QApplication
from ui_MainForm import Ui_MainWindow
import os
import sys

# CAMINHA DO TEMA
STR_THEME_PATH = "themes/[THEME_NAME]/theme.qss"

# NOME DA PASTA TEMA
# Combinear, Darkeum, Fibers, Fibrary, Genetive, Wstartpage
STR_THEME_NAME = 'Combinear'

# CREATE PRINCIPAL FORM 
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Objeto com informações da class Ui_MainWindow.
        # Arquivo: ui_MainForm.py
        self.ui = Ui_MainWindow()

        # Setando valor nome do tema que será usado.
        themeFile = STR_THEME_PATH.replace('[THEME_NAME]', STR_THEME_NAME)

        # Setando informações do forms e criando "componentes".
        self.ui.setupUi(self)

        # Setando estilo do tema.
        self.theme(themeFile)

        # Abrindo o form.
        self.show()

    def theme(self, file):
        str_ = open(file, 'r').read()
        '''Note: Creating a main window without a central 
        widget is not supported. You must have a central 
        widget even if it is just a placeholder.
        https://doc.qt.io/qt-5/qmainwindow.html#creating-main-window-components'''
        self.ui.centralwidget.setStyleSheet(str_)


if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
    except Exception as err:
        print(err)
