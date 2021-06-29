import random
maxTicketsAvailable=int(input("Enter the total number of person:"))
m=[]
for i in range(maxTicketsAvailable):
    m.append(input("Enter one name:"))
n=random.randint(0,maxTicketsAvailable-1)
print("The winner of the lottery is:",m[n])

#OUTPUT
#Enter the total number of person:5
#Enter one name:deep
#Enter one name:kakashi
#Enter one name:asuma
#Enter one name:tobi
#Enter one name:obito
#The winner of the lottery is: obito