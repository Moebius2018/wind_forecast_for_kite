from datetime import datetime
from matplotlib import pyplot as plt
from random import *
from wind_forecast import Wind_Forecast



class Wind_Forecast_Provider():
    # generic class to retrieve wind forecast


    def __init__(self,name ):
        self.name = name
       # self.windforecast = {}
        self.wind_forecast = Wind_Forecast()


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
            self.wind_forecast.date_list.append(datetime(current_date.year,current_date.month,current_date.day+1, i))
            #start_date = datetime(current_date.year,current_date.month,current_date.day+1, i)
            wind_speed = 15 + randint(-10, 15)
            self.wind_forecast.wind_average_list.append(wind_speed)
            self.wind_forecast.wind_gust_list.append(wind_speed + randint(0,8))
   #         x = randint(-10, 10)
   #         y = randint(-10,10)
   #         self.windforecast[start_date] = [12+x , 14+y]
        return self.wind_forecast

    def display_windforecast(self):
        for i  in range(len(self.wind_forecast.date_list)):
            # print("date: " + key.strftime("%d/%m/%Y - %H"))
            # print(' '*4 + "average wind speed: " + str(value[0]) + " knots")
            # print(' '*4 + "gust wind speed: " + str(value[1]) + " knots")
            print("date: " + self.wind_forecast.date_list[i].strftime("%d/%m/%Y - %H") )
            print(' '*4 + "average wind speed: " + str(self.wind_forecast.wind_average_list[i]) + " knots")
            print(' '*4 + "gust wind speed: " + str(self.wind_forecast.wind_gust_list[i]) + " knots")


    def display_windforecast_graph(self):
        #display forecast on a graph
        fig = plt.figure()
        date = self.wind_forecast.date_list
        wind_speed=  self.wind_forecast.wind_average_list
        gust_speed = self.wind_forecast.wind_gust_list
        plt.plot(date , wind_speed, c="blue")
        plt.plot(date, gust_speed, c="red")
        plt.ylabel('average windspeed and gust')
        fig.autofmt_xdate()
        plt.show()

