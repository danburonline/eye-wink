from idun_guardian_client_beta.igeb_api import GuardianAPI

api = GuardianAPI()

api.download_recording_by_id(
    device_id="F3-EB-85-A3-EB-B3",
    recording_id="bc3e0e7c-68c6-4917-80f1-3997b7f9b433",
)
