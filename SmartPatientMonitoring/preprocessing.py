import cv2
import mediapipe as mp
from eye_blink import calculate_EAR, LEFT_EYE, RIGHT_EYE
from head_gesture import detect_head_gesture
from hand_gesture import detect_hand_emergency

mp_face = mp.solutions.face_mesh
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

blink_counter = 0
ear_history = []
calibrated = False
baseline_EAR = 0
frame_count = 0


def initialize_models():
    face_mesh = mp_face.FaceMesh(refine_landmarks=True)
    hands = mp_hands.Hands(max_num_hands=2)
    return face_mesh, hands


def process_frame(frame, face_mesh, hands):

    global blink_counter, ear_history, calibrated, baseline_EAR, frame_count

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    h, w, _ = frame.shape

    face_results = face_mesh.process(rgb_frame)
    hand_results = hands.process(rgb_frame)

    thumbs_up_detected = False

    # -------- FACE PROCESSING --------
    if face_results.multi_face_landmarks:
        for face_landmarks in face_results.multi_face_landmarks:

            mp_draw.draw_landmarks(
                frame,
                face_landmarks,
                mp_face.FACEMESH_TESSELATION
            )

            left_EAR = calculate_EAR(face_landmarks.landmark, LEFT_EYE, w, h)
            right_EAR = calculate_EAR(face_landmarks.landmark, RIGHT_EYE, w, h)

            avg_EAR = (left_EAR + right_EAR) / 2
            frame_count += 1

            if not calibrated:
                ear_history.append(avg_EAR)

                if frame_count >= 30:
                    baseline_EAR = sum(ear_history) / len(ear_history)
                    calibrated = True

            else:

                threshold = baseline_EAR * 0.75

                if avg_EAR < threshold:
                    blink_counter += 1
                else:
                    if blink_counter >= 2:
                        cv2.putText(frame, "BLINK DETECTED", (450,70),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0),2)
                    blink_counter = 0

            gesture = detect_head_gesture(face_landmarks.landmark, w, h)

            cv2.putText(frame, f"HEAD: {gesture}", (450,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0),2)

    # -------- HAND PROCESSING --------
    if hand_results.multi_hand_landmarks:
        for hand_landmarks in hand_results.multi_hand_landmarks:

            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS
            )

            if detect_hand_emergency(hand_landmarks, h):
                thumbs_up_detected = True

    return frame, thumbs_up_detected