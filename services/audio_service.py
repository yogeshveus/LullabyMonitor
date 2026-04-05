import sounddevice as sd
import soundfile as sf
import threading
import time
import os
from datetime import datetime

audio_on = True
monitoring = False
recording_thread = None

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def toggle_audio():
    global audio_on
    audio_on = not audio_on
    return audio_on


def get_audio_status():
    return audio_on


def is_monitoring():
    return monitoring


def record_audio_clip(duration=6, samplerate=44100):
    global audio_on

    if not audio_on:
        print("Microphone muted. Skipping recording.")
        return None

    print("Recording audio...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='int16')
    sd.wait()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(UPLOAD_FOLDER, f"audio_{timestamp}.wav")
    sf.write(filename, audio, samplerate)

    print(f"Saved: {filename}")

    return filename


def monitor_audio():
    global monitoring

    while monitoring:
        record_audio_clip(duration=6)
        print("Waiting for next cycle...")
        time.sleep(60)


def start_monitoring():
    global monitoring, recording_thread

    if not monitoring:
        monitoring = True
        recording_thread = threading.Thread(target=monitor_audio, daemon=True)
        recording_thread.start()
        return True
    return False


def stop_monitoring():
    global monitoring
    monitoring = False