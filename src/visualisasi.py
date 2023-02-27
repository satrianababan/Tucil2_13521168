import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualisasi(arr_points,p1,p2):
    arrX = []
    arrY = []
    arrZ = []
    
    for i in range(len(arr_points)):
        if (arr_points[i] != p1 and arr_points[i] != p2):
            arrX.append(arr_points[i][0])
            arrY.append(arr_points[i][1])
            arrZ.append(arr_points[i][2])
            
    fig = plt.figure(figsize=(6,6))
    ax = plt.axes(projection ="3d")
    
    ax.scatter3D(arrX, arrY, arrZ, color = "blue")
    ax.scatter3D(p1[0], p1[1], p1[2], color="red")
    ax.scatter3D(p2[0], p2[1], p2[2], color="red")
    
    plt.title("VISUALISASI")
    ax.set_xlabel('X-axis', fontweight ='bold')
    ax.set_ylabel('Y-axis', fontweight ='bold')
    ax.set_zlabel('Z-axis', fontweight ='bold')
    
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],[p1[2],p2[2]], c="red")
    
    # show plot
    plt.show()
