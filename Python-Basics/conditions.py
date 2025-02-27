# maths = 50
 # kiswahili = 56
 #
 # if maths < kiswahili:
 #     print("maths is less than kiswahili")
 # elif maths > kiswahili:
 #     print("maths is greater than kiswahili")
 # else:
 #     print("maths is equals kiswahili")
 #
 # y = 7
# print(y)
 #
# product = y**2



# grading system conditions
maths = 60
eng = 76
kis = 89
geo = 66

# Calculate total marks and average
total = maths + eng + kis + geo
avg = total / 4

# Grading system based on average score
if 0 <= avg <= 39:
    print("The student's grade is: D")
# If the value of avg is greater than or equal to 0 and less than or equal to 39, then this condition is true.


elif 40 <= avg <= 59:
    print("The student's grade is: C")
# if the value of avg is greater than or equal to 40 and less than or equal to 59

elif 60 <= avg <= 79:
    print("The student's grade is: B")
# if the value of avg is greater than or equal to 60 and less than or equal to 79

elif 80 <= avg <= 100:
    print("The student's grade is: A")
# If the previous conditions were not true, and the value of avg is greater than or equal to 80 and less than or equal to 100,

else:
    print("Invalid average score")


