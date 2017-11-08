class City:

    def __init__(self, passing_name = 'Unknown', pop = 0, gdp = 0):
        self.name = passing_name
        self.population = pop
        self.gdp_per_capita = gdp


    def __str__(self):
        return '{} has {} people, with gdp per capita ${}.'.format(self.name, self.population, self.gdp_per_capita)

    def __gt__(self, another_city):
        if self.gdp_per_capita > another_city.gdp_per_capita:
            return True
        elif self.gdp_per_capita == another_city.gdp_per_capita:
            if self.population < another_city.population:
                return True
        return False 
    
    def __add__(self, another_city):
        city = City()
        city.name = self.name +' ' + another_city.name
        city.population = self.population + another_city.population
        city.gdp_per_capita = (self.gdp_per_capita + another_city.gdp_per_capita)/2
        return city
    
    def __eq__(self, another_city):
        return self.population == another_city.population and self.gdp_per_capita == another_city.gdp_per_capita

city1 = City()

# print(city1.name, city1.population)

new_york = City('New York', 8500000, 75000)

# print(new_york.name, new_york.population, new_york.gdp_per_capita)

print(new_york)


boston = City('Boston', 600000, 75000)

print(boston)

print(new_york>boston)

print(new_york == boston)