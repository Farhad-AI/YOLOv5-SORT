import torch
import cv2
from sort import Sort
import numpy as np


def show_objects(image, places, colors):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    x1 = places[:, 0]
    y1 = places[:, 1]
    x2 = places[:, 2]
    y2 = places[:, 3]
    for i in range(places.shape[0]):
        if places.shape[1] == 7:
            ID = int(places[i, -2])
            text = places[i, -1]
        elif places.shape[1] == 5:
            ID = int(places[i, -1])
            text = str(ID)
        cv2.rectangle(image, (int(x1[i]), int(y1[i])),
                      (int(x2[i]), int(y2[i])), colors[ID], 2)

        cv2.putText(image, text, (int(x1[i]), int(y1[i]-7)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[ID], 2)
    cv2.imshow('frame', image)


def favorite_objects(objects, favourite_list=[]):
    new_objects = objects.copy()
    if len(favourite_list) == 0:
        pass
    else:
        for i in range(objects.shape[0]):
            if objects.iloc[i][-1] in favourite_list:
                continue
            else:
                new_objects = new_objects.drop(index=i)
    return new_objects


def detection_and_tracking(fileName, favourite_list, tracking=False):
    colors = np.random.uniform(0, 255, size=(10000, 3))
    model = torch.hub.load('ultralytics/yolov5', 'yolov5m', pretrained=True).eval()
    tracker = Sort()
    cap = cv2.VideoCapture(fileName)
    while True:
        ret, frame = cap.read()
        if ret is False:
            break

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        with torch.no_grad():
            results = model(frame)
        objects = results.pandas().xyxy[0]
        new_objects = favorite_objects(objects, favourite_list)

        if tracking is False:
            new_objects = new_objects.to_numpy()
            show_objects(frame, new_objects, colors)

        elif tracking is True:
            new_objects = new_objects.drop(labels='name', axis=1)
            new_objects = new_objects.to_numpy()
            track_bbs_ids = tracker.update(new_objects)
            show_objects(frame, track_bbs_ids, colors)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    detection_and_tracking('video.mp4', ['car'], tracking=True)
