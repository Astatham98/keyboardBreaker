import numpy as np
import tensorflow as tf
from tensorflow import keras
from KeyboardBreaker import KeyboardBreaker
import cv2
import numpy as np
from numpy.random import seed 
seed(24)
tf.random.set_seed(24)
class CNN:
    def __init__(self):
        self.model = keras.models.load_model('model_Nadam.h5')

    def predict(self, combo=False):
        image = self.getPhoto(combo)
        if image is not None:
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            
            img = gray.reshape(1, 30*30) / 255
            pred = self.model.predict(img)
            top = np.argmax(pred)
            letter = self.convert(top)

            print(letter)
            return letter
        else:
            self.predict()

    def convert(self, num: int) -> str:
        pred_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z', 26:',', 27:'.', 28:';'}
        return pred_dict[num]

    def getPhoto(self, combo: bool):
        kb = KeyboardBreaker()
        if not combo:
            pt1, pt2 = kb.findBlue()
        else:
            pt1, pt2 = kb.findBlue() if kb.findBlue() else kb.findLBlue()
            while pt1 is None:
                pt1, pt2 = kb.findBlue() if kb.findBlue() else kb.findLBlue()

        if pt1 is None:
            return


        dims = {
            'left': kb.dims['left'] + pt1[0],
            'top': kb.dims['top'] + pt1[1],
            'width': 30,
            'height': 30
        }

        return kb.getScreenshot(dims=dims)



