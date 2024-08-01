import json
import os
from PySide6.QtWidgets import (QTextEdit, QVBoxLayout, QDialog)
from PySide6.QtGui import QIcon

class MemoryViewerWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("View Memories")
        self.setGeometry(200, 200, 400, 300)
        self.setWindowIcon(QIcon("MindSyncLogo.png"))
        layout = QVBoxLayout()
        
        self.memory_display = QTextEdit()
        self.memory_display.setReadOnly(True)
        layout.addWidget(self.memory_display)
        
        self.setLayout(layout)
        self.load_memories()
    
    def load_memories(self):
        if os.path.exists("memories.json"):
            with open("memories.json", "r") as file:
                memories = json.load(file)
                self.display_memories(memories)
    
    def display_memories(self, memories):
        memory_text = "Stored Memories:\n"
        for category, notes in memories.items():
            memory_text += f"{category}:\n"
            for note in notes:
                memory_text += f" - {note}\n"
            memory_text += "\n"
        self.memory_display.setText(memory_text)
