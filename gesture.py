import cv2
import mediapipe as mp
from pynput.keyboard import Key, Controller
from game import Timer


class MediaPipeHolisticDetection:

    def __init__(self):

        # initialize our Mediapipe variables
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_holistic = mp.solutions.holistic

        # detected joints
        self.lelbow = [-1, -1, -1]  # visible, x coor, ycoor
        self.lelbow_average = [0, 0, 0]  # count, x coor, ycoor
        self.relbow = [-1, -1, -1]  # visible, x coor, ycoor
        self.relbow_average = [0, 0, 0]  # count, x coor, ycoor
        self.lhand = [-1, -1, -1]  # visible, x coor, ycoor
        self.lhand_average = [0, 0, 0]  # count, x coor, ycoor
        self.rhand = [-1, -1, -1]  # visible, x coor, ycoor
        self.rhand_average = [0, 0, 0]  # count, x coor, ycoor
        self.lhip = [-1, -1, -1]  # visible, x coor, ycoor
        self.lhip_average = [0, 0, 0]  # count, x coor, ycoor
        self.rhip = [-1, -1, -1]  # visible, x coor, ycoor
        self.rhip_average = [0, 0, 0] # count, x coor, ycoor
        self.lknee = [-1, -1, -1]  # visible, x coor, ycoor
        self.lknee_average = [0, 0, 0]  # count, x coor, ycoor
        self.rknee = [-1, -1, -1]  # visible, x coor, ycoor
        self.rknee_average = [0, 0, 0]  # count, x coor, ycoor
        self.lshoulder = [-1, -1, -1]  # visible, x coor, ycoor
        self.lshoulder_average = [0, 0, 0]  # count, x coor, ycoor
        self.rshoulder = [-1, -1, -1]  # visible, x coor, ycoor
        self.rshoulder_average = [0, 0, 0]  # count, x coor, ycoor
        self.ltoe = [-1, -1, -1]  # visible, x coor, ycoor
        self.ltoe_average = [0, 0, 0]  # count, x coor, ycoor
        self.rtoe = [-1, -1, -1]  # visible, x coor, ycoor
        self.rtoe_average = [0, 0, 0]  # count, x coor, ycoor
        self.lheel = [-1, -1, -1]  # visible, x coor, ycoor
        self.lheel_average = [0, 0, 0]  # count, x coor, ycoor
        self.rheel = [-1, -1, -1]  # visible, x coor, ycoor
        self.rheel_average = [0, 0, 0]  # count, x coor, ycoor

    def DetectSingleImg(self, image):

        with self.mp_holistic.Holistic(
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

        timer = Timer()
        heel_click_timer = Timer()
        hip_jump_timer = Timer()
        hand_jump_timer = Timer()
        calculated_average = False
        w_pressed = False

        reset_heels = True
        reset_hips = True
        reset_hands = True

        keyboard = Controller()

        with self.mp_holistic.Holistic(
                model_complexity=2,
                min_detection_confidence=0.5,
                min_tracking_confidence=0.7
        ) as holistic:
            while self.cap.isOpened():
                success, image = self.cap.read()

                image = cv2.resize(image, (1280, 720))
                image.flags.writeable = False
                image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
                results = holistic.process(image)
                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                self.mp_drawing.draw_landmarks(image, results.pose_landmarks, self.mp_holistic.POSE_CONNECTIONS)

                # joints (left and right are flipped)
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
                    if results.pose_landmarks.landmark[
                        self.mp_holistic.PoseLandmark.LEFT_SHOULDER].visibility > 0.8:
                        self.lshoulder = [1, results.pose_landmarks.landmark[
                            self.mp_holistic.PoseLandmark.LEFT_SHOULDER].x,
                                          results.pose_landmarks.landmark[
                                              self.mp_holistic.PoseLandmark.LEFT_SHOULDER].y]
                    if results.pose_landmarks.landmark[
                        self.mp_holistic.PoseLandmark.RIGHT_SHOULDER].visibility > 0.8:
                        self.rshoulder = [1,
                                          results.pose_landmarks.landmark[
                                              self.mp_holistic.PoseLandmark.RIGHT_SHOULDER].x,
                                          results.pose_landmarks.landmark[
                                              self.mp_holistic.PoseLandmark.RIGHT_SHOULDER].y]
                    if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_ELBOW].visibility > 0.8:
                        self.lelbow = [1,
                                       results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_ELBOW].x,
                                       results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_ELBOW].y]
                    if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_ELBOW].visibility > 0.8:
                        self.relbow = [1,
                                       results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_ELBOW].x,
                                       results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_ELBOW].y]
                    if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_WRIST].visibility > 0.8:
                        self.lhand = [1,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_WRIST].x,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_WRIST].y]
                    if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_WRIST].visibility > 0.8:
                        self.rhand = [1,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_WRIST].x,
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
                        self.rknee = [1,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_KNEE].x,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_KNEE].y]
                    if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HEEL].visibility > 0.8:
                        self.lheel = [1, results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HEEL].x,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.LEFT_HEEL].y]
                    if results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HEEL].visibility > 0.8:
                        self.rheel = [1,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HEEL].x,
                                      results.pose_landmarks.landmark[self.mp_holistic.PoseLandmark.RIGHT_HEEL].y]
                    if results.pose_landmarks.landmark[
                        self.mp_holistic.PoseLandmark.LEFT_FOOT_INDEX].visibility > 0.8:
                        self.ltoe = [1, results.pose_landmarks.landmark[
                            self.mp_holistic.PoseLandmark.LEFT_FOOT_INDEX].x,
                                     results.pose_landmarks.landmark[
                                         self.mp_holistic.PoseLandmark.LEFT_FOOT_INDEX].y]
                    if results.pose_landmarks.landmark[
                        self.mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX].visibility > 0.8:
                        self.rtoe = [1, results.pose_landmarks.landmark[
                            self.mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX].x,
                                     results.pose_landmarks.landmark[
                                         self.mp_holistic.PoseLandmark.RIGHT_FOOT_INDEX].y]

                if float(timer.getCurrentTime()) < 8:
                    image = cv2.putText(image, 'Waiting...', (1000, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (255, 0, 0), 2, cv2.LINE_AA)
                elif 8 <= float(timer.getCurrentTime()) < 15:
                    image = cv2.putText(image, 'Calibrating...', (1000, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (126, 126, 0), 2, cv2.LINE_AA)
                    if self.lelbow[0] == 1:
                        self.lelbow_average[0] += self.lelbow[0]
                        self.lelbow_average[1] += self.lelbow[1]
                        self.lelbow_average[2] += self.lelbow[2]
                    if self.relbow[0] == 1:
                        self.relbow_average[0] += self.relbow[0]
                        self.relbow_average[1] += self.relbow[1]
                        self.relbow_average[2] += self.relbow[2]
                    if self.lhand[0] == 1:
                        self.lhand_average[0] += self.lhand[0]
                        self.lhand_average[1] += self.lhand[1]
                        self.lhand_average[2] += self.lhand[2]
                    if self.rhand[0] == 1:
                        self.rhand_average[0] += self.rhand[0]
                        self.rhand_average[1] += self.rhand[1]
                        self.rhand_average[2] += self.rhand[2]
                    if self.lhip[0] == 1:
                        self.lhip_average[0] += self.lhip[0]
                        self.lhip_average[1] += self.lhip[1]
                        self.lhip_average[2] += self.lhip[2]
                    if self.rhip[0] == 1:
                        self.rhip_average[0] += self.rhip[0]
                        self.rhip_average[1] += self.rhip[1]
                        self.rhip_average[2] += self.rhip[2]
                    if self.lshoulder[0] == 1:
                        self.lshoulder_average[0] += self.lshoulder[0]
                        self.lshoulder_average[1] += self.lshoulder[1]
                        self.lshoulder_average[2] += self.lshoulder[2]
                    if self.rshoulder[0] == 1:
                        self.rshoulder_average[0] += self.rshoulder[0]
                        self.rshoulder_average[1] += self.rshoulder[1]
                        self.rshoulder_average[2] += self.rshoulder[2]
                    if self.lknee[0] == 1:
                        self.lknee_average[0] += self.lknee[0]
                        self.lknee_average[1] += self.lknee[1]
                        self.lknee_average[2] += self.lknee[2]
                    if self.rknee[0] == 1:
                        self.rknee_average[0] += self.rknee[0]
                        self.rknee_average[1] += self.rknee[1]
                        self.rknee_average[2] += self.rknee[2]
                    if self.ltoe[0] == 1:
                        self.ltoe_average[0] += self.ltoe[0]
                        self.ltoe_average[1] += self.ltoe[1]
                        self.ltoe_average[2] += self.ltoe[2]
                    if self.rtoe[0] == 1:
                        self.rtoe_average[0] += self.rtoe[0]
                        self.rtoe_average[1] += self.rtoe[1]
                        self.rtoe_average[2] += self.rtoe[2]
                    if self.lheel[0] == 1:
                        self.lheel_average[0] += self.lheel[0]
                        self.lheel_average[1] += self.lheel[1]
                        self.lheel_average[2] += self.lheel[2]
                    if self.rheel[0] == 1:
                        self.rheel_average[0] += self.rheel[0]
                        self.rheel_average[1] += self.rheel[1]
                        self.rheel_average[2] += self.rheel[2]
                else:
                    image = cv2.putText(image, 'Active', (1000, 50), cv2.FONT_HERSHEY_SIMPLEX,
                                        1, (0, 255, 0), 2, cv2.LINE_AA)
                    if not calculated_average:
                        if self.lelbow_average[0] > 0:
                            self.lelbow_average = [0, self.lelbow_average[1]/self.lelbow_average[0], self.lelbow_average[2]/self.lelbow_average[0]]
                        if self.relbow_average[0] > 0:
                            self.relbow_average = [0, self.relbow_average[1]/self.relbow_average[0], self.relbow_average[2]/self.relbow_average[0]]
                        if self.lhand_average[0] > 0:
                            self.lhand_average = [0, self.lhand_average[1]/self.lhand_average[0], self.lhand_average[2]/self.lhand_average[0]]
                        if self.rhand_average[0] > 0:
                            self.rhand_average = [0, self.rhand_average[1]/self.rhand_average[0], self.rhand_average[2]/self.rhand_average[0]]
                        if self.lhip_average[0] > 0:
                            self.lhip_average = [0, self.lhip_average[1]/self.lhip_average[0], self.lhip_average[2]/self.lhip_average[0]]
                        if self.rhip_average[0] > 0:
                            self.rhip_average = [0, self.rhip_average[1]/self.rhip_average[0], self.rhip_average[2]/self.rhip_average[0]]
                        if self.lknee_average[0] > 0:
                            self.lknee_average = [0, self.lknee_average[1]/self.lknee_average[0], self.lknee_average[2]/self.lknee_average[0]]
                        if self.rknee_average[0] > 0:
                            self.rknee_average = [0, self.rknee_average[1]/self.rknee_average[0], self.rknee_average[2]/self.rknee_average[0]]
                        if self.lshoulder_average[0] > 0:
                            self.lshoulder_average = [0, self.lshoulder_average[1]/self.lshoulder_average[0], self.lshoulder_average[2]/self.lshoulder_average[0]]
                        if self.rshoulder_average[0] > 0:
                            self.rshoulder_average = [0, self.rshoulder_average[1]/self.rshoulder_average[0], self.rshoulder_average[2]/self.rshoulder_average[0]]
                        if self.ltoe_average[0] > 0:
                            self.ltoe_average = [0, self.ltoe_average[1]/self.ltoe_average[0], self.ltoe_average[2]/self.ltoe_average[0]]
                        if self.rtoe_average[0] > 0:
                            self.rtoe_average = [0, self.rtoe_average[1]/self.rtoe_average[0], self.rtoe_average[2]/self.rtoe_average[0]]
                        if self.lheel_average[0] > 0:
                            self.lheel_average = [0, self.lheel_average[1]/self.lheel_average[0], self.lheel_average[2]/self.lheel_average[0]]
                        if self.rheel_average[0] > 0:
                            self.rheel_average = [0, self.rheel_average[1]/self.rheel_average[0], self.rheel_average[2]/self.rheel_average[0]]
                        self.average_heel_distance = abs(self.lheel_average[1] - self.rheel_average[1])
                        self.average_hip_height = (self.lhip_average[2] + self.rhip_average[2])/2
                        self.average_hand_height = (self.lhand_average[2] + self.rhand_average[2]) / 2
                        calculated_average = True

                    # detect heel clicking Test: average .18, clicked .02
                    current_heel_distance = abs(self.lheel[1] - self.rheel[1])
                    if float(heel_click_timer.getCurrentTime()) > 2:
                        if current_heel_distance < 0.05 and reset_heels:
                            # heels have been clicked
                            keyboard.press('w')
                            w_pressed = True
                            reset_heels = False
                            heel_click_timer.reset()
                            print("HEELS CLICKED")
                        elif w_pressed:
                            print("W RELEASED")
                            keyboard.release('w')
                            w_pressed = False

                    if self.average_heel_distance * 0.8 < current_heel_distance < self.average_heel_distance * 1.2 and not reset_heels:
                        print("HEELS RESET")
                        reset_heels = True

                    # detect hand lift
                    current_hand_height = (self.lhand[2] + self.rhand[2])/2
                    if float(hand_jump_timer.getCurrentTime()) > 2:
                        if current_hand_height + 0.15 < self.average_hand_height and reset_hands:
                            # heels have been clicked
                            keyboard.press('w')
                            w_pressed = True
                            reset_hands = False
                            hand_jump_timer.reset()
                            print("HANDS LIFTED")
                        elif w_pressed:
                            print("W RELEASED")
                            keyboard.release('w')
                            w_pressed = False
                    if self.average_hand_height * 0.8 < current_hand_height < self.average_hand_height * 1.2 and not reset_hands:
                        print("HANDS RESET")
                        reset_hands = True

                    # detect hip heightening
                    current_hip_height = (self.lhip[2] + self.rhip[2])/2
                    if float(hip_jump_timer.getCurrentTime()) > 1:
                        if current_hip_height + 0.1 < self.average_hip_height and reset_hips:
                            # hips have jumped
                            keyboard.press(Key.space)
                            reset_hips = False
                            hip_jump_timer.reset()
                            print("HIPS JUMPED")
                            keyboard.release(Key.space)
                    if self.average_hip_height * 0.9 < current_hip_height < self.average_hip_height * 1.1 and not reset_hips:
                        print("HIPS RESET")
                        reset_hips = True

                cv2.imshow('MediaPipe Pose', image)
                if cv2.waitKey(5) & 0xFF == 27:
                    break
            cv2.destroyAllWindows()


# # TESTING : standalone version for mediapipe
if __name__ == "__main__":
    MHD = MediaPipeHolisticDetection()  # initialize our detection class
    MHD.StartDetection()
