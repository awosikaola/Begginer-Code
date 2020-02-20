score = float(input("Enter your score to know the grade: "))

if score >= 70:
    print('You got A')
elif score >= 60:
    print('You got B')
elif score >= 50:
    print('You got C')
elif score >= 45:
    print('You got D')
elif score >= 40:
    print('You got E')
else:
    print('You failed the course')