# encoding:utf-8
#author : Lenovo
#date: 2018/8/26
import sys
reload(sys)
sys.setdefaultencoding('gbk')
import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,100)
fig=plt.figure()

axl=fig.add_subplot(221)
y=x**2
axl.plot(x,y)

axl=fig.add_subplot(222)
axl.plot(x,-x)

axl=fig.add_subplot(223)
axl.plot(x,-x**2)

axl=fig.add_subplot(224)
axl.plot(x,-x/2)

plt.show()