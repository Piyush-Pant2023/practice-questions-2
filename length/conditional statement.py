marks=int(input("enter  student marks :"))
if(marks>=90):
    grade="a"

elif(marks>=80 and marks<=90):
    grade="b"
elif(marks>=70 and marks<=80):
    grade="d"
else:
    grade="e"
print("grade of the student ->",grade)

