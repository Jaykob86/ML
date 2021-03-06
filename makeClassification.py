# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 00:35:18 2018

"""
from keras.models import load_model
import numpy as np
from keras.preprocessing.text import Tokenizer
import pandas as pd

classes = {'HRIS - Learning Link':0,'HRIS - CompetencePortal':1,
 'HRIS - Access Management':2,'HRIS - Legacy - AC Staff':3,
 'HRIS - Reporting & Analytics':4,'HRIS - Legacy - Absence-DB':5,
 'HRIS - Master Data Management':6,'HRIS - Legacy - NAV':7,
 'HRIS - Legacy - Employee Request- / DQM-':8,
 'HRIS - People Management':9,'HRIS - Mobile App':10,
 'HRIS - Time Off':11,'HRIS - Knowledge Management':12,
 'HRIS - Change Management':13,'HRIS - Legacy - Recruitment-DB':14,
 'HRIS - Legacy - IJM':15,'HRIS - Integrations':16,
 'HRIS - Travel & Expense':17,'HRIS - Payroll':18,'HRIS - Other':19}

model = load_model('text_classifier.h5')

def predict(str_query):

    X_raw_test = [str_query]
    x_test = tokenizer.texts_to_matrix(X_raw_test, mode='binary')
    prediction = model.predict(np.array(x_test))
    class_num = np.argmax(prediction[0])
    
    for name, index in classes.items():
        if index == class_num:
            print("%s: %f%% confidence" % (name, prediction[0][np.argmax(prediction)]*100))
    return prediction
