# YOLOv5+SORT
## (object detection and tracking)
This is an implementation for detection and tracking objects. The goal of this project is specializing it for car tracking. By the way, you can personally define your favorite list for detection and tracking.

The code is as simple as possible to make using it easy and friendly. Only one command is needed by users. And the code is less than 75 lines.

### Step1: object detecion
YOLOv5 is the algorithm used for object detection. being fast, real-time and accurate, YOLOv5 is a good choice for object detection.
![image](https://user-images.githubusercontent.com/106428795/187042283-df9c9e66-4da6-489e-8dab-b65d0697019b.png)


    detection_and_tracking('video.mp4', [], tracking=False)

![object detection](https://user-images.githubusercontent.com/106428795/187042998-530f641e-aa91-4018-94c5-42d0537c3b7d.jpg)


![object detection2](https://user-images.githubusercontent.com/106428795/187043394-bd561651-10a1-42d1-b7de-458373bad3b7.jpg)


### Step2: favorite list
It is possible to define your favorite objects for both detection and tracking. It is very simple, by just writing them in the list in the input of the function.

### Step3: tracking
