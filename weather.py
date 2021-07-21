import requests, json
api_key = "04c16fffd0b3818e44e63bc74403e6bd"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name

def weather(cityName="Deoghar"):

    city_name = cityName
    #city_name = input("Enter city name : ")

    # complete_url variable to store
    # complete url address
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name

    # get method of requests module
    # return response object
    response = requests.get(complete_url)

    # json method of response object
    # convert json format data into
    # python format data
    x = response.json()

    # Now x contains list of nested dictionaries
    # Check the value of "cod" key is equal to
    # "404", means city is found otherwise,
    # city is not found
    if x["cod"] != "404":

        # store the value of "main"
        # key in variable y
        y = x["main"]

        # store the value corresponding
        # to the "temp" key of y
        current_temperature = y["temp"] - 273.15

        # store the value corresponding
        # to the "pressure" key of y
        current_pressure = y["pressure"]

        # store the value corresponding
        # to the "humidity" key of y
        current_humidity = y["humidity"]

        # store the value of "weather"
        # key in variable z
        z = x["weather"]

        # store the value corresponding
        # to the "description" key at
        # the 0th index of z
        weather_description = z[0]["description"]

        # print following values
        print(" Temperature (in degree Celsius unit) = " + 
                str(current_temperature) +
                "\n atmospheric pressure (in hPa unit) = " +
                str(current_pressure) +
                "\n humidity (in percentage) = " +
                str(current_humidity) +
                "\n description = " +
                str(weather_description))
        return (current_temperature,current_pressure,current_humidity,weather_description)
    else: 
        print(" City Not Found ")
        return "City Not Found"
