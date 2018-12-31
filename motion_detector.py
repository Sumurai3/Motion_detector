import cv2
video=cv2.VideoCapture(0)
first_frame=None
status_list=[None,None]
times=[]
status=0
while True:
    check , frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
        first_frame=gray
        continue

    delta_frame=cv2.absdiff(first_frame,gray)
    threshold_frame=cv2.threshold(delta_frame,40,255,cv2.THRESH_BINARY)[1]
    threshold_frame= cv2.dilate(threshold_frame,None, iterations=2)

    (_,cnts,_)=cv2.findContours(threshold_frame.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contours in cnts:
        if cv2.contourArea(contours) < 10000:
            continue
        status=1


        (x,y,w,h)=cv2.boundingRect(contours)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    status_list.append(status)
    cv2.imshow("Delta_frame",delta_frame)
    cv2.imshow("GRAY_FRAME",gray)
    cv2.imshow("threshold_frame",threshold_frame)
    cv2.imshow("COLOR_Frame",frame)
    key=cv2.waitKey(5)


    if key==ord("q"):
        break
print(status_list)
video.release()

cv2.destroyAllWindows()
