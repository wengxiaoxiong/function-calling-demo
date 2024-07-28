def get_current_weather(location, format):
    """
    Mock function to get the current weather for a given location.

    :param location: The city and state, e.g. San Francisco, CA
    :param format: The temperature unit to use. Either 'celsius' or 'fahrenheit'
    :return: A mock dictionary representing current weather data
    """
    mock_weather_data = {
        "location": location,
        "temperature": 22 if format == "celsius" else 72,
        "unit": format,
        "description": "Sunny"
    }
    return mock_weather_data


def get_n_day_weather_forecast(location, format, num_days):
    """
    Mock function to get a N-day weather forecast for a given location.

    :param location: The city and state, e.g. San Francisco, CA
    :param format: The temperature unit to use. Either 'celsius' or 'fahrenheit'
    :param num_days: The number of days to forecast
    :return: A mock list of dictionaries representing weather data for the next N days
    """
    mock_forecast_data = []
    for day in range(num_days):
        mock_forecast_data.append({
            "day": day + 1,
            "location": location,
            "temperature": 20 + day if format == "celsius" else 68 + day,
            "unit": format,
            "description": "Partly Cloudy" if day % 2 == 0 else "Sunny"
        })
    return mock_forecast_data


# Example usage
if __name__ == "__main__":
    print(get_current_weather("San Francisco, CA", "celsius"))
    print(get_n_day_weather_forecast("San Francisco, CA", "fahrenheit", 5))