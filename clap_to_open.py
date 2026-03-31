import subprocess
import time
import numpy as np
import pyaudio
from scipy.signal import butter, lfilter

SAMPLE_RATE = 44100
CHUNK = 2048
CHANNELS = 1
LOW_FREQ = 1400
HIGH_FREQ = 1800
MIN_RAW_VOLUME = 0.2
MIN_CLAP_GAP = 0.4
MAX_CLAP_GAP = 2.0

def bandpass_filter(data, low, high, fs, order=4):
    nyq = 0.5 * fs
    b, a = butter(order, [low / nyq, high / nyq], btype="band")
    return lfilter(b, a, data)

def open_everything():
    print("\n👏👏 Two claps! Launching...\n")
    subprocess.Popen(["open", "-a", "Claude"])
    time.sleep(0.5)
    safari_script = '''
    tell application "Safari"
        activate
        set the URL of document 1 to "https://classroom.google.com"
        delay 1
        tell window 1
            set newTab to make new tab
            set URL of newTab to "https://chatgpt.com"
            set current tab to newTab
        end tell
    end tell
    '''
    subprocess.run(["osascript", "-e", safari_script])

def listen():
    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paFloat32, channels=CHANNELS, rate=SAMPLE_RATE, input=True, frames_per_buffer=CHUNK)
    print("🎤 Listening — clap TWICE loudly! (Ctrl+C to quit)\n")
    clap_times = []
    last_clap = 0
    try:
        while True:
            raw = np.frombuffer(stream.read(CHUNK, exception_on_overflow=False), dtype=np.float32)
            peak_val = np.max(np.abs(raw))
            if peak_val < MIN_RAW_VOLUME:
                continue
            filt = bandpass_filter(raw, LOW_FREQ, HIGH_FREQ, SAMPLE_RATE)
            peak_filt = np.max(np.abs(filt))
            if peak_filt < 0.1:
                continue
            now = time.time()
            if now - last_clap < MIN_CLAP_GAP:
                continue
            last_clap = now
            clap_times.append(now)
            print(f"  👏 Clap {len(clap_times)}!")
            clap_times = [t for t in clap_times if now - t <= MAX_CLAP_GAP]
            if len(clap_times) >= 2:
                open_everything()
                clap_times = []
                last_clap = now + 2.0
                time.sleep(2.0)
    except KeyboardInterrupt:
        print("\nStopped!")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()

if __name__ == "__main__":
    listen()
