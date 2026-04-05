# List of countries
countries = ['Wales', 'Denmark', 'Belgium', 'Japan', 'South Korea', 'South Africa', 'Indonesia', 'Singapore', 'Australia', 'India', 'Saudi Arabia', 'Mexico', 'Turkey', 'Greece', 'Netherlands', 'Finland', 'Monako', 'United Arab Emirates', 'Egypt', 'Morocco', 'Brazil', 'Argentina', 'Ireland', 'Portugal', 'Chile', 'Spain', 'Czech Republic', 'Sweden', 'Switzerland', 'Thailand', 'Luxemburg', 'New Zealand', 'France', 'Italy', 'Germany', 'China', 'Canada', 'Hungary', 'Scotland', 'Norway', 'Austria', 'Ukraine', 'Poland']

# List of countries you agreed to visit
your_travel_list = []
friend_travel_list = []

"""
# Testing
for i in range(0, len(countries), 2):
    your_travel_list.append(countries[i])

for i in range(1, len(countries), 2):
    friend_travel_list.append(countries[i])
"""

for i in range(len(countries)):
    if i % 2 == 0: # even number
        your_travel_list.append(countries[i])
    else:
        friend_travel_list.append(countries[i])
    
print(your_travel_list)
print(friend_travel_list)