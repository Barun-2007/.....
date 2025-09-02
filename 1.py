# a = int(input())
# arr = list(map(int,input().split()))
# even=0
# odd=0
# for num in arr:
#     if(num % 2==0):
#         even+=1
#     else:
#         odd+=1
# if(even>odd):
#     print("READY FOR BATTLE")
# else:
#     print("NOT READY")

# a = int(input())
# i=0
# while i<a:
#     x,y,z= map(int,input().split())
#     if(x==0 and z==0):
#         print("Water filling time")
#     elif(x==0 and y==0):
#         print("Water filling time")
#     elif(y==0 and z==0):
#         print("Water filling time")
#     elif(x==0 and y==0 and z==0):
#         print("Water filling time")
#     else:
#         print("Not Now")
#     i+=1

# a = int(input())
# i=0
# while(i!=a):
#     x=int(input())
#     if(0<x<=100):
#         print(x)
#     elif(100<x<=1000):
#         k=x-25
#         print(k)
#     elif(1000<x<=5000):
#         k=x-100
#         print(k)
#     elif(5000<x):
#         k=x-500
#         print(k)
#     else:
#         print("Invalid input")
#     i+=1

# a = int(input())
# i=0
# while(i!=a):
#     x,y=map(int,input().split())
#     k=int(x*y)
#     m=(x*y)//4
#     if(k%4==0):
#         print(m)
#     else:
#         print(m+1)
#     i+=1

# a=int(input())
# i=0
# while(i<a):
#     b,c=map(int,input().split())
#     if(b==1):
#         print("",c)
#     elif(b%6==0):
#         k=((b//6)*c)
#         print("",k)
#     elif(b%6!=0):
#         k=((b//6)*c)+c
#         print("",k)
#     else:
#         print("Invalid input")
#     i+=1

# a=int(input())
# i=0
# while(i<a):
#     c=map(int,input().split())
#     if(0<c<8):
#         print("Yes")
#     elif(c>8):
#         print("No")
#     else:
#         print("Invalid input")
#     i+=1

#a=int(input())
# i=0
# while(i<a):
#     x,y,z=map(int,input().split())
#     k=(z/(x*y))*100
#     if(100>k>50):
#         print("Yes")
#     elif(0<=k<=50):
#         print("No")
#     else:
#         print("Invalid input")
#     i+=1

# a = int(input())
# i=0
# while(i!=a):
#     x,y,z,w=map(int,input().split())
#     if(x==0 and y==0 and z==0 and w==0):
#         print("IN")
#     else:
#         print("OUT")
#     i+=1

# a = int(input())
# i=0
# while(i!=a):
#     x,y=map(int,input().split())
#     if((y/x)>=0.5):
#         print("YES")
#     else:
#         print("NO")
#     i+=1

# c = int(input())
# i=0
# while(i!=c):
#     a,b,x,y=map(int,input().split())
#     k=(a*b)-(x*y)
#     if(k<=0):
#         print("Yes")
#     else:
#         print("No")
#     i+=1

# k = int(input())
# i=0
# while(i!=k):
#     a,b,c,d=map(int,input().split())
#     if(a>b+c<d or a+b+d<c or a+c+d<b or b+c+d<a):
#         print("Yes")
#     else:
#         print("No")
#     i+=1

# k = int(input())
# for i in range(k):
#     N=int(input())
#     D=list(map(int,input().split()))
#     count=0
#     for j in range(N):
#         if(D[j])>=1000:
#             count=count+1
#     i+=1
#     print(count)

# t=int(input())
# for i in range(t):
#     a,b,c=map(int,input().split())
#     if a<=b and b>=c:
#         print("yes")
#     else:
#         print("no")

# t=int(input())
# i=0
# while(i!=t):
#     a=int(input())
#     if (a<51):
#         print("LEFT")
#     else:
#         print("RIGHT")
#     i+=1
        
# t=int(input())
# for i in range(t):
#     n,x=map(int,input().split())
#     a=list(map(int,input().split()))
#     count=0
#     for j in range(n):
#         if(a[j]>=x):
#             count+=1
#         else:
#             pass
#         j+=1
#     i+=1
#     print(count)

# t=int(input())
# i=0
# while(i!=t):
#     n,x=map(int,input().split())
#     if(n>=x):
#         print(x)
#     else:;
#         print(n)

# for i in range(int(input())):
#     n, x =map(int, input().split())
#     if x!=n:
#         print(min(x, n-x))
#     else:
#         print(0)

# t=int(input())
# i=0
# def fact(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return (fact(n-1))*n
# while(i!=t):
#     x=int(input())
#     print(fact(x))
#     i+=1

# t=int(input())
# i=0
# while(i!=t):
#     x,y,z=map(int,input().split())
#     k=z-(y//x)
#     if(k>0):
#         print(k)
#     else:
#         print("0")
#     i+=1

# t=int(input())
# for i in range(t):
#     n=int(input())
#     s=input()
#     d={'A':'T', 'T':'A', 'C':'G','G':'C'}
#     l=''
#     for i in range(len(s)):
#         if s[i] in d:
#             l+=d[s[i]]
#     print(l)

# t=int(input())
# i=0
# while(i!=t):
#     n=int(input())
#     s=input()
#     k=''
#     for j in range(n):
#         if(s[j]=="A"):
#             k+="T"
#         elif(s[j]=="T"):
#             k+="A"
#         elif(s[j]=="C"):
#             k+="G"
#         elif(s[j]=="G"):
#             k+="C"
#     print(k)

# import math
# n=int(input())
# i=0
# while(i!=n):
#     a=int(input())
#     k=math.sqrt(a)
#     m=math.floor(k)
#     print(m)
#     i+=1

# n=int(input())
# i=0
# while(i!=n):
#     x,y,z=map(int,input().split())
#     k=x//3
#     m=x*y
#     l=m+k*z
#     t=m+(z*(k-1))
#     if((x%3)==0 ):
#         print(t)
#     else:
#         print(l)
#     i+=1

# n=int(input())
# i=0
# while(i!=n):
#     x,y=map(int,input().split())
#     k=x//y
#     s=x%y
#     if(x%y==0):
#         print(k)
#     else:
#         print(k+s)
#     i+=1

# def solve():
#     A, B, X, Y = map(int, input().split())
    
#     if A - Y <= B <= A + X:
#         print("YES")
#     else:
#         print("NO")

# T = int(input())
# for _ in range(T):
#     solve()

# x = int(input())
# i=0
# while(i!=x):    
#     a,b,c,d = map(int, input().split())
#     if(a==b or a==c or a==d or a==b+c or a==c+d or a==b+d or a==b+c+d):
#         print("YES")
#     else:
#         print("NO")
#     i+=1

# x = int(input())
# i=0
# while(i!=x):    
#     a,b,c,d = map(int, input().split())
#     k=a-b-c
#     if(k>=d):
#         print("0")
#     elif(k<d and d>c and d>b and d<=b+c):
#         print("2")
#     else:
#         print("1")
#     i+=1

# x = int(input())
# i=0
# while(i!=x):
#     a,b,c = map(int, input().split())
#     k=a//2
#     l=k*b+k*c
#     m=k*c+(k+1)*b
#     if(a==1):
#         print(b)
#     elif(a%2==0):
#         print(l)
#     else:
#         print(m)
#     i+=1

# x = int(input())
# i=0
# while(i!=x):
#     a,b= map(int, input().split())
#     k=b/100
#     l=b//100
#     m=b%100
#     if(l-a<0):
#         print("0")
#     elif(m==0):
#         print(l-a)
#     else:
#         print(l-a+1)
#     i+=1

# x = int(input())
# i=0
# while(i!=x):
#     a,b= map(int, input().split())
#     c=500-a*2
#     d=1000-4*(a+b)
#     e=500-(b+a)*2
#     f=1000-4*b
#     if(c+d>e+f):
#         print(c+d)
#     else:
#         print(e+f)
#     i+=1

# m = int(input())
# i=0
# while(i!=m):
#     a,b,x,y= map(int, input().split())
#     c=a/x
#     d=b/y
#     if(c>d):
#         print("CHEFINA")
#     elif(c==d):
#         print("BOTH")
#     else:
#         print("CHEF")
#     i+=1

# m = int(input())
# i=0
# while(i!=m):
#     x,y,r= map(int, input().split())
#     c=r//30
#     k=c+x
#     d=(k)//y
#     if(r==0 and x==y):
#         print("1")
#     elif(r==0 and x!=y and x%y!=0):
#         print(x//y+1)
#     elif(r==0 and x!=y and x%y==0):
#         print(x//y)
#     elif(k%y==0):
#         print(d)
#     else:
#         print(d+1)
#     i+=1

# m = int(input())
# i=0
# while(i!=m):
#     x= int(input())
#     c=x//7
#     if(x%7==1 or x%7==0):
#         print(c)
#     else:
#         print(c+1)
#     i+=1

# f=int(input())
# i=0
# while(i!=f):
#     a=0
#     b=0
#     n=int(input())
#     d=list(map(int,input().split()))
#     for j in range(n):
#         if(d[j]==1):
#             a+=1
#         elif(d[j]==-1):
#             b+=1
#         else:
#             pass
#     t=abs(a-b)
#     if(a%2==0 and b%2!=0):
#         print("-1")
#     elif(b%2==0 and a%2!=0):
#         print("-1")
#     elif(a==b):
#         print("0")
#     else:
#         print(t//2)
#     i+=1

# for i in range(int(input())):
#     n=int(input())
#     c=list(map(int,input().split()))
#     degree=0
#     for i in range(len(c)):
#         if c[i] != 0 and i>degree:
#             degree=i 
#     print(degree)

# def solve():
#     n = int(input())
#     player1_score = 0
#     player2_score = 0
#     max_lead = 0
#     winner = 0

#     for _ in range(n):
#         s1, s2 = map(int, input().split())
#         player1_score += s1
#         player2_score += s2

#         lead = player1_score - player2_score
#         abs_lead = abs(lead)

#         if abs_lead > max_lead:
#             max_lead = abs_lead
#             if lead > 0:
#                 winner = 1
#             else:
#                 winner = 2

#     print(winner, max_lead)

# solve()

# if __name__ == '__main__':
#     n = int(input())
#     l=[]
#     for i in range(1,n+1):
#         l.append(i)
#         k=''.join(map(str,l))  
#     print(k)

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     list=[]
#     list2=[]
#     for i in range(x+1):
#         for j in range(y+1):
#           for k in range(z+1):
#             if(i+j+k!=n):
#                 list2=[i,j,k]       
#                 list.append(list2)
#     print(list)

# if __name__ == '__main__':
#     n = int(input())
#     arr = map(int, input().split())
#     print(sorted(list(set(arr)))[-2])

# if __name__ == '__main__':
#     students = []
#     for _ in range(int(input())):
#         name = input()
#         grade = float(input())
#         students.append([name, grade])

# Extract all grades and find the second lowest
# grades = sorted(set([student[1] for student in students]))
# second_lowest_grade = grades[1]

# Find all students with the second lowest grade
# names_with_second_lowest = sorted([student[0] for student in students if student[1] == second_lowest_grade])

# # Print each name on a new line
# for name in names_with_second_lowest:
            #  print(name)

# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
    
#     # Get the scores of the queried student
#     query_scores = student_marks[query_name]
#     # Compute average
#     avg = sum(query_scores) / len(query_scores)
#     # Print with 2 decimal places
#     print(f"{avg:.2f}")

# if __name__ == '__main__':
#     N = int(input())
#     L=[];
#     for i in range(0,N):
#         cmd=input().split();
#         if cmd[0] == "insert":
#             L.insert(int(cmd[1]),int(cmd[2]))
#         elif cmd[0] == "append":
#             L.append(int(cmd[1]))
#         elif cmd[0] == "pop":
#             L.pop();
#         elif cmd[0] == "print":
#             print(L)
#         elif cmd[0] == "remove":
#             L.remove(int(cmd[1]))
#         elif cmd[0] == "sort":
#             L.sort();
#         else:
#             L.reverse();