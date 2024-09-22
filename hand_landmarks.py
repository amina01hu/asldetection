import cv2

# higher y coordinate means landmark is closer to bottom of screen 
def is_thumbs_up(img, landmarks, mp_hands):
    #Thumbs landmarks 2 (MCP), 2(IP), 4(TIP)

    thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP].y
    thumb_mcp = landmarks[mp_hands.HandLandmark.THUMB_MCP].y

    #Finger tips: Index(8), Middle(12), Ring(16), Pinky(20)

    index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y
    middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y
    ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y
    pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP].y

    thumb_is_up = thumb_tip < index_tip and thumb_tip < middle_tip and thumb_tip < ring_tip and thumb_tip < pinky_tip

    index_folded = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_folded = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_folded = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP].y > landmarks[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_folded = landmarks[mp_hands.HandLandmark.PINKY_TIP].y > landmarks[mp_hands.HandLandmark.PINKY_PIP].y
    
    return thumb_is_up and index_folded and middle_folded and ring_folded and pinky_folded