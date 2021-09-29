# keyboardBreaker
## Overview
KeyboardBreaker is a computr vision project made to automatically play the game [keyboard breaker](https://www.addictinggames.com/funny/keyboard-breaker#url). 

The project orignally ran by detecting the colour blue, grabbing the area of the letter, converting it to grayscale and then parsing it through [pytesseract](https://pypi.org/project/pytesseract/). However, this was very ineffcient and ended up barely being able to beat the easiest difficulty. Therefore the project pivoted to using a simple neural netowrk. Therefore, [tensorflow](https://www.tensorflow.org/) is required for this project.

## Setup
There are a few steps to setting this up to work on your machine.

* First install requirements.txt
* Install pytesseract: [windows](https://medium.com/@marioruizgonzalez.mx/how-install-tesseract-orc-and-pytesseract-on-windows-68f011ad8b9b), [mac](https://guides.library.illinois.edu/c.php?g=347520&p=4121425)
* You may need to change the [MSS version](https://python-mss.readthedocs.io/api.html) in KeyboardBreaker to your system version.