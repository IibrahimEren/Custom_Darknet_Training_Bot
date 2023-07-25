import cv2
import numpy as np
import requests

"""
This code collects frames from a camera and saves them as JPEG files.
The object coordinates are also saved as labels to a file.
"""

# The URL of the camera
url = "http://-ID-//shot.jpg"

# Count value for image and labels names
count = 0

while True:

    # Get the image from the camera
    img_resp = requests.get(url)
    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    img = cv2.imdecode(img_arr, cv2.IMREAD_COLOR)

    # Resize the image to 640x480 pixels
    frame = cv2.resize(img, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR_EXACT)
    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)

    # Calculate the width and height of the frame
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    # Calculate the center of the frame
    Frame_midX = frame_width / 2
    Frame_midY = frame_height / 2

    # Calculate the width and height of the bounding box
    box_width_start = frame_width - (frame_width - 20)
    box_height_start = frame_height - (frame_height - 20)
    box_width_end = frame_width - 20
    box_height_end = frame_height - 20
    box_width_length = box_width_end - box_width_start
    box_height_length = box_height_end - box_height_start

    # Draw the bounding box and center line on the frame
    cv2.rectangle(frame, (box_width_start, box_height_start), (box_width_end, box_height_end), (200, 200, 10), 2)
    cv2.line(frame, (int(Frame_midX), box_height_start), (int(Frame_midX), box_height_end), (10, 200, 200), 1)
    cv2.line(frame, (box_width_start, int(Frame_midY)), (box_width_end, int(Frame_midY)), (10, 200, 200), 1)

    # Save the frame as a JPEG file
    name = f"frame{count:03d}.jpg"
    with open(f"spot_data\\spot_images\\{name}", "wb") as f:
        f.write(img_arr)
    count += 1
    file = f"spot_data\\spot_images\\{name}"

    # Write the object coordinates as labels to a file
    with open(f"spot_data\\spot_labels\\{name}.txt", "w") as f:
        f.write(f"0 {Frame_midX / frame_width:.6f} {Frame_midY / frame_height:.6f} {box_width_length / frame_width:.6f} {box_height_length / frame_height:.6f}")

    # Add the file path to the training file
    with open("spot_training.txt", "a") as f:
        f.write(f"{file}\n")

    # Display the frame
    cv2.imshow("Android Camera", frame)

    # Check if the user pressed `Esc`
    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
