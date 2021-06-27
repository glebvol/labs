import pandas as pd
import numpy as np
from scipy.optimize import linprog


def maximize_function(var, fileways):
    df = pd.read_excel(fileways,skiprows = 1)
    column_names = ['Морковь', 'Капуста', 'Горох', 'Картофель', 'М', 'А']
    
    
    harvest = df[['Морковь', 'Капуста', 'Горох', 'Картофель', 'М', 'А']]
    availability = df[['Морковь.1', 'Капуста.1', 'Горох.1', 'Картофель.1', 'М.1', 'А.1']]
    sales = df[['Морковь.2', 'Капуста.2', 'Горох.2', 'Картофель.2', 'М.2', 'А.2']]
    L = len(column_names)
    
    
    harvest = np.array(harvest)[var-1]
    availability = np.array(availability)[var-1]
    sales = np.array(sales)[var-1]
    
    
    max_square = 10
    c = [float(harvest[col].replace(',','.')) * sales[col] * (-1) for col in range(L)]
    
    
    temp_cond2 = np.eye(L)
    for i in range(L):
        temp_cond2[i,i] *= float(availability[i].replace(',','.'))
    temp_cond1 = np.ones((1,L))
    
    aub = np.vstack((temp_cond2,temp_cond1))
    bub = []
    for i in range(L):
        bub.append(-1*c[i]*aub[i,i])
    bub.append(max_square)
    aub = aub.tolist()
    
    bound = []
    for i in range(L):
        bound.append((0,float(availability[i].replace(',','.'))))
    bound = tuple(bound)
    
    
    res = linprog(
        c=c, 
        A_ub=aub, 
        b_ub=bub,
        bounds=bound,
    )
    

    
    return res.x


if __name__ == '__main__':
    var = 1
    fileways = "C:\\Users\\Gleb\\Desktop\\учеба\\Программирвоание ЛАБЫ\\" + "FARMER.xlsx"
    X = maximize_function(var, fileways)
    for a,b in zip(['Морковь', 'Капуста', 'Горох', 'Картофель', 'М', 'А'], X):
        print(a,round(b,1))