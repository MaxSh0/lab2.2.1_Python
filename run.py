import optimal_gradient_method as og
from scipy.optimize import minimize

def f1(x):
    return 4*pow((x[0]-5),2) + pow((x[1]-6),2) 

def f2(x):
    return pow(x[0]*x[0]+x[1]-11, 2) + pow(x[0]+x[1]*x[1]-7,2)

def f3(x):
    return (100*(x[1]-x[0]**2)**2 + 
    (1-x[0])**2 + 
    90*(x[3]-x[2]**2)**2 + 
    (1-x[2])**2 + 
    10.1*((x[1]-1)**2+(x[3]-1)**2) + 
    19.8*(x[1]-1)*(x[3]-1))

def f4(x):
    x1,x2,x3,x4 = x
    return ((x1+10*x2)**2+
            5*(x3-x4)**2+
            (x2-2*x3)**4+
            10*(x1-x4)**4)

funcsToTestArr = [f1, f2,f3,f4] 
startPointArr = [[0.,0.],[0.,0.],[-3.,-1.,-3.,-1.],[3.,-1.,0.,1.]]
stepArr = [[1.,1.],[1.,1.],[1.,1.,1.,1.],[1.,1.,1.,1.]]
eps = 0.01
sizeArr = [2,2,4,4]

while (True):
    print("""
    Выберите функцию для оптимизации:
    1 - ф. Химмельблау №1
    2 - ф. Химмельблау №2
    
    4 - ф. Пауэлла
    """)
    chosenFun = int(input())
    functionToTest = funcsToTestArr[chosenFun-1]
    step = stepArr[chosenFun-1]
    startPoint = startPointArr[chosenFun-1]

    result = og.optimal_gradient_method(functionToTest, startPoint, eps*eps)
    
    print("Решение:", result, ", значение функции в этой точке: ", functionToTest(result))