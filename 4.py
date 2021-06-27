import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.spatial import ConvexHull, convex_hull_plot_2d

def get_angle(p1, p2):
    return math.acos(((p1[0]*p2[0])+(p1[1]*p2[1]))/(math.sqrt(p1[0]*p1[0] + p1[1]*p1[1])*math.sqrt(p2[0]*p2[0] + p2[1]*p2[1])))


def get_convexhull(fileways, var):
    df = pd.read_csv(fileways, header = None)
    points = np.array(df)[var-1].reshape(int(df.shape[1]/2),2)
    hull = ConvexHull(points)
    plt.plot(points[:,0], points[:,1], 'o')
    for simplex in hull.simplices:
        plt.plot(points[simplex, 0], points[simplex, 1], 'k-')
    plt.savefig('convex.png')
    plt.show()
    del df

    df = pd.DataFrame(columns = ['X','Y', 'angle'])

    df['X'] = hull.simplices[:,0]
    df['Y'] = hull.simplices[:,1]

    temp_points = np.vstack((hull.simplices[-1,:], hull.simplices, hull.simplices[1,:]))

    angle = []
    for i in range(1,len(temp_points)-1):
        p1 = [temp_points[i][0]-temp_points[i-1][0], temp_points[i][1]-temp_points[i-1][1]]
        p2 = [temp_points[i][0]-temp_points[i+1][0], temp_points[i][1]-temp_points[i+1][1]]
        angle.append(get_angle(p1, p2))



    df['angle'] = angle

    df = df.sort_values('angle')
    df.to_csv('convex_ans.csv', index = None)
    
if __name__ == '__main__':
    var = 1
    #ввести путь к файлу convex.csv
    fileways = "C:\\Users\\Gleb\\Desktop\\учеба\\Программирвоание ЛАБЫ\\" + "convex.csv"
    get_convexhull(fileways, var)



