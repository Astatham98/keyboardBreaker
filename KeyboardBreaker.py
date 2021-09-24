import cv2
from mss.darwin import MSS as mss
import numpy as np

class KeyboardBreaker:
    def __init__(self) -> None:
        self.SCT = mss()
        self.dims = {
            'left': 650,
            'top': 190,
            'width': 250,
            'height': 50
        }
    
    def getScreenshot(self):
        scr = self.SCT.grab(self.dims)
        img = np.array(scr)
        cv2.imshow('image', img)
        cv2.waitKey()