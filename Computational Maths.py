import numpy as np;
#The output has been placed in comments.
y = np.linspace(0,20,11)
#array([ 0.,  2.,  4.,  6.,  8., 10., 12., 14., 16., 18., 20.])
print(y)
#array([ 2.,  2.,  4., 16.,  8., 18.,  6.]) 
y[[1,1,2,8,4,9,3]]
y_bool = y > 7
#array([False, False, False, False, False, False, False, False,  True, True,  True])
y_bool
#array([ 0.,  2.,  4.,  6.,  4.,  5.,  6.,  7.,  8.,  9., 10.])
y[y>7] = y[y>7]/2\n
#array([ 0.,  2.,  4.,  6.,  4.,  5.,  6.,  7.,  8.,  9., 30.])
y2[-1] = 30\n
#array([ 0.,  2.,  4.,  6.,  4.,  5.,  6.,  7.,  8.,  9., 30.])
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3])
a+b\n
#array([11, 22, 33, 44])
x = np.arange(-6,6).reshape(4,3)\n
a =np.array([1,2,3])
b =np.array([100])
c =np.array([1,2,3,4])
d =np.array([[10],[20],[30],[40]])
e =np.array([[3,2,1]])
f =np.array([[10000]])
g =np.array([[100],[200],[300]])"

d2 = np.array([[10, 1],[20, 2],[30, 3],[40, 4]])
d2
#((4, 2), (4, 3))

d2.shape, x.shape
#(4, 1)
d\n
d.shape














     "output_type": "execute_result"
    }
   ],
   "source": [
    "d"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "c3d3b069",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[-5, -3, -1],\n",
       "       [-2,  0,  2],\n",
       "       [ 1,  3,  5],\n",
       "       [ 4,  6,  8]])"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "x + a"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "9ef3173d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([[ 94,  95,  96],\n",
       "       [ 97,  98,  99],\n",
       "       [100, 101, 102],\n",
       "       [103, 104, 105]])"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"


     

     
  x + b 
    ((4, 1), (4, 3)) 
    d.shape, x.shape
   
       #array([[ 4,  5,  6],\n",
       #       [17, 18, 19],\n",
       #       [30, 31, 32],\n",
       #       [43, 44, 45]])"
 
    d + x
   ((1, 3), (4, 3)) 
    e.shape, x.shape  
    array([[-3, -3, -3],\n",
   #    [ 0,  0,  0], 
   #    [ 3,  3,  3], 
   #    [ 6,  6,  6]]) 
