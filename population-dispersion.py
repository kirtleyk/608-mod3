import statistics as stats 

data = [1,3,4,2,6,5,3,4,5,2]

variance = stats.pvariance(data)

deviation = stats.pstdev(data)

print(f'Variance: {variance}')
print(f'Deviation: {deviation}')