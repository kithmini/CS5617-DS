import pandas as pd
from matplotlib import pyplot as plt
from datetime import datetime
import seaborn as sb
import numpy as np

# GMT_TO_HONOLULU_CONVERSION = 0    # to demonstrate the bad effect of not pre-processing
GMT_TO_HONOLULU_CONVERSION = -10 * 3600 # to change time zone from GMT to Pacific/Honolulu

plt.style.use("bmh")

raw_data = pd.read_csv("data/SolarPrediction.csv")
data = raw_data.sort_values("UNIXTime")    # pre-processing

# print(data.head())
# print(data.columns)

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

utc_date = unix_time.apply(lambda x: datetime.utcfromtimestamp(int(x) - GMT_TO_HONOLULU_CONVERSION).strftime('%Y-%m-%d'))

dates = []
for index, row in data.iterrows():
    day = datetime.utcfromtimestamp(int(row["UNIXTime"]) - GMT_TO_HONOLULU_CONVERSION).strftime('%Y-%m-%d')
    if not day in dates:
        dates.append(day)
# print(dates)

# daily_radiation = dict.fromkeys(dates, list())    # create a single list and attach the ref to every dict key :(
daily_radiation = {}
for date in dates:
    daily_radiation[date] = list()
# print(daily_radiation)

for index, row in data.iterrows():
    day = datetime.utcfromtimestamp(int(row["UNIXTime"] - GMT_TO_HONOLULU_CONVERSION)).strftime('%Y-%m-%d')
    daily_radiation[day].append(row["Radiation"])
# print(daily_radiation)

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()
fig3, ax3 = plt.subplots()

# time_units_1 = np.arange(len(daily_radiation[dates[0]]))
# time_units_2 = np.arange(len(daily_radiation[dates[30]]))
# time_units_3 = np.arange(len(daily_radiation[dates[61]]))
# time_units_4 = np.arange(len(daily_radiation[dates[91]]))
# time_units_5 = np.arange(len(daily_radiation[dates[121]]))
# ax1.plot(time_units_1, daily_radiation[dates[0]], label=dates[0], color="green", linewidth="1", linestyle="solid")
# ax1.plot(time_units_2, daily_radiation[dates[30]], label=dates[30], color="red", linewidth="1", linestyle="solid")
# ax1.plot(time_units_3, daily_radiation[dates[61]], label=dates[61], color="blue", linewidth="1", linestyle="solid")
# ax1.plot(time_units_4, daily_radiation[dates[91]], label=dates[91], color="purple", linewidth="1", linestyle="solid")
# ax1.plot(time_units_5, daily_radiation[dates[121]], label=dates[121], color="black", linewidth="1", linestyle="solid")
time_units_1 = np.arange(len(daily_radiation[dates[1]]))
time_units_2 = np.arange(len(daily_radiation[dates[32]]))
time_units_3 = np.arange(len(daily_radiation[dates[61]]))
time_units_4 = np.arange(len(daily_radiation[dates[90]]))
time_units_5 = np.arange(len(daily_radiation[dates[117]]))
ax1.plot(time_units_1, daily_radiation[dates[1]], label=dates[1], color="green", linewidth="1", linestyle="solid")
ax1.plot(time_units_2, daily_radiation[dates[32]], label=dates[32], color="red", linewidth="1", linestyle="solid")
ax1.plot(time_units_3, daily_radiation[dates[61]], label=dates[61], color="blue", linewidth="1", linestyle="solid")
ax1.plot(time_units_4, daily_radiation[dates[90]], label=dates[90], color="purple", linewidth="1", linestyle="solid")
ax1.plot(time_units_5, daily_radiation[dates[117]], label=dates[117], color="black", linewidth="1", linestyle="solid")
ax1.set_xlabel("Time of day (5 min units)")
ax1.set_ylabel("Solar Radiation (W/mm$^2$)")
ax1.set_title("Solar Radiation vs. Time of day")
ax1.legend()

ax2.scatter(temperature, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
ax2.set_xlabel("Temperature (F$^o$)")
ax2.set_ylabel("Solar Radiation (W/mm$^2$)")
ax2.set_title("Solar Radiation vs. Temperature")

ax3.scatter(pressure, radiation, s=10, c="green", edgecolor="black", linewidth=0.5, alpha=0.4)
ax3.set_xlabel("Pressure (Hg)")
ax3.set_ylabel("Solar Radiation (W/mm$^2$)")
ax3.set_title("Solar Radiation vs. Pressure")

ax_corr = plt.axes()
sb.heatmap(pearson_corr,
            xticklabels=pearson_corr.columns,
            yticklabels=pearson_corr.columns,
            cmap='RdBu_r',
            annot=True,
            linewidth=0.5,
            ax=ax_corr)
ax_corr.set_title("Pearson Correlation Heat Map")

plt.tight_layout()
plt.show()



