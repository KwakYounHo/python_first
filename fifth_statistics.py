import pandas

house = pandas.read_csv('house.csv')

houseHead = house.head(2)

print(houseHead)

print(house.describe())