"""
Script to take an input wave file and plot the audio wave with matplotlib

Uses a sample_redux.wav file created in
"""
import wave
import matplotlib.pyplot as plt
import numpy as np

obj = wave.open("sample_redux.wav", "rb")

sample_freq = obj.getframerate()
n_samples = obj.getnframes()
signal_wave = obj.readframes(-1)

obj.close()

t_audio = n_samples / sample_freq

print(t_audio)

signal_array = np.frombuffer(signal_wave, dtype=np.int16)

times = np.linspace(0, t_audio, num=n_samples*2)  # modified by multiplying samples by 2 (channels?).

plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title("Audio Signal")
plt.ylabel("Signal wave")
plt.xlabel("Time (s)")
plt.xlim(0, t_audio)
plt.show()

