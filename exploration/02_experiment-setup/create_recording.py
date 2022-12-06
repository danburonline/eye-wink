import asyncio
from idun_guardian_client_beta import GuardianClient
import csv
from datetime import datetime
import subprocess
import os

# clear workspace
os.system('clear')
print("\n\n################################################\n### IDUN INTERNAL TESTING OF IGEB - nov 2022 ###\n################################################\n\n")



# # # # # # # # # SEARCH # # # # # # # # # # # # #

# get device address
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())



# # # # # # # # # BATTERY # # # # # # # # # # # # #

# input check battery level
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
check_battery = input("Check battery level?         \ny=yes, n=no                                   ")

# display battery level
if check_battery == "y":

    # check battery
    asyncio.run(bci.start_battery())



# # # # # # # # # IMPEDANCE # # # # # # # # # # # # #

# input check impedance
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
check_impedance = input("Press ENTER to display impedance\n")

IMPEDANCE_DURATION = 5  # duration of impedance measurement in seconds
MAINS_FREQUENCY_60Hz = False
# mains frequency in Hz (50 or 60), for Europe 50Hz, for US 60Hz

# display impedance
asyncio.run(
    bci.start_impedance(
        impedance_display_time=IMPEDANCE_DURATION,
        mains_freq_60hz=MAINS_FREQUENCY_60Hz)
)



# # # # # # # # # RECORDING # # # # # # # # # # # # #

# input select recording type
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
recording_type = input("Select the type of recording \n1=sleep, 2=daytime, 3=eyes open eyes closed, 4=winking left-right    ")

# sleep recording
if recording_type == "1":

    # define variables
    EXPERIMENT: str = "Sleep" # name of the experiment
    RECORDING_TIMER: int = 36000 # recording timer in seconds
    LED_SLEEP: bool = True # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open("info_sleep_"+datetime.now().strftime("%d%m%Y_%H%M%S")+".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        filling = True
        while filling:
            impedance =     input("\nImpedance:                                    ")
            environment =   input("\nTesting Environemnt:                          ")
            comfort =       input("\nComfort of the device \n(1-10; 1=painful, 10=very comfortable):       ")
            
            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            filling = False

    # get enter key press
    waitforinput = input("\nPress Enter When You Are Ready To Go To Sleep\n")

    # get starting timestamp
    start = datetime.now()
    update = datetime.now()

    # marker name
    marker = "going_to_sleep"

    # check key press and store marker timestamp
    with open('markers_sleep_'+datetime.now().strftime("%d%m%Y_%H%M%S")+".csv", "w") as f:

        filling = True
        while filling:
            marker =    "going_to_sleep"

            writer = csv.writer(f)
            writer.writerow([update.timestamp(), marker])

            print("\n\n* * * * * * * * * *")
            print("HAVE A GOOD NIGHT !")
            print("* * * * * * * * * *\n\n")

            filling = False

    # start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER,
            led_sleep=LED_SLEEP,
            experiment=EXPERIMENT
        )
    )


# daytime recording
elif recording_type == "2":

    # define variables
    EXPERIMENT: str = "Daytime Longterm" # name of the experiment
    RECORDING_TIMER: int = 36000 # recording timer in seconds
    LED_SLEEP: bool = True # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open("info_daytime_"+datetime.now().strftime("%d%m%Y_%H%M%S")+".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        filling = True
        while filling:
            impedance =     input("\nImpedance:                                    ")
            environment =   input("\nTesting Environemnt:                          ")
            comfort =       input("\nComfort of the device \n(1-10; 1=painful, 10=very comfortable):       ")
            
            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            filling = False

    # start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER,
            led_sleep=LED_SLEEP,
            experiment=EXPERIMENT
        )
    )


# eoec recording
elif recording_type == "3":

    # define variables
    EXPERIMENT: str = "EOEC" # name of the experiment
    RECORDING_TIMER: int = 135 # recording timer in seconds
    LED_SLEEP: bool = False # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open("info_eoec_"+datetime.now().strftime("%d%m%Y_%H%M%S")+".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        filling = True
        while filling:
            impedance =     input("\nImpedance:                                    ")
            environment =   input("\nTesting Environemnt:                          ")
            comfort =       input("\nComfort of the device \n(1-10; 1=painful, 10=very comfortable):       ")
            keypress =      input("\nMake sure your speakers are on! Press Enter to start...\n")

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            filling = False

    # start subprocess (the actual experiment script)
    p = subprocess.Popen(["python", "alpha_markers.py"], shell=False)

    # start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER,
            led_sleep=LED_SLEEP,
            experiment=EXPERIMENT
        )
    )

    # terminate subprocess
    p.kill()


# winking recording
elif recording_type == "4":

    # define variables
    EXPERIMENT: str = "winking" # name of the experiment
    RECORDING_TIMER: int = 125 # recording timer in seconds
    LED_SLEEP: bool = False # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open("info_winking_"+datetime.now().strftime("%d%m%Y_%H%M%S")+".csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        filling = True
        while filling:
            impedance =     input("\nImpedance:                                    ")
            environment =   input("\nTesting Environemnt:                          ")
            comfort =       input("\nComfort of the device \n(1-10; 1=painful, 10=very comfortable):       ")
            keypress =      input("\nMake sure your speakers are on! Press Enter to start...\n")

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            filling = False

    # start subprocess (the actual experiment script)
    p = subprocess.Popen(["python", "winking_markers.py"], shell=False)

    # start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER,
            led_sleep=LED_SLEEP,
            experiment=EXPERIMENT
        )
    )

    # terminate subprocess
    p.kill()

