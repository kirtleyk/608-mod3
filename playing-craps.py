from random import randrange

# create list that will hold totals of the die rolls in each of 12 positions
face_totals = [0,0,0,0,0,0,0,0,0,0,0,0]

def roll():
    # calculate random die roll total
    die_roll_total = randrange(1,7) + randrange(1,7)
    #increment the count value for the face value rolled based on the list position
    face_totals[die_roll_total-1] += 1
    return die_roll_total

# Set total rolls and dice rolls
roll_total = 6000000
for x in range(1, roll_total+1): roll()
 
print(f'\nSimulating {roll_total} die rolls!', '\n')

# display the die roll totals calculated and stored in each position of the list  
print(f'Face {"Frequency":>13}')
for index in range(len(face_totals)): 
    print(f'{index+1:>4} {face_totals[index]:>13}')
    
craps_percentage = (face_totals[1] + face_totals[2] + face_totals[11]) / roll_total * 100
win_percentage = (face_totals[6] + face_totals[10]) / roll_total * 100

print(f'\nCraps {craps_percentage:0.2f}% of the time!')
print(f'\n{"Win":>5} {win_percentage:0.2f}% of the time!', '\n')