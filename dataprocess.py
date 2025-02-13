import numpy as np
import matplotlib.pyplot as plt
import os

# using loadtxt()

#files choose load
# def hello():

#     print("Choose file to do data processing, 1, 2, 3, 4, 5, 6, 7")
#     choice = int(input("Enter value"))
#     names = ["02062025_SampleSilane5050aged_2.CSV", "02062025_SampleSilane5050aged_4.CSV",
#              "02062025_SampleSilane5050aged_8.CSV", "02062025_SampleSilane5050agedclean_2.CSV",
#              "02062025_SampleSilane5050agedwatermark_2.CSV", "02062025_SampleSilane5050NOTaged_2_128.CSV",
#              "02062025_SampleSilane5050NOTaged_4.CSV"]
#     file = names[choice-1]
    
#     return file

# Function to choose a file from a folder dynamically
def hello(folder_path):
    # Get a list of CSV files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith(".CSV")]

    if not files:
        print("No CSV files found in the folder.")
        return None

    # Display the available files with indices
    print("Choose a file to process:")
    for idx, file in enumerate(files, start=1):
        print(f"{idx}: {file}")

    # Get user input
    choice = int(input("Enter the number of the file: "))
    
    if 1 <= choice <= len(files):
        return os.path.join(folder_path, files[choice - 1])  # Return full file path
    else:
        print("Invalid choice.")
        return None


# Define the folder where CSV files are stored
folder = "C:/Users/Sean/OneDrive - Colorado School of Mines/Senior/Senior Spring/Senior_Design/Data from today"  # Change this to your actual folder path
# file_path = hello(folder)

data = np.loadtxt(hello(folder),
                 delimiter=",", dtype=float, skiprows=500, max_rows=3100)
plt.scatter(data[:, 0], data[:, 1], s=.5)
plt.xlabel("Wavenumber (1/cm)")
plt.ylabel("Absorbance")
plt.title("FTIR Spectra")
plt.show()