import numpy as np
import pyautogui
import time
from PIL import ImageGrab, ImageOps


def restart():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')


def jump():
    pyautogui.keyUp('down')
    pyautogui.keyDown('space')
    time.sleep(0.1)
    print("jump")
    time.sleep(0.1)
    pyautogui.keyUp('space')
    pyautogui.keyDown('down')


def grabbing_image():
    box = (290, 315, 410, 430)
    image = ImageGrab.grab(box)
    image.save("myimage.png")
    greyscale = ImageOps.grayscale(image)
    print(greyscale.getcolors())
    a = np.array(greyscale.getcolors())
    print(a.sum())
    return a.sum()


restart()
while True:
    if (grabbing_image()) != 13975 and (grabbing_image()) != 13833:
        jump()
        time.sleep(0.1)
    else:
        pyautogui.keyDown('down')

