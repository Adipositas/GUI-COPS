import numpy as np
import cv2,os,sys,datetime,time

global recordingstop
recordingstop = False

myp = os.path.dirname(sys.argv[0]) +os.sep

setp = 10
print(myp)

def stop():
	#kald denne fra GUI for at stoppe
	recordingstop = True

def controlrec(topath,setp):
	#Kald denne fra gui for at starte
	cap = cv2.VideoCapture(0)
	while 1:
		done = recordoncap(topath,setp,cap)
		if done: break
	
	
def recordoncap(topath,setp,cap):
	h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
	w =  int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
	start_time = time.time()
	# video recorder
	fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
	video_writer = cv2.VideoWriter(myp + str(int(start_time))+".avi", fourcc, 20, (w, h))
	timess = datetime.datetime.now()
	
	 # record video
	while True:
		ret, frame = cap.read()
		times = datetime.datetime.now()
		timeagain = times + datetime.timedelta(microseconds=50000)
		
		if ret==True:		
			video_writer.write(frame)
		while 1: #FPS control
			if (timeagain-datetime.datetime.now()).days < 0: break
			
		timepassed = time.time() - start_time
		
		if timepassed >setp: break		#recording break
		if recordingstop: break
		
		
	timeo = datetime.datetime.now()
	video_writer.release()
	
	if recordingstop:
		donevar = True
	else:
		donevar = False
	
	return donevar
	
	
	

def recordvideo(topath,setp):
	#Topath: recording location. setp: recording length in seconds.

	cap = cv2.VideoCapture(0)

	#ARGH! FATTER IKKE HVORFOR DET HER FAAR DET TIL AT FUNGERER. Den gad ikke gemme video naar man satte w og h i writer manuelt...
	h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
	w =  int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
	
	start_time = time.time()
	
	# video recorder
	# fourcc = cv2.cv.CV_FOURCC(*'XVID')  # cv2.VideoWriter_fourcc() does not exist
	fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
	
	#Der er maaet galt med FPS
	video_writer = cv2.VideoWriter(myp + str(int(start_time))+".avi", fourcc, 20, (w, h))
	# times = datetime.datetime.now()
	timess = datetime.datetime.now()
	
	 # record video
	while(cap.isOpened()):
		
		ret, frame = cap.read()
		times = datetime.datetime.now()
		timeagain = times + datetime.timedelta(microseconds=50000)
		if ret==True:		
			video_writer.write(frame)
			
		while 1:
			if (timeagain-datetime.datetime.now()).days < 0: break

		timepassed = time.time() - start_time
		# print("%f seconds" % (timepassed))
		
		if timepassed >setp: break

		
	timeo = datetime.datetime.now()
	
	print(timeo-timess)
	cap.release()
	video_writer.release()
	cv2.destroyAllWindows()
	
	
	
controlrec(myp,setp)