import numpy as np
import tensorflow as tf
from tensorflow import keras
from KeyboardBreaker import KeyboardBreaker
import cv2
import numpy as np

def predict(image):
    model = keras.models.load_model('model_Nadam.h5')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    img = gray.reshape(1, 30*30)
    pred = model.predict(img)
    top = np.argmax(pred)
    letter = convert(top)

    print(letter)
    cv2.imshow('text image', gray)
    cv2.waitKey(0)

def convert(num: int) -> str:
    pred_dict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J',10:'K',11:'L',12:'M',13:'N',14:'O',15:'P',16:'Q',17:'R',18:'S',19:'T',20:'U',21:'V',22:'W',23:'X', 24:'Y',25:'Z', 26:'colon', 27:'dot', 28:'semi'}
    return pred_dict[num]

def test():
    kb = KeyboardBreaker()
    pt1, pt2 = kb.findBlue()

    if pt1 is None:
        return

    dims = {
        'left': kb.dims['left'] + pt1[0],
        'top': kb.dims['top'] + pt1[1],
        'width': 30,
        'height': 30
    }

    return kb.getScreenshot(dims=dims)  

predict(test())