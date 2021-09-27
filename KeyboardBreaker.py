import cv2
from mss.darwin import MSS as mss
import numpy as np
import pytesseract
import pyautogui



class KeyboardBreaker:
    def __init__(self) -> None:
        self.SCT = mss()
        self.dims = {
            'left': 750,
            'top': 250,
            'width': 650,
            'height': 475
        }

        self.blue = np.array([31, 164, 196])
        self.blue2= np.array([179, 255, 255])
        self.lblue = np.array([0, 104, 137])
        self.lblue2 = np.array([115, 255, 255])
    
    def getScreenshot(self, dims=None):
        dimension = dims if dims is not None else self.dims
        scr = self.SCT.grab(dimension)
        img = np.array(scr)
        return img
    
    def findBlue(self):
        img  = self.getScreenshot()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, self.blue, self.blue2)
        points = cv2.findNonZero(mask)
        if points is not None:
            avg = np.mean(points, axis=0)[0]

            return [int(x-15) for x in avg], [int(avg[0])+15, int(avg[1])+15]
        return None, None

    def findLBlue(self):
        img  = self.getScreenshot()
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, self.lblue, self.lblue2)
        points = cv2.findNonZero(mask)
        if points is not None:
            avg = np.mean(points, axis=0)[0]

            return [int(x-15) for x in avg], [int(avg[0])+15, int(avg[1])+15]
        return None, None

        

    def combo(self):
        img  = self.getScreenshot()
        img2 = img[:,:,:3]
        combo = cv2.imread('combo.jpg', cv2.IMREAD_UNCHANGED)
        result = cv2.matchTemplate(img2, combo, cv2.TM_CCOEFF_NORMED)
        minv, maxv, minp, maxp = cv2.minMaxLoc(result)
        print(maxv, maxp)
        if maxv > 0.85:
            return True
        return False

    def get_letter(self):
        pt1, pt2 = self.findBlue()
        if pt1 is None:
            return

        print(pt1, pt2)

        dims = {
            'left': self.dims['left'] + pt1[0],
            'top': self.dims['top'] + pt1[1],
            'width': 30,
            'height': 30
        }

        img = self.getScreenshot(dims=dims)     
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        text = pytesseract.image_to_string(gray, config='--psm 10')
        char = ''
        for t in text:
            if t.isalpha() and t.isupper():
                char = t
                break
        

        return char

    def press_button(self, char):
        pyautogui.press(char)

        
    


keyboardBreaker = KeyboardBreaker()
keyboardBreaker.get_letter()