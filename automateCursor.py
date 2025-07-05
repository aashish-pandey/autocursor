import pyautogui
import time

# Configuration
message = "Hello everyone"  # The message you want to send
repeat = 500  # Number of times to send the message
delay = 1  # Delay between each message (in seconds)

# Inform the user about starting
print("Automation will start in 5 seconds. Please focus the input field.")
time.sleep(5)  # Give time to focus on the messaging app

# Send the message repeatedly
for i in range(repeat):
    pyautogui.write(message)  # Type the message
    pyautogui.press("enter")  # Press Enter to send
    time.sleep(delay)  # Wait before sending the next message

print("Messages sent!")