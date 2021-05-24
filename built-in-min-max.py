
data1 = 12, 27, 36     
data2 = (12.3, 45.6, 9.7)
data3 = ('yellow', 'red', 'orange')  

print(f'The max value with max function using data1 {data1} is: {max(data1)}')
print(f'The max value with max function using data2 {data2} is: {max(data2)}')
print(f'The max value with max function using data3 {data3} is: {max(data3)}', '\n')

def calc_min(data):
    min_value=data[0]
    for val in data:
        if min_value > val:
            min_value = val        
    return min_value

data4 = (15, 9, 27, 14)
data5 = 'orange'
print(f'The min value with custom min function using data3 {data4} is: {calc_min(data4)}')
print(f'The min value with custom min function using data3 "{data5}" is: {calc_min(data5)}')
calc_min('orange')