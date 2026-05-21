import cv2

def start_video_stream():
    cap = cv2.VideoCapture(0)  # Open default webcam
    
    if not cap.isOpened():
        print("Error: Cannot access camera")
        return

    print("Press 'q' to exit video stream")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the video frame
        cv2.imshow("Patient Live Monitoring", frame)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()