import sys
import requests
import json
import statistics

class City:
    def __init__(self, name, weather):
        self.name = name
        self.weather = weather

    def __str__(self):
        return f"{self.name}"


def getCityList( url):
    """
    Function to query the API and decode and proccess the JSON in the response
    to return a list containins the names all of cities in the API.
    Inputs:
        - url: String containing the URL of the API
    Outputs:
        - cities: List of string city names.
    """
    response = requests.get(url+"/cities")
    cities = json.loads(response.content)
    return cities["cities"]


def getCityWeatherData(candidateNumber, url, city):
    """
    Function used to query the weekly weather data for a single given city from the API and
    return a dictionary.
    Inputs:
        - candidateNumber: Int used to query a select dataset from the API.
        - url: String containing the URL of the API.
        - city: String name of the city for which the weather is queried.
    Outputs:
        - weather: Dictionary containing the weekly weather data for a city.
    """
    response = requests.get(url+"/weather/"+str(candidateNumber)+"/"+city)
    weather = json.loads(response.content)
    return weather


def getCities(candidateNumber, url):
    """
    Function to return a list of City objects for a given candidate number queried from the API.
    Inputs:
        - candidateNumber: string value of the supplied candidate number.
        - url: string value of the url of the API being queried.
    Outputs:
        - cities: list containing City objects.
    """
    cities = []
    cityList = getCityList(url)
    for city in cityList:
        cities.append(City(city, getCityWeatherData(candidateNumber, url, city)))
    return cities


def findCityInstanceValue(city, day, time, metric):
    """
    Function to return the value of a given metric in a specified city on a given day and time.
    Inputs:
        - city: city class object
        - day: string value of the day of the week being queried
        - time: int value of the time being day being queried
        - metric: String value of the metric being queried
    Outputs:
        - int value of the metric in the city at the given timeframe
    """
    return city.weather[day][time][metric]


def getCityMinimumDailyValue(city, day, metric):
    """
    Function to find the minimum value of a given metric in a city on a specific day
    Inputs:
        - city: City object
        - day: String value of the day being queried
        - metric: String value of the metric to be found
    Outputs:
        - Int value of the lowest value in the city on a given day.
    """
    metricData = [city.weather[day][hour][metric] for hour in range(len(city.weather[day]))]
    return min(metricData)


def getCityWeeklyMedianValue(city, metric):
    """
    Function to find the median value across the week for a given metric in a city.
    Input:
        - city: City object
        - metric: string value of the metric being investigated
    Output:
        - Int value of the median for the given metric.
    """
    metricData = []
    for day in city.weather:
        dailyValues = [city.weather[day][hour][metric] for hour in range(len(city.weather[day]))]
        metricData = metricData + dailyValues
    return int(statistics.median(metricData))


def getCityWeeklyMaximumValue(city, metric):
    """
    Function to find the maximum value recorded in a city for a given metric during the week.
    Input:
        - city: City class object
        - metric: String value of the metric being investigated
    Output:
        - Int value of the max value recorded over the week/
    """
    metricData = []
    for day in city.weather:
        dailyValues = [city.weather[day][hour][metric] for hour in range(len(city.weather[day]))]
        metricData = metricData + dailyValues
    return max(metricData)


def findCityWithHighestValue(cities, metric):
    """
    Function to find the city which has the highest recorded value for a given metric during the week.
    In the case that multiple cities share this maximum value, they are sorted alphabetically and the
    first value is returned.
    Inputs:
        - cities: List containing City objects.
        - metric: String value of the metric being investigated.
    Outputs:
        - String value of the first city alphabetically in which the highest value is recorded.
    """
    cityMaxList = []
    for city in cities:
        cityMax = getCityWeeklyMaximumValue(city, metric)
        cityMaxList.append((city.name,cityMax))
    weeklyMax = max(cityMaxList, key = lambda item:item[1])[1]
    citiesWithMax = []
    for city in cityMaxList:
        if city[1] == weeklyMax:
            citiesWithMax.append(city[0])
    return sorted(citiesWithMax)[0] # List of cities are sorted and the first alphabetically is returned.


def minimumPressureCheck (city, day):
    """
    Function to check for whether the minimum pressure recorded in a city on a given day will drop below
    1000 millibars.
    Inputs:
        - city: City object
        - day: string value of the day being checked
    Outputs:
        - Boolean, indicating whether the pressure drops below 1000 millibars (True) or not (False).
    """
    minimumPressure = getCityMinimumDailyValue(city, day, "pressure") # Function call to find daily minimum pressure
    if minimumPressure < 1000:
        return True
    else:
        return False


def willItSnow(cities):
    """
    Function to check each of the cities to determine if it is likely to snow at any point during the week.
    Inputs:
        - cities: List of City objects.
    Outputs:
        - willItSnow: Boolean value representing whether it is likely to snow
    """
    willItSnow = False
    for city in cities:
        # check each hour in each day to find any instance where precipitation > 0 and temperature < 2
        for day in city.weather:
            for hour in range(len(city.weather[day])):
                if city.weather[day][hour]["precipitation"]>1 and city.weather[day][hour]["temperature"]<2:
                    willItSnow = True
    return willItSnow


def getCityFromList (cities, name):
    """
    Function to reduce repeated code when obtianing city objects from list
    of cities
    Inputs:
        - cities: List of city objects
        - name: String value of the name of the desired city
    Outputs:
        - city: City object with the matching name
    """
    for city in cities:
        if city.name == name:
            return city
    # Exception Handling for if desired city cannot be found in data obtained from the API
    print("City with the desired name does not exist within the List")
    sys.exit(1)


if __name__ == "__main__":

    if len(sys.argv) < 3: # Check to make sure that both required commandline arguments have been supplied
        print("Please ensure that you provide both the Candidate number and save path"\
              " for the answers as input on the command line.")
        sys.exit(1)

    # Command-line arguments
    candidateNumber = sys.argv[1]
    dataFilePath = sys.argv[2]

    # API URL
    url = "http://weather-api.eba-jgjmjs6p.eu-west-2.elasticbeanstalk.com/api"

    cities = getCities(candidateNumber, url)

    # Processing of quesiton answers:
    q1 = findCityInstanceValue(getCityFromList(cities, "bath"), "wednesday", 10, "temperature")
    q2 = minimumPressureCheck(getCityFromList(cities, "edinburgh"), "friday")
    q3 = getCityWeeklyMedianValue(getCityFromList(cities, "cardiff"), "temperature")
    q4 = findCityWithHighestValue(cities, "wind_speed")
    q5= willItSnow(cities)

    data = {}
    data["Answers"] = []
    data["Answers"].append({
        "Question 1": q1,
        "Question 2": q2,
        "Question 3": q3,
        "Question 4": q4,
        "Question 5": q5})
    with open(dataFilePath + "answers.txt", "w") as outfile:
        json.dump(data,outfile, indent=4) # Indent added for readability
