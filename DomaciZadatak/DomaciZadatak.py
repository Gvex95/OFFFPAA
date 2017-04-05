import random
import time
import sys
import numpy as np
import matplotlib.pyplot as plt
size1 = 10
size2 = 100
size3 = 1000
size4 = 10000
size5 = 100000
size6 = 1000000

def SelectionSort(A):
    for i in range(0,len(A)-1):
        minIndex=i
        for j in range(i+1,len(A)):
            if A[j] < A[minIndex]:
                minIndex=j
        if minIndex!=i:
            A[i],A[minIndex] = A[minIndex],A[i]
def RandomList(min,max,elements):
    list=random.sample(range(min,max),elements)
    return list

def RadixSort(A):
    max_element = max(A)
    exp=1
    while max_element/exp > 0:
        CountingSort(A,exp)
        exp*=10
def CountingSort(A,exp):
    n=len(A)
    output=[0] * (n)
    count=[0] * (10)

    #koliko se puta cifra elementa ponavlja u ulaznom nizu
    for i in range (0,n):
        index=(A[i]//exp)
        count[(index) % 10]+=1
    #sumiranje count niza, tako sto se trenutni i prosli element saberu
    for i in range(1,10):
        count[i]=count[i]+count[i-1]
    #smestanje u output niz
    i=n-1
    while i>=0:
        index=(A[i]//exp)
        output[count[(index)%10]-1]=A[i]
        count[(index)%10]-=1
        i-=1
    #kopiranje iz outputa u ulazni niz
    i=0
    for i in range(0,len(A)):
        A[i]=output[i]

def QuickSort(A):
    QuickSortRecursion(A,0,len(A)-1)

def QuickSortRecursion(A,low,high):
    pivot=Partition(A,low,high)
    QuickSortRecursion(A,low,pivot-1)
    QuickSortRecursion(A,pivot+1,high)

def GetPivot(A,low,high):
    mid=(high+low) // 2
    s = sorted([A[low],A[mid],A[high]])
    if s[1] == A[low]:
        return low
    elif s[1] == A[mid]:
        return mid
    return high

def Partition(A,low,high):
    pivotIndex = GetPivot(A,low,high)
    pivotValue = A[pivotIndex]
    #stavljamo pivot da bude skroz levo
    A[pivotIndex],A[low] = A[low],A[pivotIndex]
    border = low
    
    for i in range (low,high+1):
        if A[i] < pivotValue:
            border+=1
            A[i],A[border] = A[border],A[i]
        #postavljamo pivot na "sredinu", sve levo je manje od njega a desno je vece
    A[low],A[border] = A[border],A[low]
    return (border)

def PrintList(A):
    print(A)

list=RandomList(1,size4+1,size4)
PrintList(list)
start_time = time.clock()
SelectionSort(list)
end_time = time.clock() - start_time
print("Duration is: ", end_time)
PrintList(list)



            
          