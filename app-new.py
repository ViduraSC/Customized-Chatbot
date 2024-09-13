import sys
import json
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QFrame, QSizePolicy
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Load custom knowledge from the JSON file
with open('custom_knowledge.json', 'r') as file:
    custom_data = json.load(file)

# Define the template for the chatbot conversation
template = """
You are a knowledgeable assistant from Vertex AI Solutions trained to provide accurate answers based on a custom knowledge base. 

The knowledge base contains information about the following topics:
1. Services offered by the company, including Custom AI Model Development & Integration, Automation & Process Optimization, Cloud Integration, Predictive Analytics & Business Intelligence and Data Engineering Solutions.
2. Frequently asked questions (FAQ) about the company's products and services.
3. Company-specific details like name, industry, achievements, and contact information.

Below is the conversation history: {context}

The user's question is: {question}

Please provide an accurate answer based on the custom knowledge base without mentioning that you are referring to it, ensuring it is relevant and helpful. If you cannot find an answer, acknowledge that the information is not available.

Answer:
"""

# Instantiate the language model and create a prompt template
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

class ChatBubble(QFrame):
    def __init__(self, text, is_user=True, parent=None):
        super().__init__(parent)
        
        # Set up layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(10, 10, 10, 10)
        self.setStyleSheet("background-color: transparent;")  

        # Create a label for the icon
        icon_label = QLabel(self)
        if is_user:
            icon_label.setPixmap(QPixmap("./images/user1.png").scaled(60, 60, Qt.KeepAspectRatio))
            text_align = Qt.AlignLeft
            bubble_color = "#c6f7dc" 
        else:
            icon_label.setPixmap(QPixmap("./images/bot5.png").scaled(60, 60, Qt.KeepAspectRatio))
            text_align = Qt.AlignRight
            bubble_color = "#facdca"

        # Create a label for the chat text
        text_label = QLabel(text, self)
        text_label.setWordWrap(True)
        text_label.setStyleSheet(f"background-color: {bubble_color}; border-radius: 15px; padding: 5px; color: #333333; font-family: 'Poppins'; font-size: 18px;")
        text_label.setMaximumWidth(1800)  # Set a maximum width to make the bubbles consistent
        text_label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)  # Adjusted size policy for proper resizing
        
        # Adjust maximum width to control the size of the bubbles
        text_label.setMaximumWidth(1800)  

        # Adjust minimum height to ensure text visibility
        text_label.setMinimumHeight(text_label.sizeHint().height() + 30)
        
        # Add the widgets to the layout
        if is_user:
            self.layout.addWidget(icon_label)
            self.layout.addWidget(text_label, 1, text_align)
        else:
            self.layout.addWidget(text_label, 1, text_align)
            self.layout.addWidget(icon_label)
        
        # Align the layout
        self.setLayout(self.layout)

class ChatBotUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the layout
        self.layout = QVBoxLayout()

        # Title area with logo
        title_area = QHBoxLayout()
        title_area.setContentsMargins(10, 10, 10, 10)
        title_area.setSpacing(10)

        # Logo label
        logo_label = QLabel(self)
        logo_pixmap = QPixmap("./images/ttest.png").scaled(100, 100, Qt.KeepAspectRatio)  # Adjust the size as needed
        logo_label.setPixmap(logo_pixmap)
        logo_label.setFixedSize(100, 100)  # Set fixed size to keep the logo consistent

        # Title label
        self.title_label = QLabel("VERTEX-AI-CHAT", self)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.title_label.setStyleSheet("""
            background-color: #d5f0e8;
            color: black;
            font-family: 'Poppins';
            font-size: 40px;
            font-weight: bold;
            padding: 15px;
            border-radius: 15px;
            border-bottom: 2px solid #d5f0e8;
            margin: 10px;
        """)

        # Add logo and title to title area
        title_area.addWidget(logo_label)
        title_area.addWidget(self.title_label)

        # Scroll area for the chat display with rounded corners
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("""
            QScrollArea {
                border: 2px solid #ffffff;
                border-radius: 15px;
                background-color: #fcffff;
                margin: 0px;
            }
            QScrollBar:vertical {
                width: 0px;
            }
            QScrollBar:horizontal {
                height: 0px;
            }
        """)

        self.scroll_content = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_layout.setAlignment(Qt.AlignTop)
        self.scroll_content.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_content)
        
        # Input area layout (Input field + Send button)
        input_area = QHBoxLayout()
        input_area.setContentsMargins(10, 10, 10, 10)
        input_area.setSpacing(10)

        # Input field for the user's message
        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Ask anything...")
        self.input_field.returnPressed.connect(self.send_message)
        self.input_field.setStyleSheet("""
            background-color: #FFFFFF;
            color: #333333;
            font-family: 'Poppins';
            font-size: 20px;
            padding: 10px;
            border-radius: 15px;
            border: 3px solid #303030;
        """)

        # Send button without transition and transform
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.send_message)
        self.send_button.setStyleSheet("""
            QPushButton {
                background-color: #3d3c3c;
                color: white;
                font-family: 'Poppins';
                font-size: 20px;
                padding: 10px;
                border-radius: 10px;
                border: none;
            }
            QPushButton:hover {
                background-color: #3d3c3c;
            }
            QPushButton:pressed {
                background-color: #030303;
            }
        """)

        # Set proportions: 90% for input field, 10% for send button
        input_area.addWidget(self.input_field, 9)  # 90% space
        input_area.addWidget(self.send_button, 1)  # 10% space

        # Add widgets to the main layout
        self.layout.addLayout(title_area)  # Add the title area with logo and title
        self.layout.addWidget(self.scroll_area)
        self.layout.addLayout(input_area)  # Add the input area with input field and send button

        # Set layout for the main window
        self.setLayout(self.layout)

        # Set main window properties
        self.setWindowTitle("Vertex AI")
        self.setGeometry(100, 100, 600, 900)
        self.setStyleSheet("background-color: #ffffff;")  # Main Window Color
        self.show()

        # Initialize conversation context
        self.context = ""

    def send_message(self):
        user_input = self.input_field.text()
        if user_input.strip() == "":
            return

        # Add user's message bubble
        user_bubble = ChatBubble(user_input, is_user=True)
        self.scroll_layout.addWidget(user_bubble)

        self.input_field.clear()

        # Check if the question relates to custom knowledge
        custom_response = self.get_custom_response(user_input)
        if custom_response:
            result = custom_response
        else:
            # Get the chatbot's response by invoking the chain (existing model knowledge)
            result = chain.invoke({"context": self.context, "question": user_input})

        # Add bot's response bubble
        bot_bubble = ChatBubble(result, is_user=False)
        self.scroll_layout.addWidget(bot_bubble)

        # Scroll to the bottom
        self.scroll_area.verticalScrollBar().setValue(self.scroll_area.verticalScrollBar().maximum())

        # Update the context
        self.context += f"\nUser: {user_input}\nAI: {result}"

    def get_custom_response(self, question):
        """Check if the question is related to custom knowledge."""
        question_lower = question.lower()

        # Check for custom services
        if "ai models" in question_lower:
            return custom_data["services"][0]["description"]
        elif "automation" in question_lower:
            return custom_data["services"][1]["description"]
        elif "cloud integration" in question_lower:
            return custom_data["services"][2]["description"]
        elif "predictive analytics" in question_lower:
            return custom_data["services"][3]["description"]

        # Check for common FAQ
        for faq in custom_data["faq"]:
            if faq["question"].lower() in question_lower:
                return faq["answer"]

        # Check for other custom attributes
        if any(term in question_lower for term in [
            "company name", 
            "what's your company",
            "what's this company",
            "what is this company",
            "what is your company", 
            "who are you", 
            "what is your company called", 
            "name of your company"
        ]):
            return f"We are {custom_data['company_name']}."

        elif any(term in question_lower for term in [
            "founder", 
            "owner"
        ]):
            return f"{custom_data['founder']} is the founder of Vertex AI Solution."

        elif any(term in question_lower for term in [
            "industry", 
            "what industry", 
            "operates in", 
            "business sector",
            "do you do"
        ]):
            return f"{custom_data['company_name']} operates in the {custom_data['industry']} industry."

        elif any(term in question_lower for term in [
            "hi", 
            "hello", 
            "good morning", 
            "good afternoon", 
            "good night", 
            "excuse me"
        ]):
            return f"Hello, I am an AI assistant from Vertex AI Solutions. How can I help you?"

        elif any(term in question_lower for term in [
            "targeted industries",
            "related to"
        ]):
            return f"We are building solutions in {custom_data['target_industries']} industries."

        elif any(term in question_lower for term in [
            "achievements", 
            "accomplishments", 
            "company milestones",
            "projects",
            "tasks", 
            "success stories"
        ]):
            return f"Some achievements include: {', '.join(custom_data['achievements'])}."

        elif any(term in question_lower for term in [
            "contact", 
            "how to reach", 
            "contact information", 
            "get in touch"
        ]):
            return f"You can contact us at {custom_data['contact_information']['email']} or {custom_data['contact_information']['phone']}."

        elif any(term in question_lower for term in [
            "address", 
            "location", 
            "head office", 
            "place"
        ]):
            return f"Our head office is located at {custom_data['contact_information']['location']}."

        return None

def main():
    app = QApplication(sys.argv)
    chatbot_ui = ChatBotUI()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
