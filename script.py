import webbrowser
import time
import pygame

# Initialize Pygame
pygame.mixer.init()
alert_sound = 'alert_sound.mp3'

# Load your sound file
pygame.mixer.music.load(alert_sound)

# Write the link you want to open here
link = 'https://github.com/ogulcanwolf'

# Open the link every 5 minutes and display a countdown
while True:
    for remaining in range(300, 0, -1):  # 10 minutes = 600 seconds
        minutes, seconds = divmod(remaining, 60)
        time_str = f"{minutes:02}:{seconds:02}"
        print(f"Countdown: {time_str}", end='\r')
        time.sleep(1)
    
    # Open the link
    webbrowser.open(link)
    
    # Play an audible alert
    pygame.mixer.music.play()
    
    # Information message
    print("Link opened! (Audible alert played)")

    # Wait 5 seconds to hear the alert sound
    # time.sleep(5)
