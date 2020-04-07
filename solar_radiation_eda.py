import pandas as pd
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

data = pd.read_csv("data/SolarPrediction.csv")

print(data.columns)

unix_time = data["UNIXTime"]
date = data["Date"]
time = data["Time"]
temperature = data["Temperature"]
pressure = data["Pressure"]
humidity = data["Humidity"]
wind_direction = data["WindDirection(Degrees)"]
speed = data["Speed"]
time_sunrise = data["TimeSunRise"]
time_sunset = data["TimeSunSet"]
speed = data["Speed"]
radiation = data["Radiation"]

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()
fig4, ax4 = plt.subplots()

ax1.scatter(humidity, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
ax1.set_xlabel("Humidity (%)")
ax1.set_ylabel("Solar Radiation (W/mm$^2$)")
ax1.set_title("Solar Radiation vs. Humidity")

ax2.scatter(humidity, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
ax2.set_xlabel("Humidity (%)")
ax2.set_ylabel("Solar Radiation (W/mm$^2$)")
ax2.set_title("Solar Radiation vs. Humidity")

ax3.scatter(humidity, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
ax3.set_xlabel("Humidity (%)")
ax3.set_ylabel("Solar Radiation (W/mm$^2$)")
ax3.set_title("Solar Radiation vs. Humidity")

ax4.scatter(humidity, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
ax4.set_xlabel("Humidity (%)")
ax4.set_ylabel("Solar Radiation (W/mm$^2$)")
ax4.set_title("Solar Radiation vs. Humidity")

plt.tight_layout()
plt.show()



