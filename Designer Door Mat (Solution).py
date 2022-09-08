ip_list=input().split()
#converting str-to-int
for i in range(0,2):
    ip_list[i]=int(ip_list[i])
N=ip_list[0]
M=ip_list[1]
#initializing required variables
pattern_base=".|."
pattern_change=".|..|."
n=N//2
#applying Variable-Constraints
if (5<N and N<101) and (15<M and M<303):
    if (N%2!=0 and N*3==M):
        #upper-Body
        #first-line
        print(pattern_base.center(M,"-"))
        #second-line To Mid-Body
        for l in range(1,n):
            print((pattern_base+(l*pattern_change)).center(M,"-"))
        #Mid-Body
        print("WELCOME".center(M,"-"))
        #Mid-Body to Second last line
        for m in range(1,n):
            k=n-m
            print((pattern_base+(k*pattern_change)).center(M,"-"))
        #last-line
        print(pattern_base.center(M,"-"))    
            

            

            
        