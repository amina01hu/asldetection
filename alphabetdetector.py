'''
FUNCTION FOR PICKING UP ALPHABET IN ASL 
'''

def asl_a(hand_landmarks):
    """
    Detects ASL letter A based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check that all fingertips are below their PIP joints
    fingers_curled = (
        landmarks[8].y > landmarks[6].y and  # Index finger
        landmarks[12].y > landmarks[10].y and  # Middle finger
        landmarks[16].y > landmarks[14].y and  # Ring finger
        landmarks[20].y > landmarks[18].y and    # Pinky
        landmarks[8].y > landmarks[7].y and  # Index finger
        landmarks[12].y > landmarks[11].y and  # Middle finger
        landmarks[16].y > landmarks[15].y and  # Ring finger
        landmarks[20].y > landmarks[19].y     # Pinky
    )

    # Check if thumb is up
    thumb_up = (
        landmarks[4].y <= landmarks[3].y and
        landmarks[4].y < landmarks[8].y
        #Thumb tip is near thumb IP  
    )

    return fingers_curled and thumb_up


def asl_b(hand_landmarks):
    """
    Detects ASL letter B based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check if all fingers are extended (index up)
    fingers_up = (
        landmarks[8].y < landmarks[6].y and  # Index finger
        landmarks[12].y < landmarks[10].y and  # Middle finger
        landmarks[16].y < landmarks[14].y and  # Ring finger
        landmarks[20].y < landmarks[18].y     # Pinky
    )

    # Check if thumb is tucked in
    thumb_curled = (
        landmarks[4].x > landmarks[3].x and  # Thumb base is right of IP joint
        landmarks[3].x >= landmarks[8].x      # Thumb is to the left of the index finger
    )

    return fingers_up and thumb_curled


def asl_c(hand_landmarks):
    """
    Detects ASL letter C based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check for 'C' handshape
    return (
        landmarks[8].y > landmarks[7].y and  # Index finger tip is down
        landmarks[12].y > landmarks[11].y and  # Middle finger tip is down
        landmarks[16].y > landmarks[15].y and  # Ring finger tip is down
        landmarks[20].y > landmarks[19].y and  # Pinky tip is down
        landmarks[4].y < landmarks[3].y       # Thumb is curved
    )


def asl_d(hand_landmarks):
    """
    Detects ASL letter D based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check for 'D' handshape
    return (
        landmarks[8].y < landmarks[6].y and  # Index finger is up
        landmarks[12].y > landmarks[10].y and  # Middle finger is curled
        landmarks[16].y > landmarks[14].y and  # Ring finger is curled
        landmarks[20].y > landmarks[18].y and  # Pinky is curled
        landmarks[4].y < landmarks[3].y and   # Thumb is up
        landmarks[4].x > landmarks[3].x        # Thumb is tucked in
    )


def asl_e(hand_landmarks):
    """
    Detects ASL letter E based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check for 'E' handshape
    return (
        landmarks[8].y > landmarks[6].y and  # Index finger is curled down
        landmarks[12].y > landmarks[10].y and  # Middle finger is curled down
        landmarks[16].y > landmarks[14].y and  # Ring finger is curled down
        landmarks[20].y > landmarks[18].y and  # Pinky is curled down
        landmarks[4].x > landmarks[3].x and   # Thumb is to the right
        landmarks[4].y >= landmarks[3].y   # Thumb is to the left of the index finger
    )

def asl_f(hand_landmarks):
    """
    Detects ASL letter F based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check for 'F' handshape
    return (
        landmarks[12].y < landmarks[10].y and  # Middle finger is up
        landmarks[16].y < landmarks[14].y and  # Ring finger is up
        landmarks[20].y < landmarks[18].y and # pink is up
        landmarks[8].y > landmarks[6].y and # index is down
        landmarks[4].y < landmarks[3].y

    )

def asl_g(hand_landmarks):
    """
    Detects ASL letter G based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check for 'g' handshape
    return (
        landmarks[12].x > landmarks[10].x and  # Middle finger is tucked in
        landmarks[16].x > landmarks[14].x and  # Ring finger is tucked in
        landmarks[20].x > landmarks[18].x and # pink finger is tucked in
        landmarks[8].x < landmarks[6].x # index is pointed out

    )

def asl_h(hand_landmarks):
    """
    Detects ASL letter H based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check for 'h' handshape
    return (
        landmarks[12].x < landmarks[10].x and  # Middle finger is pointed out
        landmarks[16].x > landmarks[14].x and  # Ring finger is tucked in
        landmarks[20].x > landmarks[18].x and # pink finger is tucked in
        landmarks[8].x < landmarks[6].x # index is pointed out

    )

def asl_i(hand_landmarks):
    """
    Detects ASL letter I based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check for 'i' handshape
    return (
        landmarks[8].y > landmarks[6].y and  # Index finger is up
        landmarks[12].y > landmarks[10].y and  # Middle finger is curled
        landmarks[16].y > landmarks[14].y and  # Ring finger is curled
        landmarks[20].y < landmarks[18].y and  # Pinky is curled
        landmarks[4].y < landmarks[3].y and   # Thumb is up
        landmarks[4].x > landmarks[3].x        # Thumb is tucked in

    )

## def asl_j

def asl_k(hand_landmarks):
    """
    Detects ASL letter K based on hand landmarks.
    """
    landmarks = hand_landmarks.landmark

    # Check for 'i' handshape
    return (
        landmarks[8].y < landmarks[6].y and  # Index finger is up
        landmarks[12].y < landmarks[10].y and  # Middle finger is up
        landmarks[16].y > landmarks[14].y and  # Ring finger is curled
        landmarks[20].y > landmarks[18].y and  # Pinky is curled
        landmarks[4].y < landmarks[3].y and   # Thumb is up
        landmarks[4].x > landmarks[3].x        # Thumb is tucked in

    )


def asl_alphabet(hand_landmarks):
    """
    Detects ASL letters A, B, C, D, and E based on hand landmarks.
    """
    if asl_a(hand_landmarks):
        return 'A'
    if asl_b(hand_landmarks):
        return 'B'
    if asl_c(hand_landmarks):
        return 'C'
    if asl_d(hand_landmarks):
        return 'D'
    if asl_e(hand_landmarks):
        return 'E'
    if asl_f(hand_landmarks):
        return 'F'
    if asl_g(hand_landmarks):
        return 'G'
    if asl_h(hand_landmarks):
        return 'H'
    if asl_i(hand_landmarks):
        return 'I'
    ## j needs motion detection
    if asl_k(hand_landmarks):
        return "K"

    return 0  # Return None if no letter is detected
