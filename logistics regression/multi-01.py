import tensorflow as tf
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

TRAIN_URL="http://download.tensorflow.org/data/iris_training.csv"
train_path=tf.keras.utils.get_file(TRAIN_URL.split('/')[-1],TRAIN_URL)

df_iris=pd.read_csv(train_path,header=0) 
iris=np.array(df_iris)
train_x=iris[:,0:2]
train_y=iris[:,4]
x_train=train_x[train_y < 2 ]
y_train=train_y[train_y < 2 ]
num=len(x_train)
np.random.seed(612)
W=tf.Variable(np.random.randn(3,1),dtype=tf.float32)
cm_pt=mpl.colors.ListedColormap(["blue","red"])
x_=[-1.5,1.5]
y_=-(W[0]+W[1]*x_)/W[2]

plt.scatter(x_train[:,0],x_train[:,1],c=y_train,cmap=cm_pt)
plt.plot(x_,y_,color='red',linewidth=3)
plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1-5])
lean_rate=0.2
iter=120
display_step=30
x0_train=np.ones(num).reshape(-1,1)
X=tf.cast(tf.concat((x0_train,x_train),axis=1),tf.float32)
Y=tf.cast(y_train.reshape(-1,1),tf.float32)

ce=[]
acc=[]
for i in range(0,iter+1):
    with tf.GradientTape() as tape:
        PRED=1/(1+tf.exp(-tf.matmul(X,W)))
        Loss=-tf.reduce_mean(Y*tf.math.log(PRED)+(1-Y)*tf.math.log(1-PRED))
    accuracy=tf.reduce_mean(tf.cast(tf.equal(tf.where(PRED.numpy()<0.5,0.,1),Y),tf.float32))
    ce.append(Loss)
    acc.append(accuracy)
    
    dL_dW=tape.gradient(Loss,W)
    W.assign_sub(lean_rate*dL_dW)
    
    if i % display_step ==0:
        print("i: %i ,Acc:%f, Loss: %f" % (i,accuracy,Loss))
        y_=-(W[0]+W[1]*x_)/W[2]
        plt.plot(x_,y_)
plt.show()