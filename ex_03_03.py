#3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.


score = input ("enter score: ")

try:
    iscore = float(score)
except:
    iscore = -1

if iscore < 0.6 and iscore > 0.0:
    print('F')
elif iscore >= 0.7 and iscore < 0.8:
    print('C')
elif iscore >= 0.8 and iscore < 0.9:
    print('B')
elif iscore >= 0.9 and iscore < 1.0:
    print('A')
else:
    print('Error, please enter value between 0.0 and 1.0')
quit()
