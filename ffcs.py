import csv


n=int(input("How many courses you want to opt for?\n"))
courses=[]
for i in range (n):
    temp=input("Enter your course code for course number %d\n" %(i+1))
    courses.append(temp)

with open("Book1.csv", "r") as file:
    lst=[]
    reqd_lst=[]
    final_lst=[]
    reader=csv.reader(file)
    for line in reader:
        lst.append(line)
    for i in lst:
        for e in courses:
            if (i[0]==e):
                reqd_lst.append(i)
    for k in reqd_lst:
        count=0
        temp_slots2=[]
        temp_slots=k[3].split('+')
        for e in final_lst:
            if (e[0]==k[0]):
                count+=1
        for f in final_lst:
            temp_slots2=f[3].split('+')
        for x in temp_slots:
            for y in temp_slots2:
                if (x==y):
                    count+=1
        if (count>0):
            continue
        else:
            final_lst.append(k)
print('Your should opt these teachers with the following slots:')
for z in final_lst:
    print(z)
            
