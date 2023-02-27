from divideandconquer import *

def closest_pair_bf(arr_points,points,dimensi,count):
    min = euclidean(arr_points[0], arr_points[1], dimensi)
    p1 = arr_points[0]
    p2 = arr_points[1]
    
    for i in range(points):
        for j in range(i+1,points):
            d = euclidean(arr_points[i],arr_points[j],dimensi)
            count+=1
            if d < min:
                min = d
                p1 = arr_points[i]
                p2 = arr_points[j]
    return min,p1,p2,count