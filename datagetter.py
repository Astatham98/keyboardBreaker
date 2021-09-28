from re import S
from KeyboardBreaker import KeyboardBreaker
import pytesseract
from time import sleep
import cv2
import os

class Data:
    def __init__(self):
        self.kb = KeyboardBreaker()
        self.counter = 0

    def loop(self):
        while True:
            if not self.kb.EndGame():
                if self.kb.combo():
                    letter = self.getComboLetter()
                    self.kb.press_button(letter)
                else:
                    letter = self.save_letter_image() 
                    self.kb.press_button(letter)
            else:
                self.kb.press_button('space')
                sleep(1)
    
    def save_letter_image(self, coords=None):
        if coords is None:
            pt1, pt2 = self.kb.findBlue()
        else:
            pt1, pt2 = coords
        
        if pt1 is not None and pt2 is not None:
            dims = {
                'left': self.kb.dims['left'] + pt1[0],
                'top': self.kb.dims['top'] + pt1[1],
                'width': 30,
                'height': 30
            }

            img = self.kb.getScreenshot(dims=dims)    
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            text = pytesseract.image_to_string(gray, config='-l eng --oem 3 --psm 10')
            char = ''
            for t in text:
                if t.isalpha() and t.isupper():
                    char = t
                    break
            
            name = 'unknown'
            if char == '':
                name += str(self.counter) + '.jpg'
                self.counter += 1
            else:
                name = char + str(self.counter) + '.jpg' 
                self.counter += 1
            
            path = os.getcwd() + '/output/' + char if char != '' else os.getcwd() + '/output/' + 'unknown'
            if not os.path.exists(path):
                os.makedirs(path)

            cv2.imwrite(os.path.join(path, name), gray)
            return char
        return ''
    
    def getComboLetter(self):
        coords = self.kb.findBlue() if self.kb.findBlue() else self.findLBlue()
        return self.save_letter_image(coords = coords)


Data().loop()