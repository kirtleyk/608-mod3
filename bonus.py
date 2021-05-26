import statistics as stats 
from random import randint

data = list()  #create data list
for n in range(101): #create 100 random numbers between 1-1000 and add to the list 
    data.append(randint(1, 1000))
    
data = sorted(data) #sort data for easier viewing

print(f'Data Values: ', data, '\n')
print(f'Variance: {stats.variance(data)}')
print(f'Deviation: {stats.stdev(data)}', '\n')

print(f'Population Variance: {stats.pvariance(data)}')
print(f'Population Deviation: {stats.pstdev(data)}', '\n')