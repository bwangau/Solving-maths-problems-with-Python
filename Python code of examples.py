'''
The following coding examples were prepared for 
Creating an engaging mathematics classroom through programming
presented by Robin Wang at MAV 2021
'''

#pattern, sequence, and series
'''
#Q8
a=[1/((i+1)*(i+2)) for i in range(99)]
print('The sum is:', sum(a))
'''

'''
#Q10
def fac(x):
    if x==0:
        return 1
    else:
        return x*fac(x-1)
a=[(i+1)*fac(i+1) for i in range(9)]
print('The sum is:', sum(a))
'''

#probability
'''
#Q10
import random
n=1000
list_count=[]
for i in range(n):
    list_toss=[]
    count = 0
    while list_toss.count(1)<3:
        a=random.randint(1,2)
        list_toss.append(a)
        count += 1
    list_count.append(count)
ave = sum(list_count)/n
print('The average number of tosses is: {}'.format(ave))
'''

'''
#Q10 Extension A
import random
n=1000
list_count=[]
for i in range(n):
    list_toss=[random.randint(1,2) for i in range(3)]
    count = 3
    while list_toss[-3::]!=[1,1,1]: 
        a=random.randint(1,2)
        list_toss.append(a)
        count += 1
    list_count.append(count)
ave = sum(list_count)/n
print('The average number of tosses is: {}'.format(ave))
'''

'''
#Q19 Monty Hall
import random
a=[1,1,2] # 2 is the target
n=1000
c1=0
c2=0
for _ in range(n):
    random.shuffle(a)
    aa=a.copy() #non-switching case
    if aa[0]==2:
        c1 += 1
    else:
        c2 += 1 #switching case
print('The probability of non-switching is: {}%, {}/{}'.format(c1/n*100, c1, n))
print('The probability of switching is: {}%, {}/{}'.format(c2/n*100, c2, n))
'''

'''
#Q22
import random
def awin():
    if random.random()<3/8:
        return 1
    else:
        return 0
def bwin():
    if random.random()>3/8:
        return 1
    else:
        return 0
n=int(input('Enter the number of runs:')) #type in a number after the prompt
win = 0
list_all=[]
j=0 #initialise the number of shots in the 0th game
for i in range(n):
    list_all.append(j)
    j=0 #number of shots
    while True:
        a=awin()
        j+=1
        if a==1:
            win += 1
            break
        b=bwin()
        j+=1
        if b==1:
            break
print('The probability that Honda wins the games is: {}%, {}/{}'.
      format(win/n*100, win, n))
print('The average number of throws per game is: {}'.
      format(sum(list_all)/(n-1)))
'''

'''
#relations
#Q2 
def Ackermann(k, n):
    if k==0:
        return n+1
    if n==0:
        return Ackermann(k-1, 1)
    else:
        return Ackermann(k-1, Ackermann(k, n-1))
print(Ackermann(2,2))
'''