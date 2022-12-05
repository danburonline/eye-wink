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
duration = 120+10

# get starting timestamp
start = datetime.now()
update = datetime.now()

# initialize stuff for markers
marker = ""
sound0_init = True
sound1_init = True

# store markers and send tones
with open("markers_winking_"+datetime.now().strftime("%d%m%Y_%H%M%S")+".csv", "w") as f:

    sleep(marker1)
    
    while update.timestamp() < start.timestamp() + duration:

        # create marker and play tones and the right time
        if platform.system() == "Darwin": # mac os
            os.system("say 'left'")
        elif platform.system() == "Windows": # windows
            os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('left')\"")  
        marker = "left"
        writer = csv.writer(f)
        writer.writerow([update.timestamp(), marker])
        sleep(2)

        if platform.system() == "Darwin": # mac os
            os.system("say 'right'")
        elif platform.system() == "Windows": # windows
            os.system("powershell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('right')\"")  
        marker = "right"
        writer = csv.writer(f)
        writer.writerow([update.timestamp(), marker])
        sleep(2)

        # write to csv file
        update = datetime.now()

        # this ensures that the marker file is not too large
        sleep(0.1)
