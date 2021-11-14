import unittest
import technicalTask


class testTechnicalTask(unittest.TestCase):
    # Unit Tests for Technical Task Functions.

    def test_findCityInstanceValue(self):
        # Create a mock city class to use for testing function:
        city = technicalTask.City("test_city", {"test":[{"test_metric":100}]})
        # Run function using mock city object
        result = technicalTask.findCityInstanceValue(city,"test",0,"test_metric")
        
        self.assertEqual(type(result), int)
        self.assertEqual(result, 100)


    def test_getCityMinimumDailyValue(self):
        # Create a mock city class to use for testing function:
        city = technicalTask.City("test_city", {"test":[{"test_metric":100}]})
        # Run function using mock city object
        result = technicalTask.getCityMinimumDailyValue(city, "test", "test_metric")
        
        self.assertEqual(type(result), int)
        self.assertEqual(result, 100)


    def test_getCityWeeklyMedianValue(self):
        # Create a mock city class to use for testing function:
        city = technicalTask.City("test_city", {"test":[{"test_metric":100}]})
        # Run function using mock city object
        result = technicalTask.getCityWeeklyMedianValue(city, "test_metric")
        
        self.assertEqual(type(result), int)
        self.assertEqual(result, 100)


    def test_getCityWeeklyMaximumValue(self):
        # Create a mock city class to use for testing function:
        city = technicalTask.City("test_city", {"test":[{"test_metric":100}]})
        # Run function using mock city object
        result = technicalTask.getCityWeeklyMaximumValue(city, "test_metric")
        
        self.assertEqual(type(result), int)
        self.assertEqual(result, 100)


    def test_findCityWithHighestValue(self):
        # Create a mock City classes to use for testing function:
        cities = [] 
        cities.append(technicalTask.City("test_city1", {"test":[{"test_metric":100}]}))
        cities.append(technicalTask.City("test_city2", {"test":[{"test_metric":80}]}))
        cities.append(technicalTask.City("test_city3", {"test":[{"test_metric":50}]}))
        # Run function using mock city object
        result = technicalTask.findCityWithHighestValue(cities, "test_metric")

        self.assertEqual(type(result), str)
        self.assertEqual(result, "test_city1")
        

    def test_minimumpressureCheck(self):
        # Create a mock city class to use for testing function:
        city = technicalTask.City("test_city", {"test":[{"pressure":100}]})
        # Run function using mock city object
        result = technicalTask.minimumPressureCheck(city, "test")
        
        self.assertTrue(result)
      

    def test_willItSnow(self):
        # Create a mock city class in a list to use for testing function:
        cities = [] 
        cities.append(technicalTask.City("test_city", {"test":[{"precipitation":100, "temperature":0}]}))
        # Run function using mock city object
        result = technicalTask.willItSnow(cities)
        
        self.assertTrue(result)


    def test_getCityFromList(self):
        # Create a mock City classes to use for testing function:
        cities = [] 
        cities.append(technicalTask.City("test_city1", {"test":[{"test_metric":100}]}))
        cities.append(technicalTask.City("test_city2", {"test":[{"test_metric":80}]}))
        cities.append(technicalTask.City("test_city3", {"test":[{"test_metric":50}]}))
        # Run function using mock city object
        result = technicalTask.getCityFromList(cities, "test_city1")

        self.assertEqual(type(result), technicalTask.City)
        self.assertEqual(result.weather["test"][0]["test_metric"], 100)
    

if __name__ == "__main__":
    unittest.main()
