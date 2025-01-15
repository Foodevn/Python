from datetime import date


you="today"
if you == "hi":
    robot_brain="Hello"
elif you == "bye":
      robot_brain="Goodbye"
elif you == "today":
    today = date.today()
    robot_brain=today.strftime("%B %d, %Y")
else:
      robot_brain="I don't understand"

print(robot_brain)