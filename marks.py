print("Enter Marks Obtained in 5 Subjects: ")
ENGLISH = int(input())
MATHS = int(input())
HINDI = int(input())
SCIENCE = int(input())
HISTORY = int(input())

sum = int(ENGLISH) + int(HINDI) + int(MATHS) + int(HISTORY) + int(SCIENCE)

print("The sum is: ", sum)

per=float(sum)*(100/500)
print ("Percentage is: ",per)