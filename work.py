# -*- coding: utf-8 -*-

#Student: Luiz Augusto da Silva

import numpy as np
import matplotlib.pyplot as plot

def eval_f(fx ,x):
    return eval(fx)

def graphic(fx, a, b):   
    interval = np.linspace(a,b)  
    plot.plot(interval, eval_f(fx,interval), label = 'f(x)')
    plot.legend()
    plot.grid() 
    plot.show()

def f(x, function):
    return eval(function)

def bisection(a, b, tol, n, function):
    xant = float("nan")     
    for i in range(n):      
        x = (a + b) / 2     
        fx = f(x, function)
        signal = f(a, function) * fx
        error=abs((x-xant)/max(x, 1))       
        xant = x
        print("iteraction {i:3d}: a={a:+.5f}, ".format(i=i, a=a) +
              "b={b:+.5f}, error={err:+.5f}, ".format(b=b, err=error) +
              "x={x:+.5f}, f(x)={fx:+.5f}, ".format(x=x, fx=fx) +
              "signal={s:+.5f}".format(s=signal))
        if (fx == 0) or (error < tol):     
            print("Approximate root found: {r:+5.5f}".format(r=x))
            break
        if signal > 0:      
           a = x
        else:
           b = x

def false_position(a, b, tol, n, function):
    xant = float("nan")
    for i in range(n):
        x = (a * f(b, function) - b * f(a, function)) / (f(b, function) - f(a, function))      
        error=abs((x-xant)/max(x, 1))
        xant = x
        result = f(x, function)*f(a, function)
        fx = f(x, function)   
        print("iteraction {i:3d}: a={a:+.5f}, ".format(i=i, a=a) +
              "b={b:+.5f}, error={err:+.5f}, ".format(b=b, err=error) +
              "x={x:+.5f}, f(x)={fx:+.5f}, ".format(x=x, fx=fx) +
              "f(x) x f(a)={r:+.5f}".format(r=result))
        if (fx == 0) or (error < tol):      
            print("Approximate root found: {r:+5.5f}".format(r=x))
            break
        
        if (result) > 0:        
            a = x
        else:       
            b = x
        if (i == 19):
          print("Approximate root found: {r:+5.5f}".format(r=x))
          break

def secant(a, b ,Tol, n, function):
    x_previous = float("NaN")
    x = a
    x_previous = b 
    for k in range(0,n):
        error = abs ((x-x_previous)/(max(x,1)))
        print(k,x,f(x, function), error)
        
        if f(x, function) == 0 or error < Tol:     
            break
        xa = x - f(x, function) * ((x-x_previous)/ f(x, function) -f(x_previous, function))     #Calcula x**(k+1)
        x_previous = x     
        x = xa      
        return x
    print(f'Approximate root found: {(secant(a, b, tol, n)):.5f}')
       


while(True): 

    fx = input('Enter the function f(x): ')

    while (True):

        a = float(input('Enter the start of the range: '))
        b = float(input('Enter the end of the range: '))
    
        verific = input('Do you want to adjust the range? [Y/N]: ')
        if verific == 'N' or 'n':
            break

    tol = 0.00001       
    n = 20              

    print('\nCalculation of the root by bisection: \n')
    bisection(a, b, tol, n, fx)

    print('\nCalculation of the root by false positon: \n')
    false_position(a, b, tol, n, fx)
    print('\nCalculation of the root by secant')

    secant(a, b, tol, n, fx) 

    graphic(fx, a, b)
    
    verific = input('\nDo you want to perform a new calculation? [Y/N]: ')
    if verific == 'N' or 'n':
        break