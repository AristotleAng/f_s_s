import numpy as np
from operator import itemgetter
from .config import device
if device=='gpu':
    import tensorflow as tf

def fft_multiply(A, B,u):
    # 补零
    size = 1
    while size < len(A) + len(B) - 1:
        size *= 2
    
    if device=='cpu':
        # FFT计算
        fft_A = np.fft.fft(A, size)
        fft_B = np.fft.fft(B, size)
        # 逐点相乘
        fft_result = fft_A * fft_B
        # IFFT计算，得到乘法结果
        result = np.fft.ifft(fft_result).real
    elif device=='gpu':
        # FFT计算
        shape_a=len(A)
        shape_b=len(B)
        A = np.pad(A, (0, size - len(A)))
        B = np.pad(B, (0, size - len(B)))
        fft_A = tf.signal.fft(tf.constant(A,dtype=tf.complex64))
        fft_B = tf.signal.fft(tf.constant(B,dtype=tf.complex64))
        # 逐点相乘
        fft_result = fft_A * fft_B
        result = tf.signal.ifft(fft_result)[:shape_a+shape_b - 1]
        result = tf.math.real(result).numpy()
        
    # 四舍五入，处理浮点误差
    result = np.round(result).astype(int)
    
    return result[:u+1]

def fft_multiply_2d(A, B, u):
    # 获取A和B的shape
    shape_A = A.shape
    shape_B = B.shape
    
    # 补零，确保长度为2的幂
    size_x = 1
    size_y = 1
    while size_x < shape_A[0] + shape_B[0] - 1:
        size_x *= 2
    while size_y < shape_A[1] + shape_B[1] - 1:
        size_y *= 2
    
    # FFT计算
    if device=='cpu':
    
        fft_A = np.fft.fft2(A, s=(size_x, size_y))
        fft_B = np.fft.fft2(B, s=(size_x, size_y))

        # 逐点相乘
        fft_result = fft_A * fft_B

        # IFFT计算，得到乘法结果
        result = np.fft.ifft2(fft_result).real
        
    elif device=='gpu':
        a_padded = np.pad(A, ((0, size_x - shape_A[0]), (0, size_y - shape_A[1])))
        b_padded = np.pad(B, ((0, size_x - shape_B[0]), (0, size_y - shape_B[1])))
        fft_A=tf.signal.fft2d(tf.constant(a_padded,dtype=tf.complex64))
        fft_B=tf.signal.fft2d(tf.constant(b_padded,dtype=tf.complex64))
        fft_result = fft_A * fft_B
        result = tf.math.real(tf.signal.ifft2d(fft_result))[:shape_A[0]+shape_B[0]-1,:shape_A[1]+shape_B[1]-1].numpy()
    
    # 四舍五入，处理浮点误差
    result = np.round(result).astype(int)
    
    return result[:u+1]
    
def MincowskySum(A,B,u):
    
    def trans(A):
        arr=np.zeros(max(A)+1)
        arr[A]=1
        return arr
    
    A_mul_B = fft_multiply(trans(A),trans(B),u)
    
    return np.array([i for i,v in enumerate(A_mul_B) if v>0])

def MincowskySum_2d(A,B,u):
    
    def trans(S):
        c1 = np.array(list(map(itemgetter(0),S)))
        c2 = np.array(list(map(itemgetter(1),S)))
        M = np.zeros((max(c1)+1,max(c2)+1))
        M[c1,c2] = 1
        return M
    
    A_mul_B = fft_multiply_2d(trans(A),trans(B),u)
    # print(A_mul_B)
    return np.array(list(
        zip(*np.nonzero(np.select([A_mul_B>0], [1])))
    ))