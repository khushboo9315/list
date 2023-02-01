# l=[[0 for x in range(3)]for y in range(3)]
# print(l)

# a=[2,3,4,5]
# b=[0,9,0,7]
# print(a.count(0))
# print(b.count(0))

# a="khushi"
# a=list(a)
# print(a[(len(a)//2):-1])
# b=reverse.a[len(a)::]
# c=b.rever
# print(c)
# b=a[len(a)//2::]
# print(b)
# c=""
# d=c.join(reversed(b))
# print(len(d))
# print(d[0])
# print(d)

# a=1/2*1+1/2*0
# print((a**-1)% 998244353)

# a=int(input())-1
# max=int(input())
# s_max=0
# i=0
# while i<a:
#     b=int(input())
#     if b>max:
#         s_max=max
#         max=b
#     elif b>s_max:
#         s_max=b
#     i+=1
# print("second max is =", s_max)

a=int(input())
b=int(input())
if a/b<a//b:
    print(a//b+1)
else:
    print(a//b)

