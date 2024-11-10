import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Function definitions for each wave (P, Q, QRS, S, T, U) based on amplitude and duration
from ecg_function import p_wav, q_wav, qrs_wav, s_wav, t_wav, u_wav

# Set the range for time axis
x = np.arange(0.01, 3.0, 0.0001)

# Display welcome message
print("-------------Welcome to ECG Simulator----------------")

# Prompt the user to select a disease type
print("Select any disease from below:")
print("1. Sinus Rhythm at 70 BPM")
print("2. Sinus Rhythm at 78 BPM")
print("3. Sinus Rhythm at 120 BPM")

disease = input("Enter the number corresponding to the disease: ")

# Initialize parameters based on disease selection
if disease == "1":
    print("Sinus Rhythm at 70 BPM")
    li = 30 / 70
    a_pwav, d_pwav, t_pwav = 0.25, 0.09, 0.16
    a_qwav, d_qwav, t_qwav = 0.025, 0.066, 0.166
    a_qrswav, d_qrswav = 1.6, 0.11
    a_swav, d_swav, t_swav = 0.25, 0.066, 0.09
    a_twav, d_twav, t_twav = 0.35, 0.142, 0.2
    a_uwav, d_uwav, t_uwav = 0.035, 0.0476, 0.433
    name = "Sinus Rhythm at 70 BPM"

elif disease == "2":
    print("Sinus Rhythm at 78 BPM")
    li = 30 / 78
    a_pwav, d_pwav, t_pwav = 0.25, 0.09, 0.16
    a_qwav, d_qwav, t_qwav = 0.025, 0.066, 0.166
    a_qrswav, d_qrswav = 1.6, 0.11
    a_swav, d_swav, t_swav = 0.25, 0.066, 0.09
    a_twav, d_twav, t_twav = 0.35, 0.142, 0.2
    a_uwav, d_uwav, t_uwav = 0.035, 0.0476, 0.433
    name = "Sinus Rhythm at 78 BPM"

elif disease == "3":
    print("Sinus Rhythm at 120 BPM")
    li = 30 / 120
    a_pwav, d_pwav, t_pwav = 0.25, 0.09, 0.16
    a_qwav, d_qwav, t_qwav = 0.025, 0.066, 0.166
    a_qrswav, d_qrswav = 1.6, 0.11
    a_swav, d_swav, t_swav = 0.25, 0.066, 0.09
    a_twav, d_twav, t_twav = 0.35, 0.142, 0.2
    a_uwav, d_uwav, t_uwav = 0.035, 0.0476, 0.433
    name = "Sinus Rhythm at 120 BPM"

# Generate each wave using the provided wave functions
p_wav_res = p_wav(x, a_pwav, d_pwav, t_pwav, li)
q_wav_res = q_wav(x, a_qwav, d_qwav, t_qwav, li)
qrs_wav_res = qrs_wav(x, a_qrswav, d_qrswav, li)
s_wav_res = s_wav(x, a_swav, d_swav, t_swav, li)
t_wav_res = t_wav(x, a_twav, d_twav, t_twav, li)
u_wav_res = u_wav(x, a_uwav, d_uwav, t_uwav, li)

# Calculate the overall ECG signal as the sum of individual waves
ecg = p_wav_res + q_wav_res + qrs_wav_res + s_wav_res + t_wav_res + u_wav_res

# Set up the plot for animation
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, 5)
y_min, y_max = np.min(ecg), np.max(ecg)
ax.set_ylim(y_min - 0.2, y_max + 0.2) 
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.set_title(f"Generated ECG Signal of {name}")
line, = ax.plot([], [], lw=1.5)
plt.grid(which='both', linestyle='-', linewidth=0.5)
plt.minorticks_on()
plt.grid(which='minor', color='r', linestyle='-', alpha=0.5)
plt.grid(which='major', color='black', alpha=0.5)

# Initialize the plot
def init():
    line.set_data([], [])
    return line,

skip_points = 20 

def animate(i):
    line.set_data(x[:i*skip_points], ecg[:i*skip_points])  # Update line with progressive data up to index i * skip_points
    return line,

ani = FuncAnimation(
    fig, animate, init_func=init, frames=len(x)//skip_points, interval=10, blit=True
)

plt.show()
