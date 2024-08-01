import json
import os
from PySide6.QtWidgets import (QLineEdit, QVBoxLayout, QComboBox, QLabel, QDialog, QDialogButtonBox)
from PySide6.QtGui import QIcon

class MemoryWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Add Memory")
        self.setGeometry(200, 200, 300, 200)
        self.setWindowIcon(QIcon("MindSyncLogo.png"))
        layout = QVBoxLayout()
        
        # Category selection
        self.category_label = QLabel("Select Category:")
        layout.addWidget(self.category_label)
        
        self.category_combobox = QComboBox()
        self.category_combobox.addItems(["Home", "Health", "Work"])
        layout.addWidget(self.category_combobox)
        
        # Memory input
        self.memory_input = QLineEdit()
        self.memory_input.setPlaceholderText("Type your memory here...")
        layout.addWidget(self.memory_input)
        
        # Save button
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.save_memory)
        buttons.rejected.connect(self.reject)
        layout.addWidget(buttons)
        
        self.setLayout(layout)
    
    def save_memory(self):
        category = self.category_combobox.currentText()
        memory = self.memory_input.text().strip()
        
        if memory:
            data = {}
            if os.path.exists("memories.json"):
                with open("memories.json", "r") as file:
                    data = json.load(file)
            
            if category not in data:
                data[category] = []
            
            data[category].append(memory)
            
            with open("memories.json", "w") as file:
                json.dump(data, file, indent=4)
            
            self.accept()