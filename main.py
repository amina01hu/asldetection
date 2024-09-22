'''
APPLICATION FOR READING SIGN LANGUAGE FROM CAMERA
'''
import cv2
import mediapipe as mp
from google.protobuf.json_format import MessageToDict
from hand_landmarks import is_thumbs_up

from alphabetdetector import asl_alphabet

# Initialize the hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    model_complexity=1,
    min_detection_confidence=0.75,
    min_tracking_confidence=0.75,
    max_num_hands=2
)

# Initialize drawing utilities
mp_drawing = mp.solutions.drawing_utils

# Initialize video capture
cap = cv2.VideoCapture(0)

##def is_thumbs_up(landmarks):
    #Thumb landmarks: 2 (MCP), 3(IP), 4 (TIP)


while True:
    # Read video frame by frame
    success, img = cap.read()

    # Flip the image horizontally for a mirror view
    img = cv2.flip(img, 1)

    # Convert the BGR image to RGB
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the RGB image to detect hands
    results = hands.process(imgRGB)

    # If hands are detected in the image
    if results.multi_hand_landmarks:
        # Check if both hands are detected
        if len(results.multi_handedness) == 2:
            # Display 'Both Hands' on the image
            cv2.putText(img, 'Both Hands', (250, 50),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.9, (0, 255, 0), 2)

        # If only one hand is detected
        else:
            for i in results.multi_handedness:
                # Get whether it is a Right or Left hand
                label = MessageToDict(i)['classification'][0]['label']

                if label == 'Left':
                    # Display 'Left Hand' on the left side of the window
                    cv2.putText(img, label + ' Hand', (20, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                0.9, (0, 255, 0), 2)

                if label == 'Right':
                    # Display 'Right Hand' on the right side of the window
                    cv2.putText(img, label + ' Hand', (460, 50),
                                cv2.FONT_HERSHEY_COMPLEX,
                                0.9, (0, 255, 0), 2)

        # Draw hand landmarks on the image for each detected hand
        for hand_landmarks in results.multi_hand_landmarks:
            # Draw the hand landmarks and connections
            for idx, landmark in enumerate(hand_landmarks.landmark):
            # Get the height, width, and channels of the image
                h, w, _ = img.shape
                # Convert the normalized landmark coordinates to pixel values
                cx, cy = int(landmark.x * w), int(landmark.y * h)

                # Put the landmark index on the image at the coordinates
                cv2.putText(img, str(idx), (cx, cy),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
            mp_drawing.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(255, 192, 203), thickness=2, circle_radius=2),
                mp_drawing.DrawingSpec(color=(0, 0, 0), thickness=2))

            if is_thumbs_up(img, hand_landmarks.landmark, mp_hands):
                cv2.putText(img, 'Thumbs Up!', (50, 50), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)
            else:
                cv2.putText(img, 'Not Thumbs Up!', (50, 50),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 0), 2)

            if asl_alphabet(hand_landmarks) != 0:
                cv2.putText(img, 'Letter ' + asl_alphabet(hand_landmarks),
                            (50, 300),
                            cv2.FONT_HERSHEY_PLAIN,
                            1, (0, 0, 0), 2)

            x_min, y_min = float('inf'), float('inf')
            x_max, y_max = float('-inf'), float('-inf')

             # draw rectangle on each detected hand
            for landmark in hand_landmarks.landmark:
                h, w, _ = img.shape
                cx, cy = int(landmark.x * w), int(landmark.y * h)

                #update the bounding box coordinates
                x_min, y_min = min(x_min, cx), min(y_min, cy)
                x_max, y_max = max(x_max, cx), max(y_max, cy)


    cv2.rectangle(img, (x_min - 10, y_min - 10), (x_max + 10, y_max + 10), (0, 0, 0), 2)
             # Loop through all 21 landmarks
    # Display the image with hand landmarks
    cv2.imshow('Hand Recognition', img)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

# Release the video capture and destroy all OpenCV windows
cap.release()
cv2.destroyAllWindows()
