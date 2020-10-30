import matplotlib.pyplot as plt
import sympy as simp
import re

#Linear Eq formula - y = (ax + c)/b
#eq1 - a1x + b1y + c1 = 0
#eq2 - a2x + b2y + c2 = 0

solutions = []

def a_inp_eq1():
    global a1
    a1 = input('\nPlease specify the value of "a" for the first equation: ')

    global b1
    b1 = input('Please specify the value of "b" for the first equation: ')

    global c1
    c1 = input('Please specify the value of "c" for the first equation: ')

def check_errors_eq1():
    try:
        int(a1)
        int(b1)
        int(c1)
    except ValueError:
        try:
            float(a1)
            float(b1)
            float(c1)
        except ValueError:
            print('\nOne of your inputs may not be a valid one please try again, this time with valid ones')
            a_inp_eq1()

def a_inp_eq2():
    global a2
    a2 = input('\nPlease specify the value of "a" for the second equation: ')

    global b2
    b2 = input('Please specify the value of "b" for the second equation: ')

    global c2
    c2 = input('Please specify the value of "c" for the second equation: ')

def check_errors_eq2():
    try:
        int(a2)
        int(b2)
        int(c2)
    except ValueError:
        try:
            float(a2)
            float(b2)
            float(c2)
        except ValueError:
            print('\nOne of your inputs may not be a valid one please try again, this time with valid ones')
            a_inp_eq2()

def simpfy():
    global a1
    a1 = simp.sympify(a1)

    global b1
    b1 = simp.sympify(b1)

    global c1
    c1 = simp.sympify(c1)

    global a2
    a2 = simp.sympify(a2)

    global b2
    b2 = simp.sympify(b2)

    global c2
    c2 = simp.sympify(c2)

def conversion():
    global a_con1
    a_con1 = a1 * -1
    global b_con1
    b_con1 = b1 * 1
    global c_con1
    c_con1 = c1 * -1

    global a_con2
    a_con2 = a2 * -1
    global b_con2
    b_con2 = b2 * 1
    global c_con2
    c_con2 = c2 * -1

def solve_eq():
    x = simp.Symbol('x')
    y = simp.Symbol('y')
    eq = (a1 * x + b1 * y + c1 , a2 * x + b2 * y + c2)
    global sol
    sol = simp.solve(eq , x , y)
    solutions.append(sol)
    print('\nThe solution is: ',sol)
    m = re.match(r"{x: (-?[0-9]\d*(?:\.\d+)?), y: (-?[0-9]\d*(?:\.\d+)?)}", str(sol))
    if m:
        return m.group(1) , m.group(2)

def Linear_eq(a,b,c,clr):
    x = list(range(-10,11))
    y = [((a * ints + c)/b) for ints in x]
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('MathsAIL')
    plt.grid(True)
    plt.plot(x , y ,label = 'linear' ,linestyle = '-' ,color= clr)

def plot():
    solx , soly = solve_eq()
    Linear_eq(a_con1,b_con1,c_con1 ,'r')
    Linear_eq(a_con2,b_con2,c_con2 ,'b')
    plt.annotate('(%s,%s)'%(solx,soly) , (float(solx),float(soly)))
    plt.show()

def run():
    print('This is our Maths AIL project!Have fun!')
    print('A linear equations is generally in this form: ax + by + c = 0')
    print("For this project you as the user will be inputting the values of 'a', 'b' and 'c'")
    a_inp_eq1()
    check_errors_eq1()
    a_inp_eq2()
    check_errors_eq2()
    simpfy()
    conversion()
    plot()
    rerun()

def rerun():
    print('\nThat went great')
    g_input = input('Do you want to go again? press "y" for yes and "n" for no: ')

    if g_input.lower() == 'y' or g_input.lower() == 'yes':
        print('Fantastic lets go again')
        run()

    elif g_input.lower() == 'n' or g_input.lower() == 'no':
        print('Have a nice day!')
        print('\nThe solutions for all previously ran tests: ',solutions)
        quit()

    else:
        print('Please input a valid response')
        rerun()

run()