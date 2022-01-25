import cv2
import mediapipe as mp
from game import Timer


class MediaPipeHolisticDetection:

    def __init__(self):

        # initialize our Mediapipe variables
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic

        # detected joints
        self.lelbow = [-1, -1, -1]  # visible, x coor, ycoor
        self.relbow = [-1, -1, -1]  # visible, x coor, ycoor
        self.lhand = [-1, -1, -1]  # visible, x coor, ycoor
        self.rhand = [-1, -1, -1]  # visible, x coor, ycoor
        self.lhip = [-1, -1, -1]  # visible, x coor, ycoor
        self.rhip = [-1, -1, -1]  # visible, x coor, ycoor
        self.lshoulder = [-1, -1, -1]  # visible, x coor, ycoor
        self.rshoulder = [-1, -1, -1]  # visible, x coor, ycoor
        self.ltoe = [-1, -1, -1]  # visible, x coor, ycoor
        self.rtoe = [-1, -1, -1]  # visible, x coor, ycoor
        self.lheel = [-1, -1, -1]  # visible, x coor, ycoor
        self.rheel = [-1, -1, -1]  # visible, x coor, ycoor

    def DetectSingleImg(self, image):

        with self.mp_holistic.Holistic(
                static_image_mode=True,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.5
        ) as holistic:

            image = cv2.resize(image, (854, 480))
            image.flags.writeable = False
            image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
            results = holistic.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
            self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS)

            # joints
            self.lelbow = [-1, -1, -1]  # visible, x coor, ycoor
            self.relbow = [-1, -1, -1]  # visible, x coor, ycoor
            self.lhand = [-1, -1, -1]  # visible, x coor, ycoor
            self.rhand = [-1, -1, -1]  # visible, x coor, ycoor
            self.lhip = [-1, -1, -1]  # visible, x coor, ycoor
            self.rhip = [-1, -1, -1]  # visible, x coor, ycoor
            self.lshoulder = [-1, -1, -1]  # visible, x coor, ycoor
            self.rshoulder = [-1, -1, -1]  # visible, x coor, ycoor
            self.lknee = [-1, -1, -1]  # visible, x coor, ycoor
            self.rknee = [-1, -1, -1]  # visible, x coor, ycoor
            self.ltoe = [-1, -1, -1]  # visible, x coor, ycoor
            self.rtoe = [-1, -1, -1]  # visible, x coor, ycoor
            self.lheel = [-1, -1, -1]  # visible, x coor, ycoor
            self.rheel = [-1, -1, -1]  # visible, x coor, ycoor
            if results.pose_landmarks:
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_SHOULDER].visibility > 0.8:
                    self.lshoulder = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_SHOULDER].x,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_SHOULDER].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_SHOULDER].visibility > 0.8:
                    self.rshoulder = [1,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_SHOULDER].x,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_SHOULDER].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_ELBOW].visibility > 0.8:
                    self.lelbow = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_ELBOW].x,
                                   results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_ELBOW].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_ELBOW].visibility > 0.8:
                    self.relbow = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_ELBOW].x,
                                   results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_ELBOW].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_WRIST].visibility > 0.8:
                    self.lhand = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_WRIST].x,
                                  results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_WRIST].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_WRIST].visibility > 0.8:
                    self.rhand = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_WRIST].x,
                                  results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_WRIST].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HIP].visibility > 0.8:
                    self.lhip = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HIP].x,
                                 results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HIP].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HIP].visibility > 0.8:
                    self.rhip = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HIP].x,
                                 results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HIP].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_KNEE].visibility > 0.8:
                    self.lknee = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_KNEE].x,
                                  results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_KNEE].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_KNEE].visibility > 0.8:
                    self.rknee = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_KNEE].x,
                                  results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_KNEE].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HEEL].visibility > 0.8:
                    self.lheel = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HEEL].x,
                                  results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HEEL].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HEEL].visibility > 0.8:
                    self.rheel = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HEEL].x,
                                  results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HEEL].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_FOOT_INDEX].visibility > 0.8:
                    self.ltoe = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_FOOT_INDEX].x,
                                 results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_FOOT_INDEX].y]
                if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX].visibility > 0.8:
                    self.rtoe = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX].x,
                                 results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX].y]

        # return the drawn-on image and detected joints
        return image, [self.lelbow, self.relbow, self.lhand, self.rhand, self.lhip, self.rhip, self.lshoulder,
                       self.rshoulder,
                       self.lknee, self.rknee, self.ltoe, self.rtoe, self.lheel, self.rheel]

    # TESTING PART :, standalone function which can be called and will draw on the image
    def StartDetection(self):
        self.cap = cv2.VideoCapture(0)

        with self.mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

            while self.cap.isOpened():
                success, image = self.cap.read()
                drawn_image, joints = MediaPipeHolisticDetection.DetectSingleImg(self, image)

                print(joints)

                cv2.imshow('MediaPipe Holistic', drawn_image)

                if cv2.waitKey(5) & 0xFF == 27:
                    break

            cv2.destroyAllWindows()


# TESTING : standalone version for mediapipe
if __name__ == "__main__":
    MHD = MediaPipeHolisticDetection()  # initialize our detection class
    MHD.StartDetection()
