import time
import os

frameList = [
''' 
	+-----+
	 O    |
	/|\   |
	/ \   |
		 === ''' , '''

	+-----+
   \O/  |
    |   |
    \\\\  |
	  	 ===''' , '''
	
       _____
	O O
   	 .'''








]
while True:
	for frame in frameList:
		os.system("cls")
		print(frame)
		time.sleep(.3)