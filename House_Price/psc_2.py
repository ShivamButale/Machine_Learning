from scipy import stats
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd 
#from sklearn.cross_validation import train_test_split
#from sklearn.matrics import confusion_matrix
#from sklearn.metrics import accuracy_score

# ###TRAINING DATA

#Mydata = pd.read_csv("D:\Academics\PSC\PROJ___2\all\train")

x = np.array([112,345,198,305,372,550,302,420,578])  #SIZE OF HOUSES
y = np.array([1120,1523,2102,2230,2600,3200,3409,3689,4460])   #PRICE OF HOUSES

slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)

plt.plot(x,y,'ro',color='black')
plt.ylabel('Price')
plt.xlabel('Size of house')

plt.axis([0,600,0,5000]) #Max limits of x and y values

print("Value of the intercept is :", intercept)

plt.plot(x, x*slope+intercept, 'b') #blue coloured line whose eqn is y = m*x + c

plt.plot() #Plots the points in the given dataset on a graph
plt.show()

#Prediction

newX = 150
newY  = newX*slope + intercept #Line equation is y = m*x + c 
 
print("Price of the house is ",newY)
