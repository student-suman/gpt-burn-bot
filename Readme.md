🤖 Auto-Roaster Bot – ChatGPT + PyAutoGUI Automation
This project automates a funny chat responder using pyautogui and OpenAI's GPT model. It simulates user behavior to read the latest chat messages, processes them with a custom roast-bot, and replies automatically.

📂 Features
Reads the latest message from a chat window.

Sends the chat history to OpenAI GPT-4o-mini with a humorous Hindi-English prompt.

Generates a roasting/funny reply.

Automatically pastes and sends the generated response in the chat app.

🔧 Requirements
Install the required Python packages:

bash
Copy code
pip install openai pyautogui pyperclip
🧠 How It Works
Initial Delay: Waits for you to open the correct screen.

Text Selection: Simulates mouse drag to select chat history.

Copy & Paste: Uses clipboard to retrieve text and send response.

OpenAI API: Sends the chat history to GPT-4o-mini with a desi coder roast personality.

Auto-Reply: Clicks on the message box, pastes the funny response, and hits "Enter".

🔒 Important Notes:-
API Key: Make sure you secure your OpenAI API key (api_key="..."). Do not share this publicly.

Coordinates: Mouse positions (pyautogui.click(...)) are hardcoded. Update them as per your screen resolution and layout.

Chat App: This is intended to work with apps like WhatsApp Desktop or any app with a visible chat window. Customize positions accordingly.

🚀 Usage:
Open the target chat application.

Run the script using:

bash:
Copy code
python auto_roaster.py
Make sure the cursor is ready and your chat is open. The bot will take care of the rest.

⚠️ Disclaimer
This script simulates real mouse and keyboard actions. Do not use it while doing sensitive tasks. It's built for fun and educational purposes.

💡 Future Improvements
Dynamic screen position detection

Error handling for empty clipboard

Add GUI for setup

Multilingual roasting support 😂

👨‍💻 Author
Suman – Desi Coder, Half Roaster, Full Funny 😎