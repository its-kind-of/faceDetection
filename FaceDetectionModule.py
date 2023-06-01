import cv2
import mediapipe as mp
import time


class FaceDetector:
    def __init__(self, minDetectionCone=0.5):
        self.minDetectionCon = minDetectionCone

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)

    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        #print(results)
        bboxes = []

        if self.results.detections:
            for id, detection in enumerate(self.results.detections):
                #mpDraw.draw_detection(img, detection)
                # image height, width and channels
                ih, iw, ic = img.shape
                bboxC = detection.location_data.relative_bounding_box
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

                bboxes.append([id, bbox, detection.score])
                #cv2.rectangle(img, bbox, (255, 0, 255), 2)
                if draw:
                    img = self.fancyDraw(img, bbox)
                    cv2.putText(img, f"{int(detection.score[0]*100)}%", (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

        return img, bboxes

    def fancyDraw(self, img, bbox, l=30, t=10, rt=1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h
        cv2.rectangle(img, bbox, (255, 0, 255), rt)
        # Top Left x, y
        cv2.line(img, (x, y), (x+l, y), (255, 0, 255), t)
        cv2.line(img, (x, y), (x, y+l), (255, 0, 255), t)

        # Top Right x1, y
        cv2.line(img, (x1, y), (x1 - l, y), (255, 0, 255), t)
        cv2.line(img, (x1, y), (x1, y + l), (255, 0, 255), t)

        # Bottom Left x1, y1
        cv2.line(img, (x, y1), (x + l, y1), (255, 0, 255), t)
        cv2.line(img, (x, y1), (x, y1 - l), (255, 0, 255), t)

        # Bottom Right x, y1
        cv2.line(img, (x1, y1), (x1 - l, y1), (255, 0, 255), t)
        cv2.line(img, (x1, y1), (x1, y1 - l), (255, 0, 255), t)

        return img

def main():
    # cap = cv2.VideoCapture(r"D:\open-cv\videos\pexels-tima-miroshnichenko-5752365.mp4")
    cap = cv2.VideoCapture(0)
    pTime = 0
    cTime = 0
    detector = FaceDetector()

    while True:
        success, img = cap.read()
        img, bboxs = detector.findFaces(img, False)
        print(bboxs)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f"FPS: {int(fps)}", (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 8), 2)
        cv2.imshow("Image", img)

        cv2.waitKey(40)


if __name__=="__main__":
    main()