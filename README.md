# Simulation of Fresnel Diffraction by an Opaque Disc

### The Poisson–Arago Spot

A computational physics project that simulates Fresnel diffraction produced by an opaque circular disc using Python.

## Project Overview

The Poisson–Arago spot is a bright spot that appears at the centre of the geometrical shadow of an opaque circular disc due to the wave nature of light.

This project numerically simulates the diffraction pattern and visualizes the central bright spot and surrounding intensity distribution.

## Technologies Used

- Python
- NumPy
- Matplotlib

## Numerical Method

The simulation implements the Angular Spectrum Method using 2D Fast Fourier Transforms (FFT) to model free-space wave propagation.

## Simulation Parameters

- Wavelength: 632.8 nm
- Opaque disc radius: 1.0 mm
- Propagation distance: 1.0 m
- Grid resolution: 4096 × 4096

## Features

- Numerical simulation of light propagation.
- 2D diffraction intensity visualization.
- 1D central intensity profile.
- Visualization of the Poisson–Arago spot.

## Installation and Execution

1. Clone this repository:

   git clone https://github.com/YOUR-USERNAME/fresnel-diffraction-opaque-disc-simulation.git

2. Navigate to the project directory:

   cd fresnel-diffraction-opaque-disc-simulation

3. Install dependencies:

   pip install -r requirements.txt

4. Run the simulation:

   python opaque_disc.py

## Team

This project was collaboratively developed as part of the EP2102: Optics & Lasers course at IIT Patna.

- Akshara Karri
- Varkatam Akshaya
- Badavath Madhulatha
- Tejeswin R

## Acknowledgement

An academic project exploring the connection between wave optics and computational programming.
