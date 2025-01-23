import pyperclip
import keyboard
from gtts import gTTS
import os

def read_selected_text():
    try:
        # Get text from clipboard
        selected_text = pyperclip.paste().strip()
        
        if selected_text:
            print(f"Reading: {selected_text}")
            
            # Convert text to speech
            tts = gTTS(text=selected_text, lang='en')
            audio_file = "selected_text.mp3"
            tts.save(audio_file)
            
            # Play the audio
            os.system(f"start {audio_file}" if os.name == "nt" else f"open {audio_file}")
        else:
            print("No text found on the clipboard. Please select and copy text first.")
    except Exception as e:
        print(f"Error: {e}")

# Bind a hotkey to trigger the read_selected_text function
print("Press Ctrl+Alt+P to read the selected text.")
keyboard.add_hotkey("ctrl+alt+p", read_selected_text)

# Keep the script running
keyboard.wait("esc")  # Press 'Esc' to exit the script
