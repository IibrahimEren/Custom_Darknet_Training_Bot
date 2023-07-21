import cv2
import numpy as np
import requests

url = "http://-ID-/shot.jpg"
# count value for image and labels names frame{count}.jpg
count = 0
while True:
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)
    frame = cv2.resize(img, (640, 480))

    frame_width = frame.shape[1]
    frame_height = frame.shape[0]
    # algılanan nesnenin ortası > objektifte tek nesne olacağına göre algılanan
    # nesnemizin ortası pencerenin ortası olucak
    Frame_midX = frame_width/2
    Frame_midY = frame_height/2
    # kameramızın içerisinde sadece objeyi almayı planladığımız için kutu yükseklik ve
    # genişlik değerlerini frame ile aynı verebiliriz
    box_width = frame_width
    box_height = frame_height

##### Collect captured frames in the images\\ path with a number #####
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    name = "frame%d.jpg" % count
    cv2.imwrite(f"spot_data\\spot_images\\{name}", frame)  # save frame as JPEG file
    count += 1
    file = f"spot_data\\spot_images\\{name}"
#########################################################################

##### write object coordinats as labels #####
    path = open(f"spot_data\\spot_labels\\{name}.txt", "w")
    path.write("0 " + str("%.6f" % (Frame_midX / frame_width)) + " " + str("%.6f" % (Frame_midY / frame_height)) + " " + str(
        "%.6f" % (box_width / frame_width)) + " " + str("%.6f" % (box_height / frame_height)))
    path.close()
########################################################################

#### Add frames path to training file ####
    path = open("spot_training.txt", "a")
    path.write(f"{file}\n")
    cv2.imshow("Android Camera", frame)
#############################################

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
