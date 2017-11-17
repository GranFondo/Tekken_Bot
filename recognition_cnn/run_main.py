import tensorflow as tf
import numpy as np
from PIL import ImageGrab
import win32gui
import cv2
import time

rect = [7, 32, -5, -7]

def screen_record(): 
    last_time = time.time()
    hwnd = win32gui.FindWindow(None, r'TEKKEN 7 ')
    win32gui.SetForegroundWindow(hwnd)
    dimensions = win32gui.GetWindowRect(hwnd)
    print(dimensions)
    dimensions = np.array(list(dimensions))+rect
    print(dimensions)
    while(True):
        # 800x600 windowed mode for GTA 5, at the top left position of your main screen.
        # 40 px accounts for title bar. 
        printscreen =  np.array(ImageGrab.grab(bbox=tuple(dimensions)))
        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

screen_record()