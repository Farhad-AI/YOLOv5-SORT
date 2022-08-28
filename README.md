# YOLOv5+SORT
## (object detection and tracking)
This is an implementation for detection and tracking objects. The goal of this project is specializing it for car tracking. By the way, you can personally define your favorite list for detection and tracking.

The code is as simple as possible to make using it easy and friendly. Only one command is needed by users. The code is less than 75 lines.

### Step1: object detecion
Object detection was done by YOLOv5. it is fast, real-time and accurate.
![image](https://user-images.githubusercontent.com/106428795/187042283-df9c9e66-4da6-489e-8dab-b65d0697019b.png)


        detection_and_tracking('video.mp4', [], tracking=False)

![object detection](https://user-images.githubusercontent.com/106428795/187042998-530f641e-aa91-4018-94c5-42d0537c3b7d.jpg)


![object detection2](https://user-images.githubusercontent.com/106428795/187043394-bd561651-10a1-42d1-b7de-458373bad3b7.jpg)


### Step2: favorite list
It is possible to define your favorite objects for both detection and tracking. It is very simple, by just writing them in the list in the input of the function.

        ------> only cars:
        detection_and_tracking('video.mp4', ['car'], tracking=False)
        
![cars](https://user-images.githubusercontent.com/106428795/187044192-04a2d653-c6de-4642-b5d9-9fae5554351c.jpg)

        ------> person and traffic light
        detection_and_tracking('cars3.mp4', ['person', 'traffic light'], tracking=False)
![person-traffic light](https://user-images.githubusercontent.com/106428795/187044258-9cdd6f06-5e4a-4295-a766-25247db05342.jpg)

### Step3: tracking
Object tracking was done by SORT(Simple online and realtime tracking). It would be enable by setting the tracking 'True'. By default it is False wich means tracking is not enable.

        detection_and_tracking('video.mp4', ['car'], tracking=True)
        
![tracking1](https://user-images.githubusercontent.com/106428795/187045821-d2fcf5d6-fb59-4bcf-be7a-f7070bceecb1.jpg)


![tracking2](https://user-images.githubusercontent.com/106428795/187045835-becabe32-442f-434f-ba0e-4002dd82e650.jpg)

### Detection - Tracking
