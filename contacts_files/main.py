''' this module privede contacts application'''
import sys
from PySide6.QtWidgets import QApplication
from .views import Window
from .database import create_connection

def main():
    ''' contacts main function '''
    app = QApplication(sys.argv)
    if not create_connection('contacts.sqlite'):
        sys.exit(1)
    win = Window()
    win.show()
    sys.exit(app.exec())