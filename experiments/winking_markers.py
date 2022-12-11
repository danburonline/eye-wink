"""This script creates markers for the winking experiment used as labels for the classifier"""
import os
from time import sleep
from datetime import datetime
import csv
import platform

# duration until experiment starts (left)
MARKER_1 = 10

# duration of each condition
DURATION_COND = 2

# duration of recording
DURATION = 120 + 10

# get starting timestamp
start = datetime.now()
update = datetime.now()

# initialize stuff for markers
INIT_MARKER = ""
SOUND0_INIT = True
SOUND1_INIT = True

# Store markers and send sounds
with open(
    "markers_winking_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv", "w"
) as f:
    while update.timestamp() < start.timestamp() + DURATION:

        if update.timestamp() > start.timestamp() + MARKER_1:

            # Create marker and play tones and the right time
            if platform.system() == "Darwin":  # mac os
                os.system("say 'left'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('left')\""
                )

            # Write marker to csv
            update = datetime.now()
            INIT_MARKER = "left"
            writer = csv.writer(f)
            writer.writerow([update.timestamp() + 3600, INIT_MARKER])
            sleep(3)

            if platform.system() == "Darwin":  # mac os
                os.system("say 'right'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('right')\""
                )

            # Write marker to csv
            update = datetime.now()
            INIT_MARKER = "right"
            writer = csv.writer(f)
            writer.writerow([update.timestamp() + 3600, INIT_MARKER])
            sleep(3)

            if platform.system() == "Darwin":  # mac os
                os.system("say 'waiting'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('waiting')\""
                )

            # Write a waiting marker to csv
            update = datetime.now()
            INIT_MARKER = "waiting"
            writer = csv.writer(f)
            writer.writerow([update.timestamp() + 3600, INIT_MARKER])
            sleep(4)

        update = datetime.now()
