import speech_recognition
import pyttsx3
from datetime import date, datetime
import openai

robot_ear = speech_recognition.Recognizer()
robot_brain=""
robot_mouth = pyttsx3.init()

# Initialize the OpenAI API client
openai.api_key = 'your_openai_api_key'

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

    # Use OpenAI GPT-3 to generate a response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": you}
        ],
        max_tokens=50
    )

    robot_brain = response.choices[0].message['content'].strip()

    print("robot: ", robot_brain)

    # nói
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()
    if "bye" in you:
        break