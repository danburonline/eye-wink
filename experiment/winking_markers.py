import os
from time import sleep
from datetime import datetime
import csv
import platform

# duration until experiment starts (left)
marker1 = 10

# duration of each condition
duration_cond = 2

# duration of recording
duration = 120 + 10

# get starting timestamp
start = datetime.now()
update = datetime.now()

# initialize stuff for markers
marker = ""
sound0_init = True
sound1_init = True

# store markers and send tones
with open(
    "markers_winking_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv", "w"
) as f:
    while update.timestamp() < start.timestamp() + duration:

        if update.timestamp() > start.timestamp() + marker1:

            # create marker and play tones and the right time
            if platform.system() == "Darwin":  # mac os
                os.system("say 'left'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('left')\""
                )

            # write marker to csv
            update = datetime.now()
            marker = "left"
            writer = csv.writer(f)
            writer.writerow([update.timestamp() + 3600, marker])
            sleep(1.5)

            if platform.system() == "Darwin":  # mac os
                os.system("say 'right'")
            elif platform.system() == "Windows":  # windows
                os.system(
                    "powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('right')\""
                )

            # write marker to csv
            update = datetime.now()
            marker = "right"
            writer = csv.writer(f)
            writer.writerow([update.timestamp() + 3600, marker])
            sleep(1.5)

        update = datetime.now()
