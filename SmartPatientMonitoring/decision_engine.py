def check_emergency(thumbs_up, voice_command):

    alerts = []

    if thumbs_up:
        alerts.append("HAND GESTURE DETECTED")

    if "help" in voice_command:
        alerts.append("PATIENT ASKED FOR HELP")

    if "doctor" in voice_command:
        alerts.append("NEED DOCTOR")

    if "water" in voice_command:
        alerts.append("NEED WATER")

    if alerts:
        return "EMERGENCY: " + ", ".join(alerts)

    return ""