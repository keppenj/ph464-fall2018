import numpy as np #Need numpy for array
import matplotlib.pyplot as plt #Need matpllotlib for MATLAB like plots
import numpy.polynomial.polynomial as poly #Needed for good polynomial fitting
import scipy
from scipy import stats

plt.style.use('seaborn-whitegrid') #Setting up background for plot

data = np.loadtxt("students/one-jk/data/data.txt") #Loading in data from subfolder
#print(data) #Ensuring that data is being imported

x = data[:,0] #Splitting up the dataset into x and y
y = data[:,1]

#print(x) #Checking to make sure that the data is being split properly.
#print(y)

plt.plot(x,y,'.') #Plotting Data

z = poly.polyfit(x, y, 2) #Least square parabolic fit
z2 = poly.polyfit(x[9:21], y[9:21],2) #reducing to points around the minimum
z3 = poly.polyfit(x[9:15], y[9:15],2) #Further reducing

#zspace = np.linspace(3,10,30) #Mimicing the range of the data set
zfit = poly.Polynomial(z) #Creates the function to be evaluated as a function of zspace
zmin =np.amin(zfit(x)) #Finding the minimum of the fit.

zfit2 = poly.Polynomial(z2) #Repeating process with reduced points
zmin2 =np.amin(zfit2(x))

zfit3 = poly.Polynomial(z3)
zmin3 =np.amin(zfit3(x))

plt.plot(x, zfit(x), '-') #Plotting all of the points
plt.plot(x,zfit2(x), '-.')
plt.plot(x,zfit3(x), 'o')

slope, intercept, r_value, p_value, std_err = stats.linregress(x,zfit(x)) #Setting up linear regression with Scipy
slope2, intercept2, r_value2, p_value2, std_err2 = stats.linregress(x,zfit2(x))
slope3, intercept3, r_value3, p_value3, std_err3 = stats.linregress(x,zfit3(x))

#E(v) = E_0 + (B_0 * (v/Bprime)((1/(Bprime-1)*((V_0/v)^Bprime) +1) - (B_0*V_0/(Bprime-1))

print("The minimum of the original fitted function is:", zmin)
print("The slope of the orginal LR is:", slope)
print("The intercept of the original LR is:", intercept)
print("The standard error of the original LR is:", std_err)
print() #This breaks up the output nicely
print("The minimum of the second fitted function is:", zmin2)
print("The slope of the second LR is:", slope2)
print("The intercept of the second LR is:", intercept2)
print("The standard error of the second LR is:", std_err2)
print()
print("The minimum of the third fitted function is:", zmin3)
print("The slope of the third LR is:", slope3)
print("The intercept of the third LR is:", intercept3)
print("The standard error of the third LR is:", std_err3)
plt.show()

#print("Hello World")
