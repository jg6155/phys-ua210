import numpy as np
import matplotlib.pyplot as plt


piano_waveform = np.loadtxt('ps-8/piano.txt')
trumpet_waveform = np.loadtxt('ps-8/trumpet.txt')

plt.figure(figsize=(12, 6))
plt.plot(piano_waveform)
plt.title('Piano Waveform')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(trumpet_waveform)
plt.title('Trumpet Waveform')
plt.xlabel('Sample Number')
plt.ylabel('Amplitude')
plt.show()

from numpy.fft import fft

# calculate the discrete fourier transform for the piano waveform
piano_fft = fft(piano_waveform)

piano_magnitudes = np.abs(piano_fft)[:10000]

plt.figure(figsize=(12, 6))
plt.plot(piano_magnitudes)
plt.title('Magnitude of Piano Fourier Coefficients')
plt.xlabel('Coefficient Number')
plt.ylabel('Magnitude')
plt.show()

trumpet_fft = fft(trumpet_waveform)
trumpet_magnitudes = np.abs(trumpet_fft)[:10000]


plt.figure(figsize=(12, 6))
plt.plot(trumpet_magnitudes)
plt.title('Magnitude of Trumpet Fourier Coefficients')
plt.xlabel('Coefficient Number')
plt.ylabel('Magnitude')
plt.show()

def find_fundamental_frequency(fft_magnitudes, sample_rate=44100, waveform_length=None):
    length = waveform_length if waveform_length is not None else len(fft_magnitudes)

    #find the index of the maximum peak in the FFT magnitudes
    peak_index = np.argmax(fft_magnitudes)
    fundamental_frequency = (peak_index * sample_rate) / length
    return fundamental_frequency

piano_fnd_freq = find_fundamental_frequency(piano_magnitudes, 44100, len(piano_waveform))
trumpet_fnd_freq = find_fundamental_frequency(trumpet_magnitudes, 44100, len(trumpet_waveform))

print(piano_fnd_freq, trumpet_fnd_freq)

