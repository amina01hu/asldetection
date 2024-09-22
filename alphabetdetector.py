import cv2

# higher y coordinate means landmark is closer to bottom of screen 
def asl_alphabet(hand_landmarks):
    # LETTER A
    landmarks = hand_landmarks.landmark

    # Check that all fingertups are below their PIP
    fingercurled = (
        landmarks[8].y > landmarks[6].y and # index finger
        landmarks[12].y > landmarks[10].y and # middle finger
        landmarks[16].y > landmarks[14].y and # ring finger
        landmarks[20].y > landmarks[18].y
    )

    #check that all fingers are up

    fingersup = (
        landmarks[8].y < landmarks[6].y and # index finger
        landmarks[12].y < landmarks[10].y and # middle finger
        landmarks[16].y < landmarks[14].y and # ring finger
        landmarks[20].y < landmarks[18].y
    )

    # check if thumb is tucked in
    thumbcurled = (
        landmarks[4].x > landmarks[3].x and
        landmarks[3].x >= landmarks[8].x
    )

    # check that thumb is up

    thumbup = (
        landmarks[4].x <= landmarks[4].x  # check if thumb tip is near thumb IP
    )


    if(fingercurled and thumbup):
        return 'A'
    if (fingersup and thumbcurled):
        return 'B'
   
    return 0