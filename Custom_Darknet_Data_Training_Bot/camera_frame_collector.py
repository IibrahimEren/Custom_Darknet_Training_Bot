import cv2
import numpy as np
import requests

"""
This code collects frames from a camera and saves them as JPEG files.
The object coordinates are also saved as labels to a file.
"""

url = "http://-ID-/shot.jpg"

# count value for image and labels names frame{count}.jpg
count = 0

while True:

    # Get the image from the camera
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    # Resize the image to 640x480 pixels
    frame = cv2.resize(img, (640, 480))

    # Calculate the width and height of the frame
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    # Calculate the center of the frame
    Frame_midX = frame_width / 2
    Frame_midY = frame_height / 2

    # Calculate the width and height of the bounding box
    box_width = frame_width
    box_height = frame_height

    # Save the frame as a JPEG file
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    name = f"frame{count:03d}.jpg"
    with open(f"spot_data\\spot_images\\{name}", "wb") as f:
        f.write(img_arr)
    count += 1
    file = f"spot_data\\spot_images\\{name}"

    # Write the object coordinates as labels to a file
    with open(f"spot_data\\spot_labels\\{name}.txt", "w") as f:
        f.write(f"0 {Frame_midX / frame_width:.6f} {Frame_midY / frame_height:.6f} {box_width / frame_width:.6f} {box_height / frame_height:.6f}")

    # Add the file path to the training file
    with open("spot_training.txt", "a") as f:
        f.write(f"{file}\n")

    # Display the frame
    cv2.imshow("Android Camera", frame)

    # Check if the user pressed `Esc`
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
