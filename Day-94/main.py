#Exercise: Drink Water Reminder
import time
import pygame

pygame.mixer.init()

sound = pygame.mixer.Sound('notifications-sound-127856.mp3')

reminder_interval = 60

while True:
    current_time = time.time()

    minutes, seconds = divmod(reminder_interval, 60)
    hours, minutes = divmod(minutes, 60)

    print(f"Don't forget to drink water! It's been {hours} hours and {minutes} minutes since your last drink.")

    sound.play()

    time.sleep(reminder_interval)