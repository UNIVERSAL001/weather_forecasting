import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import requests

latitude = 38.8986
longitude = 66.0464

# Get the data from the API

url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
response = requests.get(url)
data = response.json()
plt.figure(dpi=150)
#plot data in a graph using scatter plot
plt.title("Temperature in Qashqadaryo")
plt.xlabel("Time")
plt.ylabel("Temperature")
x = pd.Series((data["hourly"]["time"])[:25])
y = pd.Series((data["hourly"]["temperature_2m"])[:25])
plt.plot(x,y,color="blue")
# plt.plot(data["hourly"]["time"], data["hourly"]["temperature_2m"],color="blue")
# plt.scatter(data["hourly"]["time"], data["hourly"]["temperature_2m"],marker="o",color="red")

plt.xticks(rotation=90)
plt.show()
# print(data)