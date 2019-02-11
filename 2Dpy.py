#!/usr/bin/env python
# coding: utf-8

# In[1]:


hetero=False
inputfile1="spec.csv"

#hetero=True
#inputfile1="spec1.csv"
#inputfile2="spec2.csv"

dynamic=True
num_contour=16


# In[2]:


get_ipython().run_line_magic('matplotlib', 'inline')
import math
import numpy
import pandas
from matplotlib import pyplot


# In[3]:


def contourplot(sp):
 x=sp.columns[0:].astype(float)
 y=sp.T.columns[0:].astype(float)
 z=sp
 pyplot.figure(figsize=(4,4))
 pyplot.contour(x,y,z,num_contour,colors='black',linewidths=0.5,linestyles='solid')
 pyplot.pcolormesh(x,y,z,cmap='jet')


# In[4]:


def specread(inputfile):
 sp=pandas.read_csv(inputfile)
 sp=sp.rename(columns={'Unnamed: 0':''})
 sp=sp.set_index('')
 sp=sp.T
 if dynamic:
  sp=sp-sp.mean()
 return sp


# In[5]:


# file read
spec1=specread(inputfile1)
if hetero==False:
 inputfile2=inputfile1
spec2=specread(inputfile2)   


# In[6]:


# synchronous correlation
sync=spec1.T.dot(spec2.values)/(len(spec1)-1)
sync.columns=spec2.columns
sync=sync.T
contourplot(sync)
sync.to_csv(inputfile1[:len(inputfile1)-4]+'_sync.csv')


# In[7]:


# Hilbert-Noda transformation matrix
noda=numpy.zeros((len(spec1),len(spec1)))
for i in range(len(spec1)):
 for j in range(len(spec1)):
  if i!=j:
   noda[i,j]=1/math.pi/(j-i)


# In[8]:


# asynchronous correlation
asyn=pandas.DataFrame(noda).dot(spec2.values)
asyn=spec1.T.dot(asyn.values)/(len(spec1)-1)
asyn.columns=spec2.columns
asyn=asyn.T
contourplot(asyn)
asyn.to_csv(inputfile1[:len(inputfile1)-4]+'_async.csv')

