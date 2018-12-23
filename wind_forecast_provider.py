from datetime import datetime
from matplotlib import pyplot as nplt



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
            self.windforecast[start_date] = [20+i , 25+i]
        return self.windforecast

    def display_windforecast(self, spot):
        windforecast = self.get_windforecast(spot)
        for key, value in windforecast.items():
            print("date: " + key.strftime("%d/%m/%Y - %H"))
            print(' '*4 + "average wind speed: " + str(value[0]) + " knots")
            print(' '*4 + "gust wind speed: " + str(value[1]) + " knots")


    def display_windforecast(self,spot):
        #display forecazst on a graph

