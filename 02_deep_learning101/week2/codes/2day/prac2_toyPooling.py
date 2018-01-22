import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.util import im2col, col2im

#%% 초기값 설정 
x = list(range(2*3*3))
x = np.array(x).reshape(1, 2, 3, 3) # (데이터 수, 채널 수, 높이, 너비)
x[0, 0, 1, 1] = 8
pool_h = 2
pool_w = 2
stride = 1
pad = 0
#%%
print("x :\n", x)
N_, C_, H_, W_ = x.shape

out_h = int(1 + (H_ - pool_h) / stride)
out_w = int(1 + (W_ - pool_w) / stride)

col_old = im2col(x, pool_h, pool_w, stride, pad) # 출력해보세요
col = col_old.reshape(-1, pool_h*pool_w) # 위의 결과와 비교해보세요

arg_max = np.argmax(col, axis=1) # max의 위치기억 (np.argmax)
out = np.max(col, axis=1) # 출력계산
out_final = out.reshape(N_, out_h, out_w, C_).transpose(0, 3, 1, 2)
print("out_final :\n", out_final)

######################################################################
#%% backward
dout = np.ones_like(out_final)
dout = dout.transpose(0, 2, 3, 1)
#%%        
pool_size = pool_h * pool_w

# 결과를 저장하기 위한 공간 (pooling size만큼 크기를 넓혀 줍니다.)
dmax = np.zeros((dout.size, pool_size))

# 기억해 두었던 위치에 값을 채워줍니다.
dmax[np.arange(arg_max.size), arg_max.flatten()] = dout.flatten()
#%%
# 원래의 모양대로 복원합니다.
#%%
dmax = dmax.reshape(dout.shape + (pool_size,)) 
#%%
dcol = dmax.reshape(dmax.shape[0] * dmax.shape[1] * dmax.shape[2], -1)
dx = col2im(dcol, x.shape, pool_h, pool_w, stride, pad)
print("dx : \n", dx)
