#TASK 3

#defining the fahrenheit function
def fahrenheit(x):
        #adding 32 to each value to get the fahrenheit
        return x + 32

#defining the temperature in celsium list
temperature_c = [26,25,23,27,26,24,21]
#mapping the temperature in farenheit function
temperature_f = map(fahrenheit,temperature_c)
#printing the temperature in farenheit function
print temperature_f





