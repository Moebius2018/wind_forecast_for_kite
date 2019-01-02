from wind_forecast_provider import Wind_Forecast_Provider

windfinder = Wind_Forecast_Provider("WindFinder")

print(windfinder.get_provider_description())

windfinder_forecast = windfinder.get_windforecast("")
windfinder.display_windforecast()

windfinder.display_windforecast_graph()
