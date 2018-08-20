# coding: utf-8
import numpy as np
#%%
X = np.array([1.0, 0.5])
W = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
B = np.array([0.1, 0.2, 0.3])
#%%
print(X.shape)
print(W.shape)
print(B.shape)
#%%
A = np.dot(X, W)+B
print(A)
#%%
def softmax(x):
    x = x - np.max(x) # 오버플로 대책
    return np.exp(x) / np.sum(np.exp(x))
#%%
y = softmax(A)
#%%
# Correct one hot vector 
t = [0, 0, 1]
#%%
# hint : np.sum, np.log(x + delta) for preventing log(0)
# 즉. np.log를 사용할때 np.log(0)이 되는 것을 막기 위해 delta를 더하세요.
###################################
####    your code      ############
###################################
def cross_entropy_error(y, t):
    delta = 1e-7
    loss = -np.sum(t*np.log(y+delta)) # write code here
    return loss

#%%
lloss = cross_entropy_error(y,t)
