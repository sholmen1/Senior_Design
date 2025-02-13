import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pybaselines import polynomial, whittaker, optimizers
from dataprocess import hello

# Load the FTIR data
# Define the folder where CSV files are stored
folder = "C:/Users/Sean/OneDrive - Colorado School of Mines/Senior/Senior Spring/Senior_Design/Data from today"  # Change this to your actual folder path
file_path = hello(folder)

df = pd.read_csv(file_path, header=None)

#pybaselines is an online module for data processing for noise/background
# for high level physics devices/functions like FTIR
#

# Assume first column is Wavenumber and second is Absorbance
wavenumber = df.iloc[:, 0].values
absorbance = df.iloc[:, 1].values

# Filter data between 500 and 3800 cm⁻¹
mask = (wavenumber >= 700) & (wavenumber <= 3800)
wavenumber_filtered = wavenumber[mask]
absorbance_filtered = absorbance[mask]

# Plot original filtered data
plt.figure(figsize=(8, 5))
plt.plot(wavenumber_filtered, absorbance_filtered, label="Filtered Spectrum", color='blue')
plt.xlabel("Wavenumber (cm⁻¹)")
plt.ylabel("Absorbance")
plt.title("Filtered FTIR Spectrum")
plt.legend()
plt.gca().invert_xaxis()  # Invert x-axis for FTIR convention
plt.show()

# Apply polynomial baseline correction
degree = 3  # Adjust polynomial degree as needed
baseline, _ = polynomial.modpoly(absorbance_filtered, poly_order=degree)

# Subtract baseline
corrected_spectrum = absorbance_filtered - baseline

# Plot corrected spectrum
plt.figure(figsize=(8, 5))
plt.plot(wavenumber_filtered, corrected_spectrum, label="Baseline Corrected Spectrum", color='red')
plt.xlabel("Wavenumber (cm⁻¹)")
plt.ylabel("Absorbance")
plt.title("Baseline Corrected FTIR Spectrum (500-3800 cm⁻¹)")
plt.legend()
plt.gca().invert_xaxis()
plt.savefig(file_path.replace(".CSV", "_out1.jpeg"), dpi=600)
plt.show()


#apply arpls in whittaker #Note arpls returns a tuple need 1st element
whittakerr = whittaker.arpls(absorbance_filtered, lam=100000, x_data=wavenumber_filtered)

whittakerr = whittakerr[0]
corrected_spectrum2 = absorbance_filtered-whittakerr

# Plot corrected spectrum
plt.figure(figsize=(8, 5))
plt.plot(wavenumber_filtered, corrected_spectrum2, label="Baseline Corrected Spectrum", color='red')
plt.xlabel("Wavenumber (cm⁻¹)")
plt.ylabel("Absorbance")
plt.title("Baseline Corrected FTIR Spectrum (500-3800 cm⁻¹)")
plt.legend()
plt.gca().invert_xaxis()
plt.savefig(file_path.replace(".CSV", "_out2.jpeg"), dpi=600)
plt.show()


#apply adaptive_minmax or custom_bc in optimizer as framework for whittaker 
#default method modpoly #note that optimizer returns an tuple need to access first element

optimizer = optimizers.adaptive_minmax(absorbance_filtered, wavenumber_filtered)
optimizer=optimizer[0]
corrected_spectrum3 = absorbance_filtered-optimizer
# Plot corrected spectrum
plt.figure(figsize=(8, 5))
plt.plot(wavenumber_filtered, corrected_spectrum3, label="Baseline Corrected Spectrum", color='red')
plt.xlabel("Wavenumber (cm⁻¹)")
plt.ylabel("Absorbance")
plt.title("Baseline Corrected FTIR Spectrum (500-3800 cm⁻¹)")
plt.legend()
plt.gca().invert_xaxis()
plt.savefig(file_path.replace(".CSV", "_out3.jpeg"), dpi=600)
plt.show()

