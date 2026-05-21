import cv2
import winsound
import voice_module
from call_alert import make_call
from email_alert import send_email_alert
from preprocessing import initialize_models, process_frame
from decision_engine import check_emergency


def start_system():

    print("Step 1: Initializing models...")
    face_mesh, hands = initialize_models()

    print("Step 2: Starting voice listener...")
    voice_module.start_voice_listener()

    print("Step 3: Opening camera...")

    
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    #cap = cv2.VideoCapture(2)
    print("Camera object created")

    if not cap.isOpened():
        print("Camera not accessible ❌")
        return
    else:
        print("Camera opened successfully ✔")

    # 🔔 Track previous state
    prev_emergency = False

    while True:

        ret, frame = cap.read()

        if not ret:
            print("Frame capture failed")
            break

        frame, thumbs_up = process_frame(frame, face_mesh, hands)

        alert_message = check_emergency(thumbs_up, voice_module.voice_command)

        # -------- ALARM LOGIC --------
        current_emergency = bool(alert_message)

        # Play alarm only when state changes NORMAL → EMERGENCY
        if current_emergency and not prev_emergency:
            winsound.Beep(2000, 700)
            send_email_alert(alert_message)
            make_call(alert_message)

        prev_emergency = current_emergency
        # -------- END ALARM --------

        # -------- UI PANEL --------
        cv2.rectangle(frame, (10,10), (320,90), (0,0,0), -1)

        cv2.putText(frame, "SMART PATIENT MONITOR", (20,35),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

        if alert_message:

            cv2.putText(frame, "STATUS : EMERGENCY", (20,65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

            cv2.putText(frame, alert_message, (20,120),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

            print(alert_message)

        else:

            cv2.putText(frame, "STATUS : NORMAL", (20,65),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        # -------- END UI --------

        cv2.imshow("Smart Patient Monitoring System", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    start_system()
