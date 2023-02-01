''' find no is exist or not'''
# a=3
# x=1
# y=1
# b=1
# while x<=a:
#     print(b"|",end="")
#     y=1
#     while y<=a:
#         print(b,"__","|",end="")
#         y+=1
#     print()
#     x+=1
# print()
# b+=1
        
     
# a=1    
# x=[]
# n= int(input())
# while a<=n:
#     c=int(input())
#     x.append(c)
#     a+=1
# print(x)
# z=int(input())
# # b=0

# b=0
# while b<n:
#     if x[b]==z:
#         print(z,"exist at index no",x.index(z))
#         break
#     b+=1
# else:
#         print(z,"it doesnt exist")     
   
# a=1    
# x=[]
# n= int(input())
# while a<=n:
#     c=int(input())
#     x.append(c)
#     a+=1
# print(x)
# z=int(input())
# m=0
# b=0
# while b<n:
#     if x[b]==z:.....
#         m=1
#     b+=1
# if m==1:
#     print(z,"exist at index no",x.index(z))
# else:
#     print(z,"it doesnt exist")

##################################################################

# a=[2,5,7,4,9,1,5]
# x=0
# b=0
# while len(a)-1>=b:
#     max=a[b]
#     c=0 
#     while len(a)>=c:
#         if a[c]>max:
#             max=a[c]
#         c-=1
#     max[x],max[c]=max[c],max[x]
#     b-=1
#     x+=1
    
    #########################################################

# a=0
# g_l=['flour','cheese','carrots']
# while a<len(g_l):
#     print(a,':',g_l[a])
#     a+=1
# e=1
# a=4
# b=1
# while b<=a:
#     c=5
#     d=1
#     if b%2==0:
#         f=e+5
#         while d<=c:
#            print(f,end=" ")
#            f-=1
#     else:
#         print(e+1,end=" ")
        
#         d+=1
#         e+=1
        
#     print()
#     b+=1
        
# a=[10,5,2,3,7,8,9]
# for i in range(0,len(a)):
#     min=i
#     for j in range(i,len(a)):
#         if a[j]<a[min]:
#             min=a[j]
#     a[min],a[i]=a[i],a[min]
# print(a)
                #################sort
# a=[10,5,2,3,7,8,9]
# for i in range(0,len(a)):
#     min=i
#     for j in range(i,len(a)):
#         if a[j]<a[min]:
#             min=j
#     a[min],a[i]=a[i],a[min]
# print(a)

# 1............
# a=[2,3,7,9,5,1,8]
# b=[]
# c=len(a)-1
# while c>=0:
#     b.append(a[c])
#     c-=1
# print(b)


# a=int(input())
# b=[None]*a
# c=[None]*a
# n=0
# while n<a:
#    x=int(input())
#    b[n]=x
#    n+=1
# print(b)
# i=a-1
# j=0
# while i>=0:
#     c[j]=b[i]
#     i-=1
#     j+=1
# print(c)
    
#2...................
#mean
# a=[4,6,7,8,3,2,4]
# b=0
# c=0
# sum=0
# while b<len(a):
#     c+=1
#     sum+=a[b]
#     b+=1
# mean=sum//c
# print(mean)

#median................
# a=[1,2,3,4,5,6,7,8,9,10]
# for i in range(0,len(a)):
#     min=i
#     for j in range(i,len(a)):
#         if a[j]<a[min]:
#             min=j
#     a[min],a[i]=a[i],a[min]
# print(a)
# b=(len(a))
# c=b//2 
# if b%2==0:
#     median=(a[c-1]+a[c])/2
# else:
#     median=(a[c])
# print(median)
    
#mode............
# a=[2,5,4,6,7,3,2,5,4,2,2]
# for  i in range(a):
#     min=i
#     for j in range(i+1,a):
#         if a[j]<a[min]:
#             min=j
#     a[min],a[i]=a[i],a[j]
# print(a)


#########################################################
# i=0
# while i<n:
#     min=i
#     j=i
#     while j<n:
#         if a[j]<a[min]:
#             min=j
#         j+=1
#     a[min],a[i]=a[i],a[min]
#     i+=1
# print(a)
###################################################################
####################print mean medium mode withoyt inbuilt method#########

# n=int(input())
# a=[None]*n
# print(a)
# b=0
# while b<n:
#     c=0
#     x=int(input())
#     while c<=b:
#         a[b]=x
#         c+=1
#     b+=1
# print(a)
# # N=0
# # c=0
# # sum=0
# # while N<n:
# #     c+=1
# #     sum+=a[N]
# #     N+=1
# # mean=sum//n
# # print(mean)
# i=0
# while i<n:
#     min=i
#     j=i
#     while j<n:
#         if a[j]<a[min]:
#             min=j
#         j+=1
#     a[min],a[i]=a[i],a[min]
#     i+=1
# print(a)

# c=n//2
# if n%2==0:
#     median=(a[c-1]+a[c])/2
# else:
#     median=(a[c])
# print(median)

# mode=0
# for m in range(n):
#     x=0
#     for k in range(m+1,n):
#         if a[m]==a[k]:
#             x+=1
#     if x>0:
#         mode=a[m]
# print(mode)

##############    prime numbers using seive  ####################
# a=int(input())
# n=[0]*(a)
# for b in range(a):
#         n[b]=b+1
# print(n)
# for j in (n):
#     if j>1:
#        if j>2 and j%2==0:
#           continue
#        if j>3 and j%3==0:
#           continue
#        if j>5 and j%5==0:
#           continue
#        if j>7 and j%7==0:
#           continue
#        if j>11 and j%11==0:
#            continue
#        
#######################################################3        


#################################  find duplicate elements  ####################

'''ques:  4. Find duplicate elements in an array'''

# n=int(input())
# a=[None]*n
# x=0
# while x<n:
#     y=int(input())
#     a[x]=y
#     x+=1
# print(a)
# b=[]
# for i in range (n):
#     c=0
#     for j in range(i+1,n):
#         if a[i]==a[j]:
#             c+=1
#         else:
#             continue
#     if c==1:
#         b.append(a[i])
# print(b)
# ##############################   with while loop  #############
# n=int(input())
# a=[None]*n
# x=0
# while x<n:
#     y=int(input())
#     a[x]=y
#     x+=1
# print(a)
# b=[]
# i=0
# while i<n:
#     c=0
#     j=i+1
#     while j<n:
#         if a[i]==a[j]:
#             c+=1
#         else:
#             continue
#     if c==1:
#         b.append(a[i])
# print(b)

##########################################################

# ################ selection sort  ############################

'''  selection sort '''

# n=int(input())
# a=[None]*n
# print(a)
# b=0
# while b<n:
#     c=0
#     x=int(input())
#     while c<=b:
#         a[b]=x
#         c+=1
#     b+=1
# print(a)
# i=0
# while i<n:
#     min=i
#     j=i
#     while j<n:
#         if a[j]<a[min]:
#             min=j
#         j+=1
#     a[min],a[i]=a[i],a[min]
#     i+=1
# print(a)

# ###################################################################    

#######################  merge 2 sorted array  ##########################

''' ques" 5. Merge two sorted arrays into a single sorted array'''

# n=int(input())
# arr1=[None]*n
# a=0
# while a<n:
#     b=int(input())
#     arr1[a]=b
#     a+=1
# print(arr1)

# k=0
# while k<n:
#     min=k
#     k1=k
#     while k1<n:
#         if arr1[k1]<arr1[min]:
#             min=k1
#         k1+=1
#     arr1[min],arr1[k]=arr1[k],arr1[min]
#     k+=1
# print(arr1)


# N=int(input())
# arr2=[None]*N
# i=0
# while i<N:
#     x=int(input())
#     arr2[i]=x
#     i+=1
# print(arr2)

# K=0
# while K<N:
#     min1=K
#     K1=K
#     while K1<N:
#         if arr2[K1]<arr2[min1]:
#             min1=K1
#         K1+=1
#     arr2[min1],arr2[K]=arr2[K],arr2[min1]
#     K+=1
# print(arr2)


# arr=[None]*(n+N)
# m=0
# m1=0
# x1=0
# while m<n and m1<N:
#     if (arr1[m]<arr2[m1]):
#         arr[x1]=arr1[m]
#         m+=1
#         x1+=1
#     else:
#         arr[x1]=arr2[m1]
#         m1+=1
#         x1+=1
# while m<n:
#     arr[x1]=arr1[m]
#     m+=1
#     x1+=1
# while m1<N:
#     arr[x1]=arr2[m1]
#     m1+=1
#     x1+=1
# print(arr)


########################################################################3
"""ques: 6. Given an unsorted array of size N that contains only non-negative integers, find a
contiguous subarray which adds to a given number S. In case of multiple subarrays,
return the subarray which comes first on moving from left to right. Eg, let us say the array
is - 3, 6, 7, 5, 10. And the value of S = 12. The output should be - 7, 5"""
# a=int(input())
# n=int(input())
# x=[None]*a
# i=0
# while i<a:
#     b=int(input())
#     x[i]=b
#     i+=1
# print(x)
# j=0
# c=0
# while j<a:
#     k=j+1
#     # c=0
#     while k<a:
#         if x[j]+x[k]==n:
#             print(x[j],x[k])
#             c+=1
#         k+=1
#     if c==1:
#         i=n
#         break
#     j+=1

#####################################################3


# a=[3,5,6,2,8,1]
# b=[]
# n=int(input())
# i=0
# while i<len(a):
#     if i==b:
#         b.append(a[i])
#         a[i]="a"
#     i=(i+1)%(len(a))
#     if a[i]=="a":
#         pass
#     i=(i+1)%(len(a))
# print(b)
        
    
    
##############################################3
"""ques: 8. Given two sorted arrays nums1 and nums2 of size m and n respectively, return the
median of the two sorted arrays.""" 
    
# n=int(input())
# arr1=[None]*n
# a=0
# while a<n:
#     b=int(input())
#     arr1[a]=b
#     a+=1
# print(arr1)

# k=0
# while k<n:
#     min=k
#     k1=k
#     while k1<n:
#         if arr1[k1]<arr1[min]:
#             min=k1
#         k1+=1
#     arr1[min],arr1[k]=arr1[k],arr1[min]
#     k+=1
# print(arr1)


# N=int(input())
# arr2=[None]*N
# i=0
# while i<N:
#     x=int(input())
#     arr2[i]=x
#     i+=1
# print(arr2)

# K=0
# while K<N:
#     min1=K
#     K1=K
#     while K1<N:
#         if arr2[K1]<arr2[min1]:
#             min1=K1
#         K1+=1
#     arr2[min1],arr2[K]=arr2[K],arr2[min1]
#     K+=1
# print(arr2)


# arr=[None]*(n+N)
# m=0
# m1=0
# x1=0
# while m<n and m1<N:
#     if (arr1[m]<arr2[m1]):
#         arr[x1]=arr1[m]
#         m+=1
#         x1+=1
#     else:
#         arr[x1]=arr2[m1]
#         m1+=1
#         x1+=1
# while m<n:
#     arr[x1]=arr1[m]
#     m+=1
#     x1+=1
# while m1<N:
#     arr[x1]=arr2[m1]
#     m1+=1
#     x1+=1
# print(arr)
# if (n+N)%2!=0:
#    median=arr[((n+N)//2)]
# else:
#     median=(arr[((n+N)//2)-1]+arr[((n+N)//2)])//2
# print(median)

#########################################################

'''ques:3  Print the elements of an array of size N, in a rotated manner with a gap of K. Eg, let us
say the array is - 3, 6, 7, 5, 10. And the value of k = 3. The output should be - 7, 3, 10, 6,
5. If k = 2, the output should be - 6, 5, 3 10, 7  '''

a=int(input())
n=[None]*a
n2=[None]*a
k=int(input())
i=0
while i<a:
    b=int(input())
    n[i]=b
    i+=1
print(n)
n2 = [0]*a
t=0
j=0
c=0
while t<a:
    if n[j]!="a":
        c+=1
    # elif c<k:
    #     c+=1
    if c==k:
        n2[t]=n[j]
        n[j]="a"
        c=0
        t+=1
    j=(j+1)%a
print(n2)


    ###############################################################
    
# num=[23,4,1,8,6,45,34]
# i=0
# while i<len(num):
#     j=0
#     while j<len(num)-1:
#         if num[j]>num[j+1]:
#             num[j],num[j+1]=num[j+1],num[j]
#         j+=1
#     i+=1
# print(num)
# value=int(input())
# low=0
# high=len(num)-1
# while low<=high:
#     mid=(low+high)//2
#     if num[mid]==value:
#         print(num[mid])
#     elif num[mid]>value:
#         mid=low
#     elif num[mid]<value:
#         mid=high
#     i+=1
# print(mid,value)
    
        


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# a=[1,2,3,4,5]
# a1=5
# insertion=[]
# b=[4,5,6,7,8,9]
# b1=6
# union=[]
# m=0
# n=0
# while m<a1 and n<b1:
#     if a[m]<b[n]:
#         insertion.append(a[m])
#         m+=1
#     elif a[m]>b[n]:
#         insertion.append(b[n])
#         n+=1
#     elif a[m]==b[n]:
#         insertion.append(a[m])
#         union.append(a[m])
#         m+=1
#         n+=1
# if m<a1:
#     insertion.append(a[m])
#     m+=1
# if n<b1:
#     insertion.append(b[n])
#     n+=1
# print(insertion)
# print(union)



# a=input()
# b=0
# k=a
# count=0
# while b<len(k):
#     c= k.count(k[b])
#     if c%2!=0:
#         print("no")
#         count=0
#         break
#     else:
#         n=0
#         while n<len(k):
#             if k[b]==k[n]:
#                 k=k.replace(k[n],"")
#                 count+=1
#             n+=1
# if count>0:
#     print("yes")
#     b+=1


# a=int(input())
# n=int(input())
# i=0
# l=[None]*a
# while i<a:
#     b=int(input())
#     l[i]=b
#     i+=1
# j=0
# low=j
# up=a-1
# mid=(low+up)//2
# while low<up:
#     if n==l[mid]:
#         print("found",l[mid])
#     else:
#         if n<l[mid]:
#           up=mid-1
#         else:
#             low=mid+1
#     low+=1
# print("found",l[mid],mid)
        


