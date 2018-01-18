import sys, os
sys.path.append(os.pardir)
import numpy as np
from common.util import im2col, col2im

#%% 초기값 설정 
x = list(range(1*3*3))
x = np.array(x).reshape(1, 1, 3, 3) # (데이터 수, 채널 수, 높이, 너비)
W = np.ones((2, 1, 2, 2)) # (필터 수, 필터 채널, 필터높이, 필터 너비)
W[1] = W[1]*2
b = np.ones((2,)) # (바이어스 수)
pad = 0
stride = 1
#%% 
N_, C_, H_, W_ = x.shape
FN, C, FH, FW = W.shape
#%%
out_h = 1 + int((H_ + 2*pad - FH)/stride)
out_w = 1 + int((W_ + 2*pad - FW)/stride)
#%%
col = im2col(x, FH, FW, stride, pad) # im2col 함수 활용
###############################
######### your code ###########
###############################
col_W = None # W의 형태를 변형하시오.
out = None # Affine 연산 후 바이어스를 더합시다.
###############################
out_final = out.reshape(N_, out_h, out_w, -1).transpose(0, 3, 1, 2)
print("out_final : \n", out_final)

####################################
### 백프로파게이션 구현시 아래 주석 해제 ####
####################################
#%% backward
# dout = np.ones_like(out_final)
# dout = dout.transpose(0,2,3,1).reshape(-1, FN)

###############################
######### your code ###########
###############################
# db = None
# dcol_W = None
# dW = dcol_W.transpose(1, 0).reshape(FN, C, FH, FW)
# dcol = None
# ###############################
# dx = col2im(dcol, x.shape, FH, FW, stride, pad)
# print("dW :\n", dW)
# print("db :\n", db)
# print("dx :\n", dx)


