import cv2
import mediapipe as mp
import pyautogui

vid = cv2.VideoCapture(0)
detect = mp.solutions.hands.Hands(min_detection_confidence=0.7,min_tracking_confidence=0.8)
sw, sh = pyautogui.size()
draw = mp.solutions.drawing_utils
index_x, index_y, ring_x, ring_y, thumb_x, thumb_y, middle_x, middle_y = 0, 0, 0, 0, 0, 0, 0, 0
while True:
    _, frame = vid.read()
    frame = cv2.flip(frame, 1)
    fh, fw, fc = frame.shape
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = detect.process(img)
    hands = res.multi_hand_landmarks
    if hands:
        for hand in hands:
            draw.draw_landmarks(frame, hand)
            for id, landm in enumerate(hand.landmark):
                x = int(landm.x*fw)
                y = int(landm.y*fh)
                if id == 16:
                    cv2.circle(frame, (x, y), 10, (244, 244, 244))
                    ring_x = sw/fw*x
                    ring_y = sh/fh*y
                    pyautogui.moveTo(ring_x, ring_y)
                elif id == 4:
                    cv2.circle(frame, (x, y), 10, (244, 244, 244))
                    thumb_x = sw/fw*x
                    thumb_y = sh/fh*y
                elif id == 8:
                    cv2.circle(frame, (x, y), 10, (244, 244, 244))
                    index_x = sw/fw*x
                    index_y = sh/fh*y
                    if abs(thumb_y-index_y) < 20:
                        pyautogui.click()
                       #pyautogui.sleep(2)
                        print('Left click')
                    
                elif id == 12:
                    cv2.circle(frame, (x, y), 10, (244, 244, 244))
                    middle_x = sw/fw*x
                    middle_y = sh/fh*y
                    if abs(thumb_y-middle_y) < 20:
                        pyautogui.click(button='right')
                        #pyautogui.sleep(2)
                        print('Right click')
                    
                elif id == 20:
                    cv2.circle(frame, (x, y), 10, (244, 244, 244))
                    pinky_x = sw/fw*x
                    pinky_y = sh/fh*y
                    if abs(thumb_y-pinky_y) < 20:
                        pyautogui.click(clicks=2)
                        #pyautogui.sleep(2)
                        print('Double click')
                   
    ex = cv2.waitKey(10)
    if ex == ord('q'):
        break
    cv2.imshow("Virtual Pointer", frame)
vid.release()
cv2.destroyAllWindows()
