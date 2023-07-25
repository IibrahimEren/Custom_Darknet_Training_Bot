# Camera Frame Collector and Label Generator

This Python script collects frames from a camera URL and saves them as JPEG files. Additionally, it generates label files containing object coordinates for each saved frame. The captured frames and their corresponding labels can be used for training object detection models.



https://github.com/IibrahimEren/Custom_Darknet_Training_Bot/assets/87008174/571a5e77-d445-4670-95c6-d4b12e657fa5



## Requirements

- Python 3.x
- OpenCV (cv2) library
- NumPy library
- Requests library

Install the required libraries using pip:

```bash
pip install opencv-python numpy requests
```

## How to Use

1. Replace `-ID-` in the `url` variable with the camera's IP address or the URL where the camera is streaming the images.

2. Run the script:

```bash
python camera_frame_collector.py
```

3. The script will capture frames from the camera stream and save them as JPEG images in the `spot_data/spot_images/` directory.

4. For each saved frame, a corresponding label file will be created in the `spot_data/spot_labels/` directory. The label file will contain the object coordinates in the format: `0 center_x center_y width height`.

5. The file paths of the captured frames will be appended to the `spot_training.txt` file. This file can be used as a list of training data for an object detection model.

6. Press the 'Esc' key to stop the script and exit the image capture.

## Notes

- The captured frames are resized to 640x480 pixels before saving.
- The script uses the Requests library to fetch the camera stream.

## Important Information

- Make sure to have permission to access the camera URL or IP address.
- The script assumes that the camera stream provides JPEG images.
- The script assumes that the camera feed captures only one object at a time. It is designed for scenarios where the camera is focused on a single object or the region of interest within the frame.
-The captured frames are resized to 640x480 pixels before saving.
-The script uses the Requests library to fetch the camera stream.
