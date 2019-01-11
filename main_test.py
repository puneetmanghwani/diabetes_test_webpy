#!/usr/bin/env python3

# In[4]:


import numpy as np
import pandas as pd




# In[2]:

class main_test:
	def __init__(self):
		self.df=pd.read_csv("pima-indians-diabetes-deepnet.csv")


# In[13]:


		self.df.head(15)


# In[14]:


		self.df.columns


# In[10]:


		from sklearn.tree import DecisionTreeClassifier


# In[11]:


		self.algo_DT=DecisionTreeClassifier()


# In[12]:


		from sklearn.model_selection import train_test_split


# In[15]:


		x_train,x_test,y_train,y_test=train_test_split(self.df[['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age']],self.df['diabetes'],test_size=0.1)


# In[16]:


		train_DT=self.algo_DT.fit(x_train,y_train)


# In[17]:


		self.prediction_DT=self.algo_DT.predict(x_test)


# In[44]:


		from sklearn.metrics import classification_report,confusion_matrix,accuracy_score


# 
# print('accuracy is ->',accuracy_score(y_test,prediction_DT))
# print('\n')
# print('classification_report is-> ')
# print(classification_report(y_test,prediction_DT))
# print('\n')
# print('confusion matrix is->')
# print(confusion_matrix(y_test,prediction_DT))
# 

# In[20]:


		from sklearn.ensemble import RandomForestClassifier


# In[21]:


		self.algo_RF=RandomForestClassifier(n_estimators=100)


# In[27]:


		self.train_RF=self.algo_RF.fit(x_train,y_train)


# In[28]:


		self.prediction_RF=self.train_RF.predict(x_test)


# print('accuracy is ->',accuracy_score(y_test,prediction_RF))
# print('\n')
# print('classification_report is-> ')
# print(classification_report(y_test,prediction_RF))
# print('\n')
# print('confusion matrix is->')
# print(confusion_matrix(y_test,prediction_RF))
# 

# In[30]:


		from sklearn.svm import SVC


# In[31]:


		self.algo_SVM=SVC()


# In[32]:


		self.train_SVM=self.algo_SVM.fit(x_train,y_train)


# In[33]:


		self.prediction_SVM=self.algo_SVM.predict(x_test)


# print('accuracy is ->',accuracy_score(y_test,prediction_SVM))
# print('\n')
# print('classification_report is-> ')
# print(classification_report(y_test,prediction_SVM))
# print('\n')
# print('confusion matrix is->')
# print(confusion_matrix(y_test,prediction_SVM))
# 

# In[35]:


		self.param_grid = {'C': [0.1,1, 10, 100, 1000], 'gamma': [1,0.1,0.01,0.001,0.0001], 'kernel': ['rbf']} 


# In[36]:


		from sklearn.model_selection import GridSearchCV


# In[37]:


		self.algo_GR_SVM= GridSearchCV(SVC(),self.param_grid,refit=True,verbose=3)


# In[38]:


		self.train_GR_SVM=self.algo_GR_SVM.fit(x_train,y_train)


# In[39]:


		self.prediction_GR_SVM=self.algo_GR_SVM.predict(x_test)


# print('accuracy is ->',accuracy_score(y_test,prediction_GR_SVM))
# print('\n')
# print('classification_report is-> ')
# print(classification_report(y_test,prediction_GR_SVM))
# print('\n')
# print('confusion matrix is->')
# print(confusion_matrix(y_test,prediction_GR_SVM))
# 

# In[61]:


#print('enter your input for diabetes')


# In[173]:


#		test_data= list(map(float,input('enter the preg,plas,pres,skin,test,mass,pedi and age').split()))


# In[174]:


#		test_data=pd.DataFrame(data=(np.array(test_data)).reshape((1,8)),columns=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age'])


# In[175]:


		


# In[184]:

#		flag=0
#		avg_prediction=int((prediction_by_DT+prediction_by_RF+prediction_by_GR_SVM)/2)
#		if(avg_prediction==1):
#		    print('yes you have diabetes')
#		    flag=1
#		else:
#		    print('no you don\'t have diabetes')


# In[ ]:
#		if flag==1:
#			import scrap
	def result(self,info):
		self.prediction_by_DT=self.algo_DT.predict([list(info)])
		self.prediction_by_RF=self.algo_RF.predict([list(info)])
		self.prediction_by_GR_SVM=self.algo_GR_SVM.predict([list(info)])	
		

		flag=0
		self.avg_prediction=int((self.prediction_by_DT+self.prediction_by_RF+self.prediction_by_GR_SVM)/2)




		  								    		    
		return(self.avg_prediction)



	#	if(self.avg_prediction==1):
	#		print('yes you have diabetes')
	#		flag=1
	#	else:
	#		print('no you don\'t have diabetes')
	#
	#
	#	if flag==1:
	#		import scrap








	



