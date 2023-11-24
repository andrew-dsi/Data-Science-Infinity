####################################################
# Matplotlib - Scatter Plots
####################################################

import matplotlib.pyplot as plt
import pandas as pd

body_data = pd.read_csv("weights_and_heights.csv")

male = body_data[body_data["Gender"] == "Male"]
female = body_data[body_data["Gender"] == "Female"]

male_sample = male.sample(200, random_state = 42)

plt.style.use("seaborn-poster")
plt.scatter(male_sample["Weight"], male_sample["Height"], color = "blue", s = 700, alpha = 0.5)
plt.title("Weight vs. Height for Males")
plt.xlabel("Weight (lbs)")
plt.ylabel("Height (in)")
plt.axvline(x = male_sample["Weight"].median(), color = "black", linestyle = "--")
plt.axhline(y = male_sample["Height"].median(), color = "black", linestyle = "--")
plt.tight_layout()
plt.show()