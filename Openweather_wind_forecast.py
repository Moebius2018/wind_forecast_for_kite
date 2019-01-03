from wind_forecast_provider import Wind_Forecast_Provider
import requests
import datetime

class Wind_forecast_OW(Wind_Forecast_Provider):
    # 5 day forecast through API
    # more info on https://openweathermap.org/forecast5

    def __init__(self):
        super().__init__("Open Weather")
        self.url = "http://api.openweathermap.org/data/2.5/forecast?q=SPOT,belgium&APPID=7fc01188d26b1de192c786ee57d75bd9"
        #self.wind_forecast = Wind_Forecast()


    def get_wind_forecast(self, spot):
        url = self.url.replace("SPOT",spot)
        print(url)
        r = requests.get(self.url)
        response = r.json()
        wind_list = response["list"]
        for item in wind_list:
            date = datetime.datetime.fromtimestamp(item['dt'])
            speed = item["wind"]['speed'] * 1.94384
            self.wind_forecast.date_list.append(date)
            self.wind_forecast.wind_average_list.append(speed)
        return self.wind_forecast

