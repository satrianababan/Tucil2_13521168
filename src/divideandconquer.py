import random
import math

# Function to find the partition position
def partition(arr, low, high):
    pivot = arr[(low+high)//2][0]
    i = low
    j = high
    while True:
        while(arr[i][0] < pivot):
            i = i + 1
        while(arr[j][0] > pivot):
            j = j - 1
        if i < j :
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i = i+1
            j = j-1
        if i>=j :
            break
    return j
 
# function to perform quicksort
def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi + 1, high)

# def sortbyX(npoint):
#     npoint_sorted = quick_sort(npoint)
#     return closest_pair(npoint_sorted)

def euclidean(x,y,n):
    if n == 1:
        return (x[0]-y[0])
    else:
        return math.sqrt(euclidean(x,y,n-1)**2 + (x[n-1]-y[n-1])**2)
    
def count_euclidean(x,y,n,ctr) :
    ctr += 1
    return euclidean(x,y,n), ctr

def closest_pair_DnC(arr,n,dimensi,count):
    if (n == 2):
        d = euclidean(arr[0],arr[1],dimensi)
        count += 1
        return d,arr[0],arr[1],count
    elif (n == 3):
        d1 = euclidean(arr[0],arr[1],dimensi)
        d2 = euclidean(arr[0],arr[2],dimensi)
        d3 = euclidean(arr[1],arr[2],dimensi)
        count += 3
        if (d1 < d2 and d1 < d3):
            return d1,arr[0],arr[1],count
        elif (d2 < d1 and d2 < d3):
            return d2,arr[0],arr[2],count
        else:
            return d3,arr[1],arr[2],count
    else:
        mid = n // 2
        kiri = arr[:mid]
        kanan = arr[mid:]
        d1,p11,p12,count1 = closest_pair_DnC(kiri,mid,dimensi,0)
        d2,p21,p22,count2 = closest_pair_DnC(kanan,n-mid,dimensi,0)
        count += count1 + count2
        d = 0
        p1 = []
        p2 = []
        if (d1 < d2):
            d = d1
            p1 = p11
            p2 = p12
        else:
            d = d2
            p1 = p21
            p2 = p22
        temp = []
        
        if (n%2) == 0:
            mid = (arr[mid-1][0] + arr[mid][0])/2
        else:
            mid = arr[mid][0]
            
        for i in kiri:
            if i[0] >= mid-d:
                temp.append(i)            
        for i in kanan:
            if i[0] <= mid+d:
                temp.append(i)
                
        for i in range(len(temp)):
            for j in range(i+1,len(temp)):
                count+=1
                if euclidean(temp[i],temp[j],dimensi) < d:
                    d = euclidean(temp[i],temp[j],dimensi)
                    p1 = temp[i]
                    p2 = temp[j]
        return d,p1,p2,count

# Generate random titik 
def random_points(points,dimensi):
    arr_points = []
    for i in range(points):
        point1 = []
        for j in range(dimensi):
            point2 = random.uniform(-1000,1000)
            point1.append(point2)
        arr_points.append(point1)
    return arr_points