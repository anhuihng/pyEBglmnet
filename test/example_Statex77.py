##
import numpy as np
from EBglmnet import cv_EBglmnet
import pandas as pd
##

baseDataDir = './data/'
# Read the CSV file using pandas
df = pd.read_csv(baseDataDir + 'statex77.csv')

y = df['Life Exp']
X = df[['Population', 'Income', 'Illiteracy', 'Murder', 'HS Grad', 'Frost', 'Area']]

ave = np.mean(y)
yBinary = [1 if y[i] >=ave else 0 for i in range(len(y))]
##
# Linear Regression Model 1: lasso prior
family = "gaussian"
prior = "lasso"
output = cv_EBglmnet(X, y, family= family, prior=prior, kFolds = 5,verbose =1)
print(output['fit'] )

##
# Linear Regression Model 2: lassoNEG prior
family = "gaussian"
prior = "lassoNEG"
output = cv_EBglmnet(X, y, family= family, prior=prior, kFolds = 5,verbose =0)
print(output['fit'] )
##
# Linear Regression Model 3: elastic net prior
family = "gaussian"
prior = "elastic net"
output = cv_EBglmnet(X, y, family= family, prior=prior, kFolds = 5,verbose =1)
print(output['fit'] )


##
# Logistic Regression Model 1: lasso prior
family = "binomial"
prior = "lasso"
output = cv_EBglmnet(X, yBinary, family= family, prior=prior, kFolds = 5,verbose =1)
print(output['fit'] )

##
# Logistic Regression Model 2: lassoNEG prior
family = "binomial"
prior = "lassoNEG"
output = cv_EBglmnet(X, yBinary, family= family, prior=prior, kFolds = 5,verbose =0)
print(output['fit'] )
##
# Logistic Regression Model 3: elastic net prior
family = "binomial"
prior = "elastic net"
output = cv_EBglmnet(X, yBinary, family= family, prior=prior, kFolds = 5,verbose =1)
print(output['fit'] )
