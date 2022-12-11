"""This file is used to download a recording from the IDUN Guardian API"""
from idun_guardian_client_beta.igeb_api import GuardianAPI

api = GuardianAPI()

DEVICE_ID = "D4-32-62-7C-C6-7F"

api.download_recording_by_id(
    device_id=DEVICE_ID,
    recording_id="9447a739-6bfc-44f8-b74f-86d237403e11",
)
