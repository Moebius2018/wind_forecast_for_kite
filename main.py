from wind_forecast_provider import Wind_Forecast_Provider
from Openweather_wind_forecast import Wind_forecast_OW

#windfinder = Wind_Forecast_Provider("WindFinder")

#print(windfinder.get_provider_description())

#windfinder_forecast = windfinder.get_windforecast("")
#windfinder.display_windforecast()

#windfinder.display_windforecast_graph()


OW_wind_forecast = Wind_forecast_OW()

print(OW_wind_forecast.get_provider_description())

OW_wind_forecast.get_wind_forecast("zeebrugges")

OW_wind_forecast.display_windforecast()

OW_wind_forecast.display_windforecast_graph()