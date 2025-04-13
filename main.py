import pyautogui
import time
import pyperclip
from openai import OpenAI;


client= OpenAI("use your own apikeys")


def is_last_message_from_sender(chat_log, sender_name="patner"):
    # 1. Split the chat log into individual messages
    messages = chat_log.strip().split("/2024] ")[-1]
    if sender_name in messages:
        return True 
    return False

# 2.Give some time to switch to the correct screen
time.sleep(3)

#  3.Click on the icon at (681,1049)
pyautogui.click(1389, 1051)
time.sleep(1)  # Wait for the app to open

# 4.Move to starting position and drag to select text
pyautogui.moveTo(724, 404)
#pyautogui.mouseDown()
pyautogui.dragTo(1820, 891, duration=1)
#pyautogui.mouseUp()

# 5. Copy to clipboard (Ctrl+C)
pyautogui.hotkey('ctrl', 'c')
time.sleep(2)  # Wait for copy operation
pyautogui.click(707,437)

# 6. Retrieve text from clipboard
chat_history = pyperclip.paste()

# 7.Print the copied text
print(chat_history)

response = client.chat.completion.create(
    model="gpt-4o-mini",
    messages= [
        { "role": "system", "content": "You are a person named Suman who speaks hindi as well as english. You are from India and you are a coder. You analyze chat history and roast people in a funny way. Output should be the next chat response (text message only)" },
        {"role": "system", "content": "Do not start like this [21:02, 12/6/2024] patner: "},
        {
            "role": "user",
            "content": chat_history,
        },
    ],
)
print(response.choices[0].message.content)
pyperclip.copy(response)

# 8.Click at (1240, 956) to paste the copied text
pyautogui.click(1240, 956)
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'v')
time.sleep(1)

# 9.Press Enter
pyautogui.press('enter')

# 10.Print the copied text
#print("Copied Text:", chat_history)
