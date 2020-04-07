import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sb

print(plt.style.available)
plt.style.use("bmh")

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

pearson_corr = data.corr("pearson")
kendall_corr = data.corr("kendall")
spearman_corr = data.corr("spearman")

ax = plt.axes()
sb.heatmap(pearson_corr,
            xticklabels=pearson_corr.columns,
            yticklabels=pearson_corr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5,
            ax=ax)
ax.set_title("Pearson Correlation Heat Map")

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# ax1.scatter(humidity, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
# ax1.set_xlabel("Humidity (%)")
# ax1.set_ylabel("Solar Radiation (W/mm$^2$)")
# ax1.set_title("Solar Radiation vs. Humidity")

ax1.scatter(temperature, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
ax1.set_xlabel("Temperature (F$^o$)")
ax1.set_ylabel("Solar Radiation (W/mm$^2$)")
ax1.set_title("Solar Radiation vs. Temperature")

ax2.scatter(pressure, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
ax2.set_xlabel("Pressure (Hg)")
ax2.set_ylabel("Solar Radiation (W/mm$^2$)")
ax2.set_title("Solar Radiation vs. Pressure")

# ax4.scatter(wind_direction, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
# ax4.set_xlabel("Wind Direction ($^o$)")
# ax4.set_ylabel("Solar Radiation (W/mm$^2$)")
# ax4.set_title("Solar Radiation vs. Wind Direction")

# ax4.scatter(wind_direction, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
# ax4.set_xlabel("Wind Direction ($^o$)")
# ax4.set_ylabel("Solar Radiation (W/mm$^2$)")
# ax4.set_title("Solar Radiation vs. Wind Direction")

plt.tight_layout()
plt.show()



