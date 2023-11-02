UserDays = int(input('Please enter how many days you recorded temperature for:\n'))
temps = []
def AveAndDays(temps):
    DAA = []
    ave = sum(temps)/len(temps)
    for t in temps:
        if t > ave:
            DAA.append(t)
    return len(DAA)    









for i in range(1, UserDays+1):
    userTemp  = int(input(f'Please enter the high for day {i}:\n'))
    temps.append(userTemp)
print('\n\n' + str(AveAndDays(temps)) + " days(s) above average")