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
# matrix multiplication : np.dot
# element wise multiplication : just *
# matrix add : just + 

# your code
A = np.dot(X, W) + B # make : XW+B
print(A)
