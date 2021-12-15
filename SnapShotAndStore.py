import dropbox
import cv2
import time
import random

startTime=time.time()

def take_snapShot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0) # 0 is code for webcam
    result=True

    while(result):
        ret,frame=videoCaptureObject.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        startTime=time.time()
        result=False
    return img_name
    print("SnapShot Taken.!")
    videoCaptureObject.release()
    cv2.destroyAllWindows()

def uploadFile(img_name):
    access_token="WMmwC3QxvzIAAAAAAAAAAbEQJxqFCABpbIEsHJ9m00fTvoJsvJFLgGHwYt-AmHyW"
    file=img_name
    file_from=file
    file_to="/newFolder/"+(img_name)
    dbx=dropbox.Dropbox(access_token)

    with open(file_from,"rb") as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("Files Uploaded")

def main():
    while(True):
        if((time.time()-startTime)>= 5):
            name=take_snapShot()
            uploadFile(name)

main()
 