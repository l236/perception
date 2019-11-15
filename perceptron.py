import torch
import numpy as np
from matplotlib import pyplot as plt
x=torch.tensor([[3,3],[4,3],[1,1]]).float()
y=torch.tensor([1,1,-1]).float()
w=torch.tensor([-1,5]).float()
b=torch.tensor(5).float()
lr=1
xp=x[:2]
xn=x[2:]
count=0
color=['blue','orange','green', 'red','purple','brown','pink','gray', 'olive', 'cyan',]
a=torch.tensor([0,1,2,3,4,5,6]).float()
while 1:
    flag=0
    for i in range(len(y)):
        if y[i]*(w@x[i]+b)<=0:
            w=w+lr*y[i]*x[i]
            b=b+lr*y[i]
            flag=1
            f=(-a*w[0]-b)/w[1]
            print(w,b)
            count+=1
            plt.plot(a.numpy(),f.numpy(),color=color[count%9], label=str(count%9))
            plt.scatter(xp[:,0],xp[:,1],color='r')
            plt.scatter(xn[:, 0], xn[:, 1], color='b')
            plt.title('using_format_string')
            plt.xlabel('some x numbers')
            plt.ylabel('some y numbers')
            plt.legend()
    if flag==0:
        break
print(count)
plt.show()