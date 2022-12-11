"""This file is used to download a recording from the IDUN Guardian API"""
from idun_guardian_client_beta.igeb_api import GuardianAPI

api = GuardianAPI()

api.download_recording_by_id(
    device_id="F3-EB-85-A3-EB-B3",
    recording_id="58f6dd9d-a6ae-4d72-af80-040a84990e63",
)

api.download_recording_by_id(
    device_id="F3-EB-85-A3-EB-B3",
    recording_id="e8088821-0b73-4777-8f0d-d15a9ab8c48b",
)

api.download_recording_by_id(
    device_id="C4-D6-AF-AA-11-0D",
    recording_id="1694fa75-4bb0-4d81-853c-622d9775c416",
)

api.download_recording_by_id(
    device_id="F3-EB-85-A3-EB-B3",
    recording_id="52d79a12-ef57-43f0-a15e-7bc3b6bf6e91",
)

api.download_recording_by_id(
    device_id="C4-D6-AF-AA-11-0D",
    recording_id="bf741d00-aa91-41cb-956c-6dfe219233a6",
)

api.download_recording_by_id(
    device_id="C4-D6-AF-AA-11-0D",
    recording_id="422ad1ef-0095-49ba-96fb-fcd2580adb45",
)

api.download_recording_by_id(
    device_id="F3-EB-85-A3-EB-B3",
    recording_id="ba012f0e-f9cc-44a4-8d4f-90e4db2a74d3",
)

api.download_recording_by_id(
    device_id="F3-EB-85-A3-EB-B3",
    recording_id="b0b56ca9-da8e-4a91-a12c-1ef499f0aa48",
)
