import sys
import os
import pynput

from pynput.keyboard import Key, Listener


def on_press(key):
    print('{0} pressed'.format(
        key))


def on_release(key):
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()


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


log = Logger("Logs.txt")
log.write_to_file("Logs from the keyboard will be stored here.")
log.read_from_file()
