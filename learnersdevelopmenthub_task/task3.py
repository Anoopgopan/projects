# Smart Student Stats - Name, Marks, Percentage! 

# Input student names and marks for 5 subjects, and 
# watch the magic unfold as we print their stats - Name, Total Marks, and Percentage! 

print(input("Enter the student name : "))
Subjects=["English","Tamil","Science","Maths","Social"]
t=[]
for i in Subjects:

    a=int(input("enter the marks"+" "+i+" : "))
    t.append(a)
print("Total Marks :",sum(t))
print("percentage :",(sum(t)/500)*100)