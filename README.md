# Smart Patient Monitoring System

##  Project Overview

The Smart Patient Monitoring System is an AI-based healthcare monitoring application developed using Python, Computer Vision, and Voice Recognition technologies. The main objective of this project is to continuously monitor patient activity in real time and provide immediate alerts during emergency situations.

The system uses a camera and microphone to monitor the patient. It detects patient activities such as hand gestures, eye blinking, head movement, and emergency voice commands. Whenever an emergency keyword such as “help,” “doctor,” or “water” is recognized, the system automatically triggers alerts including an alarm sound, email notification, and phone call notification using Twilio API.

This project is designed to reduce dependency on manual supervision and improve patient safety, especially for elderly or home-based patients.

---

#  Objectives

* To monitor patients continuously in real time.
* To detect emergency situations automatically.
* To recognize patient voice commands.
* To analyze patient activity using computer vision.
* To send instant alerts to caregivers.
* To provide a low-cost and user-friendly healthcare monitoring solution.

---

# 🛠 Technologies Used

| Technology         | Purpose                                   |
| ------------------ | ----------------------------------------- |
| Python             | Core programming language                 |
| OpenCV             | Video processing and image analysis       |
| MediaPipe          | Hand tracking and face landmark detection |
| SpeechRecognition  | Voice command recognition                 |
| PyAudio            | Microphone support                        |
| NumPy              | Numerical computations                    |
| SMTP               | Sending email alerts                      |
| Twilio API         | Sending phone call alerts                 |
| Visual Studio Code | Development environment                   |

---

#  Working Process

## Step 1: Camera Initialization

The system starts by initializing the webcam using OpenCV. Real-time video frames are captured continuously.

## Step 2: Gesture and Activity Detection

Using MediaPipe and OpenCV:

* Hand gestures are detected.
* Eye blink patterns are monitored.
* Head movement analysis is performed.
* Thumbs-up gesture indicates normal condition.

## Step 3: Voice Recognition

The microphone continuously listens for emergency keywords such as:

* “help”
* “doctor”
* “water”

SpeechRecognition converts speech into text and checks for these predefined keywords.

## Step 4: Decision Engine

The decision engine combines:

* Gesture detection
* Eye blink monitoring
* Head movement analysis
* Voice recognition

If an emergency condition is detected, the system activates alerts.

## Step 5: Alert Generation

The system performs the following actions:

1. Plays alarm sound
2. Sends email notification
3. Initiates phone call alert using Twilio API

---

#  Execution Flow

1. Start the application
2. Initialize camera and microphone
3. Capture video and audio input
4. Detect patient activity
5. Recognize emergency keywords
6. Analyze patient condition
7. Trigger alerts if emergency is detected
8. Notify caregivers immediately

---

#  How to Run the Project

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/Smart-Patient-Monitoring-System.git
```

## Step 2: Open Project Folder

```bash
cd Smart-Patient-Monitoring-System
```

## Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

## Step 4: Run the Application

```bash
python main.py
```

---

#  Email Alert Configuration

To send email alerts:

1. Enable 2-Step Verification in Gmail.
2. Generate App Password.
3. Add sender email and app password in email.py file.

Example:

```python
SENDER_EMAIL = "yourmail@gmail.com"
APP_PASSWORD = "your_app_password"
```

---

#  Twilio Call Alert Configuration

1. Create Twilio account.
2. Get:

   * Account SID
   * Auth Token
   * Twilio Phone Number
3. Add credentials in call.py file.

Example:

```python
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
twilio_number = "+1XXXXXXXXXX"
```

---

# Advantages

* Real-time monitoring
* Contactless healthcare monitoring
* Easy to use
* Cost-effective
* Automated emergency alerts
* Reduces manual supervision

---

# Future Enhancements

* Heart rate sensor integration
* Mobile application support
* Cloud database integration
* AI-based health prediction
* Multi-patient monitoring

---

#  Conclusion

The Smart Patient Monitoring System provides an intelligent and efficient solution for healthcare monitoring. By integrating computer vision and voice recognition technologies, the system can monitor patient activity continuously and provide immediate alerts during emergencies.

This project demonstrates how AI-based technologies can improve patient safety, reduce manual supervision, and ensure faster response during critical situations.

---

#  Authors

* Angadi Ramya Sri (24265A0501)
* Parelli Swetha (24265A0504)

Department of Computer Science and Engineering
Mahatma Gandhi Institute of Technology (MGIT)
