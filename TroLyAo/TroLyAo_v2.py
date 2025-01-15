import speech_recognition
import pyttsx3
from datetime import date, datetime

robot_ear = speech_recognition.Recognizer()
robot_brain=""
robot_mouth = pyttsx3.init()

while True:
# nghe
    with speech_recognition.Microphone() as mic:
        print("Robot: I'm listening")
        audio = robot_ear.listen(mic)

    try:
        you = robot_ear.recognize_google(audio)
    except:
        you = ""
    print("You: " + you)

    print("robot: .....")

    # xử lý
    if "hi" in you:
        robot_brain="Hello you"
    elif  "bye"in you:
        robot_brain="Goodbye"
    elif "today"in you:
        today = date.today()
        robot_brain=today.strftime("%B %d, %Y")
    elif  "time"in you:
        now = datetime.now()
        robot_brain=now.strftime("%H hours %M minutes %S seconds")
    else:
        robot_brain="I don't understand"

    print("robot: ",robot_brain)

    # nói
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    if("bye" in you):
        break