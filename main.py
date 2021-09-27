from KeyboardBreaker import KeyboardBreaker
import keyboard
from time import sleep

class Game:
    def __init__(self):
        self.kb = KeyboardBreaker()
        self.current_letter = None
        self.finished = False

    def start(self):
        while not self.finished:
            if keyboard.is_pressed('a') == True:
                self.finished = True
                print(self.finished)

            if self.isCombo():
                letter = self.kb.get_combo_letter()
                while self.isCombo():
                    if letter is not None:
                        self.kb.press_button(letter)
                    else:
                        letter = self.kb.get_combo_letter()
            else:
                letter = self.kb.get_letter(coords=None)
                if letter is not None and len(letter) > 0:
                    self.kb.press_button(letter)
    
    def isCombo(self):
        return self.kb.combo()

if __name__ == '__main__':
    game = Game()
    game.start()