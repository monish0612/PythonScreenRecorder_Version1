import datetime

from PIL import ImageGrab
import numpy as np
import cv2
import pyautogui
import os

def recorder():
    os.startfile("D:\Programs\python\ScreenRecorder")
    screeng=pyautogui.screenshot()
    screeng.save("image.png")
    resolution = screeng.size
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    print(timestamp)
    filename = f"{timestamp}.avi"
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    capture_video = cv2.VideoWriter(filename, fourcc, 20.0, resolution)

    while True:
        # img = ImageGrab.grab(bbox=(0, 0, 1920, 1200))
        img = pyautogui.screenshot()
        img_np = np.array(img)
        img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
        cv2.imshow('Capture', img_final)
        capture_video.write(img_final)

        if cv2.waitKey(10) == ord('q'):
            break

    capture_video.release()
    cv2.destroyAllWindows()




recorder()