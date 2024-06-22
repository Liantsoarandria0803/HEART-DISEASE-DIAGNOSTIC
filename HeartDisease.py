import numpy as np
import matplotlib.pyplot as plt
class RandriaMlp :
     
     def cost_function(A, y):
        eps=10**(-4)
        L = 1 / 4 * np.sum(-y * np.log(A+eps) + (1 - y) * np.log(1 - A+eps))
        return L
     def initial(dimension):
         C=len(dimension)
         parameters={}
         for i in range (1,C):
             parameters['W'+str(i)]=np.random.randn(dimension[i],dimension[i-1])
             parameters['b'+str(i)]=np.random.randn(dimension[i],1)
         return parameters
     def fowardpropagation(X, parameters):
         C=len(parameters) // 2
         activation={'A0' : X}
         for i in range (1,C+1):
             Z=parameters['W'+str(i)].dot(activation['A'+str(i-1)])+parameters['b'+str(i)]
             activation['A'+str(i)]=1/(1+np.exp(-Z))
         return activation
     def backpropagation(X, y, activation, parameters):
         m=y.shape[1]
         c=len(parameters)//2
         dZ=activation['A'+str(c)]-y
         gradients={}
         for i in reversed(range(1,c+1)):
             gradients['dW'+str(i)]=1/m*np.dot(dZ,activation['A'+str(i-1)].T)
             gradients['db'+str(i)]=1/m*np.sum(dZ,axis=1,keepdims=True)
             if i > 1 :
                 dZ=np.dot(parameters['W'+str(i)].T,dZ)*activation['A'+str(i-1)]*(1-activation['A'+str(i-1)])
         return gradients

     def update(gradients, parameters,lr):
         C=len(parameters)//2
         for c in range(1,C+1):
             parameters['W'+str(c)]=parameters['W'+str(c)]-lr*gradients['dW'+str(c)]
             parameters['b'+str(c)]=parameters['b'+str(c)]-lr*gradients['db'+str(c)]
         return parameters


     def predict(X,parameters):
         c=len(parameters)//2
         activation=RandriaMlp.fowardpropagation(X,parameters)
         Afinal=activation['A'+str(c)]
         return Afinal >= 0.5


     def artificial_neuron(X, y,listrnn, lr=0.1, n=1000):
         np.random.seed(0)
         ##initialisena
         dimensions=list(listrnn)
         dimensions.insert(0,X.shape[0])
         dimensions.append(y.shape[0])
         parameters=RandriaMlp.initial(dimensions)
         C=len(parameters) // 2
         train_loss = []
         ##accuracy = []
         for i in range(n):
             activation = RandriaMlp.fowardpropagation(X, parameters)
             gradients =RandriaMlp.backpropagation(X, y,activation,parameters)
             parameters = RandriaMlp.update(gradients, parameters, lr)
             if i % 10 == 0:
                 train_loss.append(RandriaMlp.cost_function(y, activation['A'+str(C)]))
                 y_pred=RandriaMlp.predict(X,parameters)
                ## accuracy.append(recall_score(y_pred.flatten(),y.flatten())*100)
         print("Learning accomplished!!")
         print("loss:")
         print(train_loss[-1])
         print("\n\n")
         print("PREDICTION AFTER LEARNING:")
         print(y_pred)
         print(" with :\n  False = 0 \n True =1")
         print("\n ")
        #  plt.figure(figsize=(14,4))
        #  plt.subplot(1,2,1)
        #  plt.plot(train_loss,label='Train loss',c='red')
        ## plt.subplot(1,2,1)
        ## plt.plot(accuracy,label='Accuracy',c='green')
        ## plt.legend()
         plt.show()
         return parameters
## DATA PREPARING
##heart disease data
import pandas as pd
dataheart=pd.read_csv('./data/heart.csv')
Xhts=np.array(dataheart.drop('target',axis=1))
Xh=Xhts.T
yh=np.array(dataheart['target'])
yh=yh.reshape((1,yh.shape[0]))
param4=RandriaMlp.artificial_neuron(Xh,yh,(1000,224,224),lr=0.011, n=400)
cli=pd.read_json('requestData.json')
x=np.array([[int(cli.data.age),int(cli.data.sex),int(cli.data.cp),float(cli.data.trestbps),float(cli.data.chol),int(cli.data.fbs),int(cli.data.restecg),float(cli.data.thalach),int(cli.data.exang),int(cli.data.oldpeak),int(cli.data.slope),int(cli.data.ca),int(cli.data.thal)]])
x=x.T
b=RandriaMlp.predict(x,param4)
b=b[0][0]
print("Statement:")
print(b)
if b == 0 :
    print("\n\nDuring my analysis ,{} ,Good News !! , You don't have heart disease".format(cli.data.nom))
else:
    print("\n During my analysis, {} this is bad news for you , and I'm afraid to say that you have heart disease ,please consult a doctor".format(cli.data.nom))