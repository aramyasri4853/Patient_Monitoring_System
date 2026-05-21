def detect_head_gesture(landmarks, w, h):
    # Nose tip
    nose = landmarks[1]
    nose_x = int(nose.x * w)
    nose_y = int(nose.y * h)

    # Face center using cheek landmarks
    left_cheek = landmarks[234]
    right_cheek = landmarks[454]

    center_x = int(((left_cheek.x + right_cheek.x) / 2) * w)
    center_y = int(((left_cheek.y + right_cheek.y) / 2) * h)

    dx = nose_x - center_x
    dy = nose_y - center_y

    gesture = "CENTER"

    # Swap LEFT and RIGHT due to mirrored camera
    if dx > 20:
        gesture = "LEFT"
    elif dx < -20:
        gesture = "RIGHT"
    elif dy > 20:
        gesture = "DOWN"
    elif dy < -20:
        gesture = "UP"

    return gesture