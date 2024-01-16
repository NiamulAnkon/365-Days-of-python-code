import speech_recognition as sr
import pyttsx3
import datetime
import os
import json

class TaskScheduler:
    def __init__(self):
        self.tasks = {}
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def get_audio(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source, timeout=5)
            print("Processing...")

        try:
            command = self.recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Could not understand audio. Please try again.")
            return None
        except sr.RequestError as e:
            print(f"Error making the request; {e}")
            return None

    def schedule_task(self, task_name, date, time):
        timestamp = datetime.datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M")
        self.tasks[task_name] = timestamp.strftime("%Y-%m-%d %H:%M")
        self.save_tasks()

    def view_tasks(self):
        if not self.tasks:
            self.speak("You have no tasks scheduled.")
        else:
            self.speak("Your upcoming tasks are:")
            for task, timestamp in self.tasks.items():
                self.speak(f"{task} on {timestamp}")

    def save_tasks(self):
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)

    def run(self):
        self.load_tasks()

        while True:
            self.speak("How can I assist you?")
            command = self.get_audio()

            if not command:
                continue

            if "schedule" in command:
                self.speak("What task would you like to schedule?")
                task_name = self.get_audio()

                self.speak("On which date?")
                date = self.get_audio()

                self.speak("At what time?")
                time = self.get_audio()

                self.schedule_task(task_name, date, time)
                self.speak("Task scheduled successfully.")

            elif "view" in command:
                self.view_tasks()

            elif "exit" in command:
                self.speak("Exiting. Have a great day!")
                break

            else:
                self.speak("Command not recognized. Please try again.")

if __name__ == "__main__":
    scheduler = TaskScheduler()
    scheduler.run()
