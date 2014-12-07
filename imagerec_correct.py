from PIL import Image
import numpy as np
import matplotlib.pyplot as plt 
import time
from collections import Counter

'''
Each row appears as:
[[  0   0   0 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]
 [255 255 255 255]]
 each line is a pixel
 item 0 = red
 item 1 = green
 item 2 = blue
 item 3 = alpha (transparency)
'''

def createExamples():
	numberArrayExamples = open('numArrayExamples.txt','a')
	numbersWeHave = range(0,10) # 0-9
	versionsWeHave = range(1,10) # 1-9

	for eachNum in numbersWeHave:
		for eachVer in versionsWeHave:
			# print str(eachNum)+'.'+str(eachVer)
			imageFilePath = 'images/numbers/' + str(eachNum) +'.' + str(eachVer)+'.png'
			ei = Image.open(imageFilePath)
			eiar = np.array(ei)
			eiar1 = str(eiar.tolist())

			lineToWrite = str(eachNum)+'::'+eiar1+'\n'
			numberArrayExamples.write(lineToWrite)


def threshold(imageArray):
	# blurring function would assign percentages to adjacent pixels (0,25,50,100%)
	# make every pixel black or white
	balanceArray = []
	newArray = imageArray

	# part is a row
	for eachRow in imageArray:
		for eachPixel in eachRow:
			avgNum = reduce(lambda x, y: x + y, eachPixel[:3])/len(eachPixel[:3])
			balanceArray.append(avgNum)

	balance = reduce(lambda x, y: x + y, balanceArray)/len(balanceArray)

	for eachRow in newArray:
		for eachPixel in eachRow:
			if reduce(lambda x, y: x + y, eachPixel[:3])/len(eachPixel[:3]) > balance:
				eachPixel[0] = 255
				eachPixel[1] = 255
				eachPixel[2] = 255
				eachPixel[3] = 255

			else:
				eachPixel[0] = 0
				eachPixel[1] = 0
				eachPixel[2] = 0
				eachPixel[3] = 255

	return newArray

def whatNumIsThis(filePath):
	# this is a very basic example - doesn't use blurring/smoothing or any other logic to find similar images
	matchedArray = []
	loadExamples = open('numArrayExamples.txt', 'r').read()
	loadExamples = loadExamples.split('\n')

	i = Image.open(filePath)
	iar = np.array(i) # need two versions for analysis
	iarl = iar.tolist()

	inQuestion = str(iarl)

	for eachExample in loadExamples:
		if len(eachExample) > 3: # make sure it's a proper line
			splitEx = eachExample.split('::')
			currentNum = splitEx[0]
			currentArray = splitEx[1]

			eachPixelExample = currentArray.split('],')

			eachPixelInQuestion = inQuestion.split('],')

			x = 0

			while x < len(eachPixelExample):
				if eachPixelExample[x] == eachPixelInQuestion[x]:
					matchedArray.append(int(currentNum))

				x += 1

	print matchedArray
	x = Counter(matchedArray)
	print x 


	graphX = []
	graphY = []

	for eachThing in x:
		print eachThing
		graphX.append(eachThing)
		print x[eachThing]
		graphY.append(x[eachThing])

	fig = plt.figure()
	ax1 = plt.subplot2grid((4,4),(0,0), rowspan=1, colspan=4)
	ax2 = plt.subplot2grid((4,4),(1,0), rowspan=3, colspan=4)

	ax1.imshow(iar)

	ax2.bar(graphX, graphY, align='center')

	plt.ylim(300) # if less than 400 similar, then it's a mistake

	xloc = plt.MaxNLocator(12) # cover for -1

	ax2.xaxis.set_major_locator(xloc)

	plt.show()
'''
i = Image.open('images/numbers/0.1.png')
iar = np.array(i)

i2 = Image.open('images/numbers/y0.4.png')
iar2 = np.array(i2)

i3 = Image.open('images/numbers/y0.5.png')
iar3 = np.array(i3)

i4 = Image.open('images/sentdex.png')
iar4 = np.array(i4)
'''

# createExamples() #creates file database

whatNumIsThis('images/test2.png')
