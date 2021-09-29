from KeyboardBreaker import KeyboardBreaker
from CNNPredict import CNN
import pyautogui
from time import sleep

class Game:
    def __init__(self):
        self.kb = KeyboardBreaker()
        self.CNN = CNN()
        self.first = True

    def start(self):
        while True:
            if self.first:
                print('Getting screen coordinates - this may take a few seconds')
                dims = self.getDims()
                self.CNN.setScreenDims(dims)
                self.statrtGame()
                self.first = False
            while not self.kb.EndGame():
                if self.isCombo():
                    letter = self.CNN.predict(combo=True)
                    while self.isCombo():
                        self.kb.press_button(letter)
                else:
                    letter = self.CNN.predict()
                    if letter is not None and len(letter) > 0:
                        self.kb.press_button(letter)
    
    def isCombo(self):
        return self.kb.combo()

    def getDims(self):
        r = None
        while r is None:
            r = pyautogui.locateOnScreen('mainMenu.png', confidence=0.5, grayscale=True)

        positions = ["left", "top", "width", "height"]
        dims = {}
        for i in range(len(r)):
            dims[positions[i]] =r[i]
        
        return dims
    
    def statrtGame(self):
        pyautogui.press('q')
        sleep(0.25)
        pyautogui.press('r')
        sleep(0.25)
        pyautogui.press('F')

if __name__ == '__main__':
    game = Game()
    game.start()