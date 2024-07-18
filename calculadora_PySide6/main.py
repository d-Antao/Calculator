import sys

import qdarktheme
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from buttons import Button, ButtonsGrid
from display import Display, Info
from main_window import MainWindow
from styles import setupTheme
from variables import WINDOW_ICON_PATH

if sys.platform.startswith('win'):
        import ctypes
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            u'CompanyName.ProductName.SubProduct.VersionInformation')  # Arbitrary string

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    dark_stylesheet = qdarktheme.load_stylesheet('dark')  # ou dark
    window = MainWindow()
    
    print("test")
    
    #Icon difine   
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)
    
    #Info
    info = Info('')
    window.addTooVLayout(info)
    
    
    #Display
    display = Display()
    window.addTooVLayout(display)
    
    #Gride
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)
    
   
    
    app.setStyleSheet(dark_stylesheet)

     
    window.adjustFixedSize()
    window.show()
    app.exec()
    
import pathlib; print(pathlib.Path().absolute()) 
