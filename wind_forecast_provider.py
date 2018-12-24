from datetime import datetime
from matplotlib import pyplot as plt
from random import *



class Wind_Forecast_Provider():
    # generic class to retrieve wind forecast


    def __init__(self,name ):
        self.name = name
        self.windforecast = {}


    def get_provider_description(self):
        #return  a descritpion of the wind provider
        description = "Provider name is " + str(self.name)
        return description

    def get_windforecast(self, spot):
        #return windforecast for the provided spot
        #windforecast is structured as follow
        # - date in datetime  format
        # - list with corresponding:
        #   - average wind speed forecast in knots
        #   - gust wind speed forecast in knots
        #current_date = datetime.now().strftime('%Y-%m-%d %H')
        current_date = datetime.today()

        for i in range(0,24):
            start_date = datetime(current_date.year,current_date.month,current_date.day+1, i)
            x = randint(-10, 10)
            y = randint(-10,10)
            self.windforecast[start_date] = [12+x , 14+y]
        return self.windforecast

    def display_windforecast(self, windforecast):
        for key, value in windforecast.items():
            print("date: " + key.strftime("%d/%m/%Y - %H"))
            print(' '*4 + "average wind speed: " + str(value[0]) + " knots")
            print(' '*4 + "gust wind speed: " + str(value[1]) + " knots")

    def get_forecast_date_list(self, windforecast):
        date_list = []
        for key in windforecast.keys():
            date_list.append(key.strftime("%d/%m/%y - %H:00"))
        return date_list


    def get_forecast_average_wind_speed_list(self, windforecast):
        av_windspeed =[]
        for value in windforecast.values():
                av_windspeed.append(value[0])
        return av_windspeed

    def display_windforecast_graph(self, windforecast):
        #display forecast on a graph
        fig = plt.figure()
        x = self.get_forecast_date_list(windforecast)
        y=  self.get_forecast_average_wind_speed_list(windforecast)
        plt.plot(x , y)
        plt.ylabel('windspeed')
        fig.autofmt_xdate()
        plt.show()

