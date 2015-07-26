import numpy as np
import pylab as p
from pandas.io.data import DataReader as DR
from datetime import datetime as dt

#define function for moving average
def movingaverage (values,window):
    weights = np.repeat(1.0,window)/window
    sma = np.convolve(values,weights,'valid')
    return sma

#download Maxis 5 years stock price    
start = dt(2010, 1, 1)
end = dt(2015, 5, 1)
data = DR("6012.KL", 'yahoo', start, end) 
Close_P = data['Close'].values #take out close price from maxis

# Calculate 5-day moving average of Maxis
MA = movingaverage (Close_P,5)

#plot the moving average graph
num= len(MA)
t = p.linspace (0,num,num); 
p.title('5-day Moving Average for Maxis')
p.xlabel('Days');p.ylabel('Average Stock Price, $RM$ ')
p.plot(t,MA); p.show();

#calculate the correlation of Maxis with FTSEKLCI
Alldata=['^KLSE','6012.KL']
cor = DR(Alldata, 'yahoo', start, end)['Close']
correlation = cor.corr()
print('The correlation is : ')
print(correlation)
