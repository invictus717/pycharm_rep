import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

TRAIN_URL="http://download.tensorflow.org/data/iris_training.csv"
train_path=tf.keras.utils.get_file(TRAIN_URL.split('/')[-1],TRAIN_URL)

COLUMN_NAMES=['SepalLength','SepalWidth','PetalLength','PetalWidth','Spices']
df_iris=pd.read_csv(train_path,names=COLUMN_NAMES,header=0)
iris=np.array(df_iris)
for i in range(4):
    for j in range(4):
        plt.subplot(4,4,4*i+(j+1))
        if(i==j):
            plt.text(0.3,0.4,COLUMN_NAMES[i],fontsize=8)
        else:
            plt.scatter(iris[:,j],iris[:,i],c=iris[:,4],cmap='brg')
        if(i==0):
            plt.title(COLUMN_NAMES[j])
        if(j==0):
            plt.ylabel(COLUMN_NAMES[i])
plt.tight_layout()
plt.show()