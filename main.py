from wind_forecast_provider import Wind_Forecast_Provider

windfinder = Wind_Forecast_Provider("WindFinder")


print(windfinder.get_provider_description())

windfinder.display_windforecast("Zeebrugges")
