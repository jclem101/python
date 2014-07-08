import urllib, urllib2, os, sys, time

#recursively finds deepest directory of filesystem. head recursion used

max = 0 #current max value for any directory
maxurl = '' #current string url for deepest directory

def recurse(currdir, currval):
	#print currdir

	global max,maxurl
	#if currval is greater than global max 
	if currval > max:
		max = currval
		maxurl = currdir
	#get list of all subdirectories
	dirlist = os.walk(currdir).next()[1]
	
	#if no subdirectories then return
	if len(dirlist) == 0:
		return
	#recurse with currval+=1 for all children in list
	for dir in dirlist:
		recurse(currdir+'\\'+dir, currval+1)
	
	
#get start directory
print 'Please enter starting directory.'
#startdirectory = raw_input()
startdirectory = 'C:\Users\j\Desktop\changeAlert\dir'
#call recurse with startdirectory, 0 as arguments
recurse(startdirectory, 0)
print max
print maxurl
