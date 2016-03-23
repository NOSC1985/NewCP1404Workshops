from random import random

TITLE = "Gopher Population Simulator"

initial_population = 1000
lowest_percent_population_increase = 10
highest_percent_population_increase = 20
lowest_percent_population_decrease = 5
highest_percent_population_decrease = 25

print("Welcome to the {}!\nStarting Population: {}\n\n".format(TITLE, initial_population))
population = initial_population
for i in (1, 11, 1):
    percentage_increaser = random(lowest_percent_population_increase, highest_percent_population_increase)/100
    births = population * percentage_increaser
    percentage_decreaser = random(lowest_percent_population_decrease, highest_percent_population_decrease)/100
    deaths = population * percentage_decreaser
    population = population + births - deaths
    print("Year {0}\n*****\n{1} gophers were born. {2} died\nPopulation: {3}".format(i, births, deaths, population))