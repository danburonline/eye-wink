"""File to recording new experiments to collect data for the classifier"""
import asyncio
import csv
from datetime import datetime
import subprocess
import os
from idun_guardian_client_beta import GuardianClient

os.system("clear")

# Search for device and get device address
bci = GuardianClient()
bci.address = asyncio.run(bci.search_device())

# Input check battery level
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
check_battery = input(
    "Check battery level?         \ny=yes, n=no                                   "
)

# Display battery level
if check_battery == "y":

    # Check battery
    asyncio.run(bci.start_battery())


# Impedance check
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
check_impedance = input("Press ENTER to display impedance\n")

IMPEDANCE_DURATION = 5  # Duration of impedance measurement in seconds
MAINS_FREQUENCY_60HZ = False
# Main frequency in Hz (50 or 60), for Europe 50Hz, for US 60Hz

# Display impedance values
asyncio.run(
    bci.start_impedance(
        impedance_display_time=IMPEDANCE_DURATION, mains_freq_60hz=MAINS_FREQUENCY_60HZ
    )
)

# Check recording types
print("\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\nIDUN*IDUN*IDUN*IDUN*IDUN*IDUN\n")
recording_type = input(
    "Select the type of recording \n1=sleep, 2=daytime, 3=eyes o&c, 4=winking left-right"
)

# Sleep recording
if recording_type == "1":

    # Define variables
    EXPERIMENT: str = "Sleep"  # Name of the experiment
    RECORDING_TIMER: int = 36000  # Recording timer in seconds
    LED_SLEEP: bool = True  # True will turn off the LED on the earbud during recording

    # get some information about the recording and save it to csv
    with open(
        "info_sleep_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv",
        "w",
        newline="",
    ) as csvfile:
        writer = csv.writer(csvfile)
        FILLING = True
        while FILLING:
            impedance = input("\nImpedance:                                    ")
            environment = input("\nTesting Environment:                          ")
            comfort = input(
                "\nComfort of the device \n(1-10; 1=painful, 10=very comfortable):       "
            )

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            FILLING = False

    # Get enter key press
    wait_for_input = input("\nPress Enter When You Are Ready To Go To Sleep\n")

    # get starting timestamp
    start = datetime.now()
    update = datetime.now()

    # Marker name
    MARKER = "going_to_sleep"

    # Check key press and store marker timestamp
    with open(
        "markers_sleep_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv", "w"
    ) as f:

        FILLING = True
        while FILLING:
            MARKER = "going_to_sleep"

            writer = csv.writer(f)
            writer.writerow([update.timestamp(), MARKER])

            print("\n\n* * * * * * * * * *")
            print("HAVE A GOOD NIGHT !")
            print("* * * * * * * * * *\n\n")

            FILLING = False

    # Start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        )
    )


# Daytime recording
elif recording_type == "2":

    # Define variables
    EXPERIMENT: str = "Daytime long-term"  # Name of the experiment
    RECORDING_TIMER: int = 36000  # Recording timer in seconds
    LED_SLEEP: bool = True  # True will turn off the LED on the earbud during recording

    # Get some information about the recording and save it to csv
    with open(
        "info_daytime_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv",
        "w",
        newline="",
    ) as csvfile:
        writer = csv.writer(csvfile)
        FILLING = True
        while FILLING:
            impedance = input("\nImpedance:                                    ")
            environment = input("\nTesting Environment:                          ")
            comfort = input(
                "\nComfort of the device \n(1-10; 1=painful, 10=very comfortable):       "
            )

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            FILLING = False

    # Start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        )
    )


# EOEC recording
elif recording_type == "3":

    # Define variables
    EXPERIMENT: str = "EOEC"  # name of the experiment
    RECORDING_TIMER: int = 135  # recording timer in seconds
    LED_SLEEP: bool = False  # True will turn off the LED on the earbud during recording

    # Get some information about the recording and save it to csv
    with open(
        "info_eoec_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv",
        "w",
        newline="",
    ) as csvfile:
        writer = csv.writer(csvfile)
        FILLING = True
        while FILLING:
            impedance = input("\nImpedance:                                    ")
            environment = input("\nTesting Environment:                          ")
            comfort = input(
                "\nComfort of the device \n(1-10; 1=painful, 10=very comfortable):       "
            )
            keypress = input(
                "\nMake sure your speakers are on! Press Enter to start...\n"
            )

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            FILLING = False

    # Start subprocess (the actual experiment script)
    p = subprocess.Popen(["python", "alpha_markers.py"], shell=False)

    # Start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        )
    )

    # Terminate subprocess
    p.kill()


# Winking recording
elif recording_type == "4":

    # Define variables
    EXPERIMENT: str = "winking"  # Name of the experiment
    RECORDING_TIMER: int = 125  # Recording timer in seconds
    LED_SLEEP: bool = False  # True will turn off the LED on the earbud during recording

    # Get some information about the recording and save it to csv
    with open(
        "info_winking_" + datetime.now().strftime("%d%m%Y_%H%M%S") + ".csv",
        "w",
        newline="",
    ) as csvfile:
        writer = csv.writer(csvfile)
        FILLING = True
        while FILLING:
            impedance = input("\nImpedance:                                    ")
            environment = input("\nTesting Environment:                          ")
            comfort = input(
                "\nComfort of the device \n(1-10; 1=painful, 10=very comfortable):       "
            )
            keypress = input(
                "\nMake sure your speakers are on! Press Enter to start...\n"
            )

            writer.writerow(["Experiment", EXPERIMENT])
            writer.writerow(["Set Recording Duration", RECORDING_TIMER])
            writer.writerow(["LED Sleep Mode", str(LED_SLEEP)])
            writer.writerow(["Impedance", impedance])
            writer.writerow(["Testing Environment", environment])
            writer.writerow(["Comfort Rating", comfort])
            FILLING = False

    # Start subprocess (the actual experiment script)
    p = subprocess.Popen(["python", "winking_markers.py"], shell=False)

    # Start a recording session
    asyncio.run(
        bci.start_recording(
            recording_timer=RECORDING_TIMER, led_sleep=LED_SLEEP, experiment=EXPERIMENT
        )
    )

    # Terminate subprocess
    p.kill()
