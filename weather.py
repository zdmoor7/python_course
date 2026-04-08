import requests

response = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={"latitude": 51.5, "longitude": -0.12, "current_weather": True}
)

print(response.status_code)
print(response.json())