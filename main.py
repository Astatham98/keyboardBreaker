from KeyboardBreaker import KeyboardBreaker
from CNNPredict import CNN

class Game:
    def __init__(self):
        self.kb = KeyboardBreaker()
        self.CNN = CNN()

    def start(self):
        while not self.kb.EndGame():

            if self.isCombo():
                letter = self.CNN.predict(combo=True)
                while self.isCombo():
                    self.kb.press_button(letter)
            else:
                #letter = self.kb.get_letter(coords=None
                letter = self.CNN.predict()
                if letter is not None and len(letter) > 0:
                    self.kb.press_button(letter)
    
    def isCombo(self):
        return self.kb.combo()

if __name__ == '__main__':
    game = Game()
    game.start()