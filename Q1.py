#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def spirals(n_points, noise=.5):
    n = np.sqrt(np.random.rand(n_points,1)) * 200 * (2*np.pi)/180
    d1x = -np.cos(n)*n + np.random.rand(n_points,1) * noise
    d1y = np.sin(n)*n + np.random.rand(n_points,1) * noise
    return (np.vstack((np.hstack((d1x,d1y)),np.hstack((-d1x,-d1y)))), 
            np.hstack((np.zeros(n_points),np.ones(n_points))))

X, Y = spirals(100)

plt.title('train')
plt.plot(X[Y==0,0], X[Y==0,1], '.', label='A')
plt.plot(X[Y==1,0], X[Y==1,1], '.', label='B')
plt.legend()
plt.show()
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

def spirals(n_points, noise=.5):
    n = np.sqrt(np.random.rand(n_points,1)) * 200 * (2*np.pi)/180
    d1x = -np.cos(n)*n + np.random.rand(n_points,1) * noise
    d1y = np.sin(n)*n + np.random.rand(n_points,1) * noise
    return (np.vstack((np.hstack((d1x,d1y)),np.hstack((-d1x,-d1y)))), 
            np.hstack((np.zeros(n_points),np.ones(n_points))))

X, Y = spirals(100)

plt.title('train')
plt.plot(X[Y==0,0], X[Y==0,1], '.', label='A')
plt.plot(X[Y==1,0], X[Y==1,1], '.', label='B')
plt.legend()
plt.show()


# In[ ]:




