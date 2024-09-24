def get_weather_report() -> str:
    """docstring"""
    weather: str = input("What is the weather?")
    if wetaher == "rainy" or weather == "cold":
        print("Bring a jacket")
    elif weather ==