import os
import json
import pyttsx3
from dotenv import load_dotenv
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from PySide6.QtWidgets import (QMainWindow, QTextEdit, QLineEdit, QPushButton, QVBoxLayout, 
                               QWidget, QHBoxLayout)
from PySide6.QtGui import QIcon
from memory_window import MemoryWindow
from memory_viewer_window import MemoryViewerWindow
import warnings

# Suppress all warnings
warnings.filterwarnings("ignore")


load_dotenv()  # Load the environment variables

class ChatWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("MindSync")
        self.setGeometry(100, 100, 400, 500)
        self.setWindowIcon(QIcon("MindSyncLogo.png"))
        # Initialize TTS engine
        self.tts_engine = pyttsx3.init()
        
        # Load tokenizer and model with authentication
        self.hf_token = os.getenv("HF_TOKEN")
        self.tokenizer = AutoTokenizer.from_pretrained("google/gemma-2b-it", use_auth_token=self.hf_token)
        self.model = AutoModelForCausalLM.from_pretrained(
            "google/gemma-2b-it",
            torch_dtype=torch.bfloat16,
            device_map="auto",
            use_auth_token=self.hf_token,
            pad_token_id=self.tokenizer.eos_token_id  # Ensure pad_token_id is set
        )
        
        # Check the device the model is on
        self.device = next(self.model.parameters()).device
        
        # Main layout
        layout = QVBoxLayout()
        
        # Chat display area
        self.chat_display = QTextEdit()
        self.chat_display.setReadOnly(True)
        layout.addWidget(self.chat_display)
        
        # Message input area
        self.message_input = QLineEdit()
        self.message_input.setPlaceholderText("Type your message here...")
        layout.addWidget(self.message_input)
        
        # Send button
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)
        layout.addWidget(send_button)
        
        # Memory buttons layout
        memory_buttons_layout = QHBoxLayout()
        
        # Add Memory button
        add_memory_button = QPushButton("Add Memory")
        add_memory_button.clicked.connect(self.open_memory_window)
        memory_buttons_layout.addWidget(add_memory_button)
        
        # View Memories button
        view_memories_button = QPushButton("View Memories")
        view_memories_button.clicked.connect(self.open_memory_viewer_window)
        memory_buttons_layout.addWidget(view_memories_button)
        
        layout.addLayout(memory_buttons_layout)
        
        # Central widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def open_memory_window(self):
        memory_window = MemoryWindow()
        memory_window.exec()
    
    def open_memory_viewer_window(self):
        memory_viewer_window = MemoryViewerWindow()
        memory_viewer_window.exec()
    
    def send_message(self):
        message = self.message_input.text().strip()
        if message:
            self.chat_display.append(f"User: {message}")
            self.message_input.clear()
            
            # Get AI response
            response = self.get_response(message)
            self.chat_display.append(f"AI: {response}")
            self.speak_text(response)
    
    def get_response(self, message):
        # Load memories
        memories = self.load_memories()
        memory_prompt = self.format_memories(memories)
        
        system_prompt = (
            "You are a helpful assistant. Answer the following question clearly and concisely.\n\n"
        )
        full_prompt = system_prompt + memory_prompt + "User: " + message
        
        input_ids = self.tokenizer(full_prompt, return_tensors="pt").input_ids.to(self.device)
        outputs = self.model.generate(
            input_ids,
            max_length=200,  # Adjust max_length to a reasonable number for responses
            num_return_sequences=1,  # Generate only one response
            eos_token_id=self.tokenizer.eos_token_id,  # End generation at EOS token
            pad_token_id=self.tokenizer.pad_token_id  # Ensure padding is handled
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        # Remove the initial system prompt and user prompt from the response
        response = response.replace(system_prompt + memory_prompt + "User: " + message, "").strip()
        return response
    
    def load_memories(self):
        if os.path.exists("memories.json"):
            with open("memories.json", "r") as file:
                return json.load(file)
        return {}
    
    def format_memories(self, memories):
        memory_prompt = "Memories:\n"
        for category, notes in memories.items():
            memory_prompt += f"{category}:\n"
            for note in notes:
                memory_prompt += f"- {note}\n"
        memory_prompt += "\n"
        return memory_prompt
    
    def speak_text(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()