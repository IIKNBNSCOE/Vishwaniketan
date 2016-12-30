""" McCulloch Pitts Neuron Model for AND function """
import numpy as np
Threshold=2
bias=0
W=[1,1]
print('Enter Inputs for AND function')
i1=int(input('Enter first input\n'))
i2=int(input('Enter Second input\n'))
X=[i1,i2]
X1=np.mat(X)
W1=np.mat(W)
W2=W1.reshape(2,1)
Net=X1*W2+bias
if Net>=Threshold:
    print('Output=',1)
else:
    print('Output=',0)