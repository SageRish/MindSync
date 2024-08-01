from PySide6.QtWidgets import QApplication
from chat_window import ChatWindow
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec())