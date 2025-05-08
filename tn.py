import tkinter as tk
from tkinter import filedialog, scrolledtext
import os

# Simulated basic response logic
def get_bot_response(user_input):
    user_input = user_input.lower()
    if "refund" in user_input:
        return "I'm sorry to hear that. Let me help you with the refund process."
    elif "broken" in user_input or "damage" in user_input:
        return "Could you please upload an image of the damaged item?"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    else:
        return "Thank you for your message. A support agent will get back to you shortly."

# Image upload handler
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png *.jpg *.jpeg")])
    if file_path:
        chat_window.insert(tk.END, "You uploaded: " + os.path.basename(file_path) + "\n")
        chat_window.insert(tk.END, "Support Bot: Thank you for uploading the image. We'll review it.\n")

# Send message handler
def send_message():
    user_message = user_input.get()
    if user_message.strip() == "":
        return
    chat_window.insert(tk.END, "You: " + user_message + "\n")
    response = get_bot_response(user_message)
    chat_window.insert(tk.END, "Support Bot: " + response + "\n")
    user_input.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("Visual Customer Support System")

chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20)
chat_window.pack(padx=10, pady=10)

user_input = tk.Entry(root, width=50)
user_input.pack(side=tk.LEFT, padx=10, pady=5)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(side=tk.LEFT)

upload_button = tk.Button(root, text="Upload Image", command=upload_image)
upload_button.pack(side=tk.LEFT, padx=5)

root.mainloop()