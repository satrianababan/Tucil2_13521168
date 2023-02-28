from divideandconquer import *
from bruteforce  import *
from visualisasi import *
import time
import platform
import numpy as np

points = int(input("Masukkan banyak titik : ")) 
dimensi = int(input("Masukkan dimensi : "))

if (points > 0 and dimensi > 0):
    arr_points = random_points(points,dimensi)
    quickSort(arr_points,0,points-1)
    if (dimensi == 3):
        count = 0
        start1 = time.time()
        d,p1,p2,count = closest_pair_DnC(arr_points,points,dimensi,count)
        end1 = time.time()
        timed1 = (end1-start1)*1000
        print("========================================")
        print("           DIVIDE AND CONQUER           ")
        print("========================================")
        print("Jarak terdekat antara 2 titik : ",round(d,2))
        print("Titik pertama : ",np.round_(p1, decimals=2))
        print("Titik kedua : ",np.round_(p2, decimals=2))
        print("Jumlah operasi euclidean DnC : ",count)
        print("Waktu eksekusi : ",timed1, "ms")
        print("Run in",platform.processor(),"Processor")
        print(" ")
        
        count =0
        start2 = time.time()
        min,p1,p2,count = closest_pair_bf(arr_points,points,dimensi,count)
        end2 = time.time()
        timed2 = (end2-start2)*1000
        print("========================================")
        print("              BRUTE FORCE               ")
        print("========================================")
        print("Jarak terdekat antara 2 titik : ",round(d,2))
        print("Titik pertama : ",np.round_(p1, decimals=2))
        print("Titik kedua : ",np.round_(p2, decimals=2))
        print("Jumlah operasi euclidean BF : ",count)
        print("Waktu eksekusi : ",timed2, "ms")
        print("Run in",platform.processor(),"Processor")
        
        visualisasi(arr_points,p1,p2)
        
    elif(dimensi > 0 and dimensi != 3):
            count = 0
            start1 = time.time()
            d,p1,p2,count = closest_pair_DnC(arr_points,points,dimensi,count)
            end1 = time.time()
            timed1 = (end1-start1)*1000
            print("========================================")
            print("           DIVIDE AND CONQUER           ")
            print("========================================")
            print("Jarak terdekat antara 2 titik : ",round(d,2))
            print("Titik pertama : ",np.round_(p1, decimals=2))
            print("Titik kedua : ",np.round_(p2, decimals=2))
            print("Jumlah operasi euclidean DnC : ",count)
            print("Waktu eksekusi : ",timed1, "ms")
            print("Run in",platform.processor(),"Processor")
            print(" ")
            
            count =0
            start2 = time.time()
            min,p1,p2,count = closest_pair_bf(arr_points,points,dimensi,count)
            end2 = time.time()
            timed2 = (end2-start2)*1000
            print("========================================")
            print("              BRUTE FORCE               ")
            print("========================================")
            print("Jarak terdekat antara 2 titik : ",round(d,2))
            print("Titik pertama : ",np.round_(p1, decimals=2))
            print("Titik kedua : ",np.round_(p2, decimals=2))
            print("Jumlah operasi euclidean BF : ",count)
            print("Waktu eksekusi : ",timed2, "ms")
            print("Run in",platform.processor(),"Processor") 
            
            # visualisasi(arr_points,p1,p2) 
    else:
        print("Dimensi tidak valid")
else:
    print("Jumlah titik atau dimensi tidak valid")
    

    
    
        
        
        