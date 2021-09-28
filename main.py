from KeyboardBreaker import KeyboardBreaker

class Game:
    def __init__(self):
        self.kb = KeyboardBreaker()

    def start(self):
        while not self.kb.EndGame():

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