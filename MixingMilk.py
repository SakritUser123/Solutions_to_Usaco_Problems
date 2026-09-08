import sys 
sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

c1,m1 = map(int, input().split())
c2,m2 = map(int, input().split())
c3,m3 = map(int, input().split())

if(m1+m2<= c2):
    m2 += m1
    m1=0
else:
    m1 = abs(c2-(m1+m2))
    m2 = c2

for i in range(33):
    if(m2+m3<= c3):
        m3 += m2
        m2=0
    else:
        m2 = abs(c3-(m3+m2))
        m3 = c3

    if(m3+m1<= c1):
        m1 += m3
        m3=0
    else:
        m3 = abs(c1-(m3+m1))
        m1 = c1
    if(m1+m2<= c2):
        m2 += m1
        m1=0
    else:
        m1 = abs(c2-(m1+m2))
        m2 = c2
    

print(m1)
print(m2)
print(m3)
