def detect_hand_emergency(hand_landmarks, h):
    lm = hand_landmarks.landmark

    # Thumb tip and joint
    thumb_tip = lm[4]
    thumb_ip = lm[3]

    # Other finger tips and joints
    index_tip, index_pip = lm[8], lm[6]
    middle_tip, middle_pip = lm[12], lm[10]
    ring_tip, ring_pip = lm[16], lm[14]
    little_tip, little_pip = lm[20], lm[18]

    # Thumb must be extended (tip higher than joint)
    thumb_up = thumb_tip.y < thumb_ip.y

    # Other fingers must be folded (tips lower than joints)
    index_folded = index_tip.y > index_pip.y
    middle_folded = middle_tip.y > middle_pip.y
    ring_folded = ring_tip.y > ring_pip.y
    little_folded = little_tip.y > little_pip.y

    # Strict thumbs-up condition
    if thumb_up and index_folded and middle_folded and ring_folded and little_folded:
        return True

    return False