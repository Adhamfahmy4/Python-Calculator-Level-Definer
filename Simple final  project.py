#Checking Grade
print ("Enter marks obtained in 5 subjects: ")
mark1= int(input())
mark2= int(input())
mark3= int(input())
mark4= int(input())
mark5= int(input())

tot = mark1+mark2+mark3+mark4+mark5
avg = tot/5
x=0
gradelist=[0,10,20,30,40,50,60,70,80,90,100]
ranklist=["E2", "E1", "D2", "D1", "C2", "C1", "B2", "B1", "A2", "A1"]

for i in range(len(gradelist)-1):
    if avg>gradelist[x+1]:
        x+=1
    elif avg>=gradelist[x] and avg<=gradelist[x+1]:
        pass
print("Your Grade is", ranklist[x])
