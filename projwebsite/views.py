from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
import cv2
import os
path = os.getcwd()
import dlib
print(path)
save_path = os.path.join(path,"Sample")

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        passwd1 = request.POST['passwd1']
        passwd2 = request.POST['passwd2']
        
        user = User.objects,create_user(fname=fname, lname=lname, email=email, passwd=passwd1)
        user.save()
        print("User created!")
        return redirect('/')

    else:
        return render(request, 'register.html')


def getid():
    m_path = os.path.join(os.getcwd(),"Sample")
    file = open("id.txt","r")
    fid = file.read()
    file.close()
    file = open("id.txt","w")
    file.write(str(int(fid)+1))
    file.close()
    return int(fid)

def addFace():
    U_id = getid()
    os.mkdir(save_path + "/"+str(U_id))
    reco = dlib.get_frontal_face_detector()
    cap = cv2.VideoCapture(0)
    cnt=0
    while True:
        frame , img = cap.read()
        img = cv2.flip(img,1)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = reco(img)
        for face in faces:
            x = face.left()
            y = face.top()
            w = face.right() 
            h = face.bottom()
        
            cv2.rectangle(img,(x,y),(w,h),(255,255,0),2)
            cv2.putText(img,"Total sample taken = "+str(cnt),(x,y-10),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
            c_face = gray[y:h,x:w]
            if frame:
                c_face = cv2.resize(c_face,(200,200))
                cv2.imwrite(save_path + "/" + str(U_id) + "/" + str(cnt) + ".png",c_face)
                cnt+=1
        
        cv2.imshow("img",img)  
        k = cv2.waitKey(30)
        if k==27 or cnt>=100:
            break
    cap.release()
    cv2.destroyAllWindows()        

