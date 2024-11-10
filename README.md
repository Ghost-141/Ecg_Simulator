# Ecg_Simulator

## Overview
This project presents a basic ECG Signal Simulator developed in Python, aimed at simulating normal ECG signals with variable beats per minute (BPM). ECG signal simulation is an essential tool for studying and understanding the distinct components of the signal and analyzing cardiac health. This simulator offers three different BPM rate options, allowing for flexible testing and analysis of ECG signal characteristics at various heart rates.

## Features
- **Three BPM Rate Options:** Generate ECG signals at three preset heart rates, simulating normal, slow, and fast heart rates.
- **Custom [`ecg_function`](./ecg_function.py):** Developed from a conference paper and inspired by the MATLAB code for ECG simulation available on the official website of MATLAB.
- **Python Implementation:** Accessible, easy-to-use Python code suitable for educational and research purposes.

## Purpose
Simulating ECG signals can be highly beneficial for:
- Understanding distinct components of a ECG signal(P,QRS,S,T,U waves).
- Research and analysis in cardiac health.

## Usage
Clone the repository and run the provided [`ecg_simulator`](./ecg_simulator.py) file and then select any of the predefined options to simulate ECG signals. This simulator can be modified to test additional BPM rates or other ECG parameters. However, generating more accurate graph can lead to more usage of ram.

## Acknowledgments
The `ecg_function` used in this simulator was inspired by concepts from a conference paper and references MATLAB's official ECG simulation code.
