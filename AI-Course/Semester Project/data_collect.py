import uuid
import os
import time
import cv2

PATH = os.path.join(os.getcwd(),'data','images')#.replace("\\","/") # /data/images
labels = ['happy','sad']
num_imgs = 10

cap = cv2.VideoCapture(1)


for label in labels:
    print("Image for {}".format(label))
    time.sleep(1)

    for img_num in range(num_imgs):
        print("Image {} of {}".format(img_num+1,num_imgs))
        ret, frame = cap.read()
        if ret:
            img_name = os.path.join(PATH,label,str(uuid.uuid1())+'.jpg')#.replace("\\","/")
            print(cv2.imwrite(img_name,frame))
            cv2.imshow(label,frame)
            print("Image saved at {}".format(img_name))
            time.sleep(1)
        else:
            print("Error capturing image")
            break
        
        
        if cv2.waitKey(1) == ord('q'):
                cap.release()
                cv2.destroyAllWindows()
                break

    cv2.destroyAllWindows()
    print ("\n\n GOING FOR NEXT LABEL \n\n")

