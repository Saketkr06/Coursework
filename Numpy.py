#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#All about numpy arrays


# In[1]:


#creating numpy arrays
import numpy as np


# In[3]:


arr1=np.array([1,2,3,4])
arr1


# In[4]:


type(arr1)


# In[5]:


arr2=np.array([[1,2,3],[2,5,6]])
arr2


# In[6]:


arr3=np.zeros((2,3))
arr3


# In[7]:


arr4=np.ones((3,3))
arr4


# In[8]:


type(arr4)


# In[12]:


arr5=np.identity(5)
arr5


# In[13]:


arr6=np.arange(10)
arr6


# In[14]:


arr7=np.linspace(10,20,10)#equal length between no
arr7


# In[15]:


arr9=arr7.copy()


# In[16]:


arr1.shape


# In[17]:


arr2.shape


# In[18]:


arr10=np.array([[1,2,3],[4,5,6],[7,8,9]])
arr10
arr10.shape


# In[19]:


arr10.ndim


# In[20]:


arr10.size


# In[21]:


arr10.itemsize


# In[23]:


arr7.itemsize


# In[24]:


arr9.astype('int')#changing data type


# In[25]:


lista=range(100)
arr11=np.arange(100)


# In[26]:


import sys


# In[27]:


print(sys.getsizeof(87)*len(lista))


# In[28]:


print(arr11.itemsize*arr11.size)


# In[29]:


import time


# In[30]:


x=range(100000)
y=range(100000,200000)
start_time=time.time()

c=[(x,y) for x,y in zip(x,y)] #add twoo arrays in 1 array

print(time.time()-start_time)


# In[32]:


a=np.arange(100000)
b=np.arange(100000,200000)
start_time=time.time()
c=a+b
print(time.time()-start_time)


# In[34]:


arr12=np.arange(24).reshape(6,4)
arr12


# In[36]:


arr12[2]


# In[37]:


arr12[:,2]


# In[40]:


arr12[:,2:4]


# In[41]:


arr12[2:4,1:3]


# In[42]:


arr12[4:6,2:4]


# In[43]:


for i in arr12:
    print(i)


# In[44]:


for i in np.nditer(arr12):
    print(i)


# In[45]:


arr1=np.array([1,2,3,4,5,6])
arr2=np.array([4,5,6,7,8,9])


# In[46]:


arr2-arr1


# In[47]:


arr1*arr2


# In[48]:


arr2>3


# In[51]:


arr3=np.arange(6).reshape(2,3)
arr4=np.arange(6,12).reshape(3,2)


# In[53]:


arr3.dot(arr4)


# In[54]:


arr4.max()


# In[56]:


arr4


# In[55]:


arr4.min(axis=0)


# In[57]:


arr4.min(axis=1)


# In[58]:


arr4.sum()


# In[59]:


arr4.sum(axis=0)#axis =0 gives column


# In[60]:


arr4.mean()


# In[62]:


arr4.std()


# In[63]:


np.median(arr4)


# In[64]:


arr4.std(axis=1)


# In[66]:


np.exp(arr4)


# In[67]:


#ravel fn converts higher d to 1d
arr4.ndim


# In[68]:


arr4.ravel()


# In[69]:


arr4.transpose()


# In[70]:


arr3


# In[71]:


arr5=np.arange(12,18).reshape(2,3)
arr5


# In[72]:


arr4


# In[73]:


np.hstack((arr3,arr5)) #keeping no of rows common


# In[74]:


np.vstack((arr3,arr5)) #keeping no of columns common


# In[75]:


np.hsplit(arr3,3)


# In[76]:


arr3


# In[77]:


np.vsplit(arr3,2)


# In[78]:


arr8=np.arange(24).reshape(6,4)
arr8


# In[79]:


arr8[[0,2,4]]


# In[80]:


arr12=np.random.randint(low=1,high=100,size=20).reshape(4,5)
arr12


# In[81]:


arr12>50


# In[84]:


arr12[arr12>50] #indexing using boolean array


# In[86]:


arr12[(arr12>50) & (arr12%2!=0)]


# In[87]:


arr12[(arr12>50) & (arr12%2!=0)]=0


# In[88]:


arr12


# In[89]:


#plotting graph
x=np.linspace(-40,40,100)


# In[91]:


x.size


# In[92]:


y=np.sin(x)


# In[93]:


y.size


# In[96]:


#to show graph
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[97]:


plt.plot(x,y)


# In[98]:


y=x*x+2*x+6


# In[101]:


plt.plot(x,y)


# In[102]:


#broad casting heps in operation of disimilar arrays


# In[103]:


np.random.random()


# In[104]:


np.random.seed(1) #same random value between rang(0,1)


# In[105]:


np.random.random()


# In[106]:


np.random.random()


# In[107]:


np.random.uniform(3,10)


# In[108]:


np.random.uniform(3,10)


# In[110]:


np.random.uniform(1,100,10).reshape(2,5)


# In[113]:


np.random.randint(1,10)


# In[115]:


np.random.randint(1,10,15).reshape(3,5)


# In[116]:


a=np.random.randint(1,10,6)
a


# In[117]:


np.max(a)


# In[118]:


#arg max fn gives indes of max fn
np.argmax(a)


# In[119]:


np.argmin(a)


# In[120]:


a=np.random.randint(1,10,6)
a


# In[121]:


a[a%2==1]=-1
a


# In[126]:


a=np.random.randint(1,50,6)
a


# In[127]:


np.where(a%2==1,-1,a) #doesnot change the array(conditon,True,False)


# In[128]:


a


# In[129]:


a=np.sort(a)
a


# In[130]:


np.percentile(a,25) #percentile of array


# In[131]:


np.percentile(a,50)


# In[132]:


np.percentile(a,100)


# In[ ]:




