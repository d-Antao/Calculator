
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QKeyEvent
from PySide6.QtWidgets import QLabel, QLineEdit, QWidget

from utils import isEmpty, isNumOrDot
from variables import (BIG_FONT_SIZE, MINIMUM_WIDTH, SMALL_FONT_SIZE,
                       TEXT_MARGINS)


class Display(QLineEdit):
    eqPressed = Signal()
    delPressed = Signal()
    clearPressed = Signal()
    inputPressed = Signal(str)
    operatorPressed = Signal(str)
    
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
        
    def configStyle(self):
        margins = [TEXT_MARGINS for _ in range(4)]
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px')
        self.setMinimumHeight(BIG_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setTextMargins(*margins)
        
    def keyPressEvent(self, event: QKeyEvent) -> None:
        text = event.text().strip()
        key = event.key()
        KEYS = Qt.Key

        isEnter = key in [KEYS.Key_Enter, KEYS.Key_Return, KEYS.Key_Equal]
        isDelete = key in [KEYS.Key_Backspace]
        isClear = key in [KEYS.Key_Escape, KEYS.Key_Delete]
        isOperator = key in [
            KEYS.Key_Plus, KEYS.Key_Minus, KEYS.Key_Slash, KEYS.Key_Asterisk,
             KEYS.Key_AsciiCircum
        ]
        print("Git test")
        print("Test git")
        if isEnter:
            self.eqPressed.emit()
            return event.ignore()
        
        if isDelete:
            self.delPressed.emit()
            return event.ignore()

        if isClear:
            self.clearPressed.emit()
            return event.ignore()
        
        if isOperator:
            self.operatorPressed.emit(text)
            return event.ignore()

        # Não passar daqui se não tiver texto
        if isEmpty(text):
            return event.ignore()

        if isNumOrDot(text):
            self.inputPressed.emit(text)
            return event.ignore()
        

class Info(QLabel):
    def __init__(self, text : str, parents: QWidget | None = None) -> None:
        super().__init__(text,parents)
        self.configStyle()
    
    def configStyle(self):
        self.setStyleSheet(f'font-size: {SMALL_FONT_SIZE}px')
        self.setMinimumHeight(SMALL_FONT_SIZE * 2)
        self.setMinimumWidth(MINIMUM_WIDTH)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
