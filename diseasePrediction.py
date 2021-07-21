import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from statistics import mean
from sklearn.model_selection import train_test_split, cross_val_score

def predictDisease(psymptoms):

	df=pd.read_csv("Dataset/dis_sym_dataset_norm.csv")
	X = df.iloc[:, 1:]
	diseases = df.iloc[:, 0:1]
	#print(diseases)
	Y=list(diseases['label_dis'])
	#print(Y)
	dataset_symptoms = list(X.columns)
	
	sample_x = [0 for x in range(0,len(dataset_symptoms))]
	for val in psymptoms:
	    sample_x[dataset_symptoms.index(val)]=1

	lr = LogisticRegression()
	lr = lr.fit(X, Y)
	if(len(psymptoms)>=3):
		prediction = lr.predict([sample_x])
		return prediction[0]
	else :
		return 'Please Enter at least 3 symptoms...'