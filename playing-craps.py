from random import Random, randrange

# create list that will hold totals of the die rolls
face_totals = [0,0,0,0,0,0,0,0,0,0,0,0]

def roll():
    # calculate random die roll total
    die_roll_total = randrange(1,7) + randrange(1,7)
    #increment the value for the face value based on the list position
    face_totals[die_roll_total-1] += 1
    return die_roll_total

# Set total rows and roll the dice that many times
roll_total = 1000000
for x in range(1,roll_total+1): roll()
 
# display the die roll totals calculated and stored in each position of the list  
for index in range(len(face_totals)):
    print(f'Face value total {index+1}: {face_totals[index]}')
    
craps_percentage = (face_totals[1] + face_totals[2] + face_totals[11]) / roll_total * 100
win_percentage = (face_totals[6] + face_totals[10]) / roll_total * 100

print('\n')
print(f'Rolled Craps {craps_percentage:0.2f}% of the time!', '\n')
print(f'Won {win_percentage:0.2f}% of the time!', '\n')