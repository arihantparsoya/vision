from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from scipy.ndimage.interpolation import shift

def plot_contour(cnt1=None, cnt2=None, axis1='X', axis2='Y', top_axis='Z'):

    '''
    To plot the contour in 3D with height of the person as the given axis

    Inputs:
        cnt1: first contour to be plotted
        cnt2: second contour to be plotted
        axis: axis along which it will be plotted in 3D

    Output:
        plots the contour in 3D
    '''

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')


    x1 = []
    y1 = []
    z1 = []
    x2 = []
    y2 = []
    z2 = []

    if cnt1 is not None:
        for points in cnt1:
            x1.append(points[0][0])
            z1.append(-points[0][1])
            y1.append(0)
    x1 = np.array(x1) - np.average(x1) # shifting the plot to the origin

    if cnt2 is not None:
        for points in cnt2:
            y2.append(points[0][0])
            z2.append(-points[0][1])
            x2.append(0)

    y2 = np.array(y2) - np.average(y2) # shifting the plot to origin

    ax.scatter(x1, y1, z1, c='r', marker='D')
    ax.scatter(x2, y2, z2, c='r', marker='*')
    axes = plt.gca()
    axes.set_xlim([-300,300])
    axes.set_ylim([-300,300])
    axes.set_zlim([-1600,100])
    plt.gca().set_aspect('equal', adjustable='box')
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    #plt.axis('equal')
    plt.show()
