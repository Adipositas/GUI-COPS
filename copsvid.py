import numpy as np
import cv2,os,sys,datetime,time
global recordingstop
recordingstop = False

myp = os.path.dirname(sys.argv[0]) +os.sep

setp = 10
print(myp)

def stop():
	#kald denne fra GUI for at stoppe
	print("Stopping video recording")
	global recordingstop
	recordingstop = True
	#Collect coordinates calculate COPS and provide score
	
	
def controlrec(topath,setp):
	#Kald denne fra gui for at starte
	global recordingstop
	cap = cv2.VideoCapture(0)
	print(cap)
	while 1:
		done = recordoncap(topath,setp,cap)
		if done: break
		
	print("Done is done")
	cap.release()
	recordingstop = False
	
def recordoncap(topath,setp,cap):
	#Topath: recording location. setp: recording length in seconds.
	# h = int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
	# w =  int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
	global recordingstop
	#cv3
	h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
	w =  int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
	start_time = time.time()
	# video recorder
	# cv2
	# fourcc = cv2.cv.CV_FOURCC('m', 'p', '4', 'v')
	# cv3
	fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
	# fourcc = cv2.VideoWriter_fourcc(*'XVID') 
	# fourcc = cv2.VideoWriter_fourcc('d', 'i', 'v', 'x')
	video_writer = cv2.VideoWriter(topath + str(int(start_time))+".avi", fourcc, 20, (w, h))
	timess = datetime.datetime.now()
	print("recording")
	 # record video
	while True:
		ret, frame = cap.read()
		# print(ret)
		times = datetime.datetime.now()
		timeagain = times + datetime.timedelta(microseconds=50000)
		
		if ret==True:		
			video_writer.write(frame)
		while 1: #FPS control
			if (timeagain-datetime.datetime.now()).days < 0: break
			
		timepassed = time.time() - start_time

		if timepassed >setp: 
			#Start tracking on video  
			break		#recording break
		if recordingstop: break		
		
	timeo = datetime.datetime.now()
	video_writer.release()
	
	
	if recordingstop: donevar = True
	# else:
		# donevar = False
	
	return donevar
	
	
	


#Temporary folder
# temp_path = myp + "temp" + os.sep	
	
# topath = temp_path + "video" +os.sep
# print(topath)
# setp = 60
		
# controlrec(topath,setp)
# controlrec(myp,setp)