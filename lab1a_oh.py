import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from lab1a_utilities import calculate_force
from lab1a_utilities import calculate_potential

# Create the source charges

Q1 = 1
Q2 = -1
Q3 = -1

x1 = 100
y1 = 100

x2 = 10
y2 = 10

x3 = -50
y3= -50

charges = np.array([Q1, x1, y1, Q2, x2, y2, Q3, x3,y3]).reshape(3, 3)

# Set the default initial conditions for v0, angle, and y0
v0, angle, y0 = 50.0, 30.0, 30.0    
# Keep x0 fixed at -100
x0 = -100.

def clear():
    
    # NO NEED TO EDIT THIS FUNCTION

    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    ax.cla()
    ax.axis('square')
    ax.set_xlim(-200,200)
    ax.set_ylim(-200,200)
    ax.set_title('Electrostatic Projectile Game',fontsize=16)
    ax.set_xlabel('x position (meters)',fontsize=16)
    ax.set_ylabel('y position (meters)',fontsize=16)
    ax.grid(visible=True)
    fig.tight_layout()    
    fig.show()
    return

def create_game_window():
    fig = plt.figure('Game Window')
    fig.clf()
    ax = fig.add_subplot()
    clear()
    return

############################################################

def play():

    # NO NEED TO EDIT THIS FUNCTION

    global v0, angle, y0
    
    print("Starting x location is -100")
    v0 = float(input("Enter the initial speed between zero and 100.\n"))
    assert(v0 >= 0 and v0 <= 100), "Initial velocity should > 0 and < 100"
    angle = float(input("Enter the initial angle in degrees.\n"))
    assert(angle >= -180.00 and angle <= 180.00), \
        "Angle should be between -180 and +180"
    y0 = float(input("Enter the initial y position.\n"))
    assert(y0 >= -200 and y0 <= 200), "y0 should be between -200 and +200"
    
    plot_trajectory()
    
    return
 


############################################################

def reveal_potential():

    fig = plt.figure('Game Window')
    # for a 3D wireframe or surface plot, comment out this line:
    ax = fig.axes[0]
# Uncomment these lines to create a 3D wireframe or surface plot
#    fig.clf()
#    ax = fig.add_subplot(projection='3d')

    # your code goes here

    x = np.linspace(-500, 500, 100)
    y = np.linspace(-500, 500, 100)
    
    X, Y = np.meshgrid(x, y)
    
    Z = np.zeros(100*100).reshape(100, 100)
    
    for m in range(100):
        for n in range(100):
            Z[m, n] = calculate_potential(x[n], y[m], charges)

    return ax.contour(X, Y, Z, levels = np.linspace(-5000, 5000, 30))
     

############################################################

def reveal_forcefield():
    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    
    # your code goes here


    return

############################################################


############################################################

def plot_trajectory():

    fig = plt.figure('Game Window')
    ax = fig.axes[0]
    
    # Your code goes here
    
    def derivatives(t, s):
        D = np.zeros(4)
        D[0] = s[1]
        D[1] = calculate_force(s[0], s[2], charges)[0]
        D[2] = s[3]
        D[3] = calculate_force(s[0], s[2], charges)[1]
        return D
    vx0 = v0*np.cos(np.radians(angle))
    vy0 = v0*np.sin(np.radians(angle))
    
    t1 = 0
    t2 = 50
    
    t = np.linspace(t1, t2, 100)
    
    solution = solve_ivp(derivatives, (t1, t2), (x0, vx0, y0, vy0), t_eval = t)
    
    x = solution.y[0]
    y = solution.y[2]
    
    ax.plot(x, y, marker = 'o', markersize = 4)
    return

############################################################


def solve_it():
    answer1 = int(input('Does the first quadrant have (1) positive charge, (2) negative charge, (3) neither, (4) both? \n'))
    a1 = (Q1 > 0 and x1 > 0 and y1 > 0) or (Q2 > 0 and x2 > 0 and y2> 0) or (Q3 > 0 and x3 > 0 and y3 > 0)
    b1 = (Q1 < 0 and x1 > 0 and y1 > 0) or (Q2 < 0 and x2 > 0 and y2 > 0) or (Q3 < 0 and x3 > 0 and y3 > 0)
    if answer1 == 1:
        if a1 and (not b1):
            s1 = 1
        else:
            s1 = 0
      
    elif answer1 == 2:
        if b1 and (not a1):
            s1 = 1
        else:
            s1 = 0
        
    elif answer1 == 3:
        if (not a1) and (not b1):
            s1 = 1
        else:
            s1 = 0
            
    elif answer1 == 4:
        if a1 and b1:
            s1 = 1
        else:
            s1 = 0
            
    answer2 = int(input('How about the second quadrant?\n'))
    
    a2 = (Q1 > 0 and x1 < 0 and y1 > 0) or (Q2 > 0 and x2 < 0 and y2 > 0) or (Q3 > 0 and x3 < 0 and y3 > 0)
    b2 = (Q1 < 0 and x1 < 0 and y1 > 0) or (Q2 < 0 and x2 < 0 and y2 > 0) or (Q3 < 0 and x2 < 0 and y2 > 0)
            
    if answer2 == 1:
        if a2 and (not b2):
            s2 = 1
            print('Correct')
        else:
            s2 = 0
            print('Incorrect')
    elif answer2 == 2:
        if b2 and (not a2):
            s2 = 1
            print('Correct')
        else:
            s2 = 0
            print('Incorrect')
    elif answer2 == 3:
        if (not a2) and (not b2):
            s2 = 1
            print('Correct')
        else:
            s2 = 0
            print('Incorrect')
            
    elif answer2 == 4:
        if a2 and b2:
            s2 = 1
            print('Correct')
        else:
            s2 = 0
            print('Incorret')
    answer3 = int(input('How about the third quadrant? \n'))
    
    a3 = (Q1 > 0 and x1 < 0 and y2 < 0) or (Q2 > 0 and x2 < 0 and y2 < 0) or (Q3 > 0 and x3 <0 and y3 < 0)
    b3 = (Q1 < 0 and x1 < 0 and y1 < 0) or (Q2 < 0 and x2 < 0 and y2 < 0) or (Q3 < 0 or x3 < 0 or y3 < 0)
        
    if answer3 == 1:
        if a3 and (not b3):
            s3 = 1
            print('Correct')
        else:
            s3 = 0
            print('Incorrect')
    elif answer3 == 2:
        if b3 and (not a3):
            s3 = 1
            print('Correct')
        else:
            s3 = 0
            print('Incorrect')
    elif answer3 == 3:
        if (not a3) and (not b3):
            s3 = 1
            print('Correct')
        else:
            s3 = 0
            print('Incorrect')
            
    elif answer3 == 4:
        if a3 and b3:
            s3 = 1
            print('Correct')
        else:
            s3 = 0
            print('Incorrect')
            
    answer4 = int(input('How about the fourth quadrant? \n'))

    a4 = (Q1 > 0 and x1 > 0 and y1 < 0) or (Q2 > 0 and x2 > 0 and y2 < 0) or (Q3 > 0 and x3 > 0 and y3 < 0)
    b4 = (Q1 < 0 and x1 > 0 and y1 < 0) or (Q2 < 0 and x2 > 0 and y2 < 0) or (Q3 < 0 and x3 > 0 and y3 < 0)
    
    if answer4 == 1:
        if a4 and (not b4):
            s4 = 1
            print('Correct')
        else:
            s4 = 0
            print('Incorrect')
    elif answer4 == 2:
        if b4 and (not a4):
            s4 = 1
            print('Correct')
        else:
            s4 = 0
            print('Incorrect')
    elif answer4 == 3:
        if (not a4) and (not b4):
            s4 = 1
            print('Correct')
        else:
            s4 = 0
            print('Incorrect')
    elif answer4 == 4:
        if a4 and b4:
            s4 = 1
            print('Correct')
        else:
            s4 = 0
            print('Incorrect')
    
    if s1 + s2 + s3 + s4 == 4:
        print('Congratulations!')
        create_game_window()
        return reveal_potential()
    else:
        print('Please try again.')
        return









