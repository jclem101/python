from PIL import Image
import os, numpy

#assigns every pic in a directory with a profile, consisting of user defined width pixel signature. ie. pixel signature composed of list of pixels from every other width length in image if represented linearlly. Sigs are compared within a range (+- threshold value), if within the set range 

#list of image files, each index corresponds to index in sig object list.
imagelist = []

#list of sig objects
siglist = []

#get directory
print 'directory:'
directory = raw_input()
#get width
print 'width(lower->more exact matches):'
width = int(raw_input())

#set pixel threshold, for interpixel comparisons.
#smaller thresholds == more exact detection of duplicates
print 'pixel threshold(lower->more exact matches):'
pixthreshold  = int(raw_input())

#set image threshold for comparison of number of pixels inside match threshold. 
print 'image threshold(lower->more exact matches)'
imgthreshold  = int(raw_input())


class Sig:
	pixlist = []
	thisimgfile = ''
	thisimg = ''
	global directory
	def __init__(self, imagefile):
		global directory
		self.thisimgfile = imagefile
		#imagefile is a string
		if not directory.endswith('/'):
			directory = directory + '/'
		self.thisimg = Image.open(directory + imagefile)
		#list of pixels for sig
		self.pixlist = getpixlist(self.thisimg, self.thisimg.load())

def getpixlist(imageobj, pixelmap):
	global width
	pixlist = []
	for i in range(0, imageobj.size[0],width):
		for j in range(0, imageobj.size[1],width):
			pixlist.append(pixelmap[i,j])
	return pixlist

def cmppix(target, current):
	#compares pixel tuple, if difference between all three elements is above the threshold this means that 
	#threshold is limit for pixel to be considered dissimilar. if doesnt exceed threshold pixel is held to be similar.
	global pixthreshold
	if (abs(target[0 ] - current[0] ) < pixthreshold) and (abs(target[1] - current[1] ) < pixthreshold) and (abs(target[2] - current[2] ) < pixthreshold):
		return 1
	else:
		return 0

def cmpimg(target, current):
	#compares 2 sig objects, representing 2 images
 	#two images not necessarily of same dimensions
	#must evenly distribute comparisons from target to current
	#find scale of img target and current, use as scaling factor 
	#for now skipping comparison if image is different dimensions ie, lengths of pixlist not equal
	total = 0
	for i in range(0, len(target.pixlist)):
		total = cmppix(target.pixlist[i], current.pixlist[i]) + total
	return total	


def killdupes():
	global directory
	for target in siglist:
		for curr in siglist:
			if target == curr:
				continue
			if target.thisimg.size[:] != curr.thisimg.size[:]:
				continue
			elif cmpimg(target, curr) > imgthreshold:
				print 'removed ' + target.thisimgfile
				os.remove(directory + target.thisimgfile)
				siglist.remove(target)
					


#populate image file list
imagelist = os.walk(directory).next()[2]
#remove all non image files
for i in imagelist:
	if not i.lower().endswith('.jpg') and not i.lower().endswith('.png'):
		imagelist.remove(i)
for i in imagelist:
	siglist.append(Sig(i))
killdupes()
