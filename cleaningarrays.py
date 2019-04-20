

#### FILTERING AND CLEANING ARRAYS
import numpy as np


def clean(income, age, sex):
    for i in range(len(income)):
        if income[i] == "Less than $10,000":
            income[i] =  5000.0
        elif income[i] == "$10,000 to $24,999":
            income[i] =  17500.0
        elif income[i] == "$25,000 to $49,999":
            income[i] =  37500.0
        elif income[i] == "$50,000 to $74,000":
            income[i] =  62500.0
        elif income[i] == "$75,000 to $99,999":
            income[i] =  87500.0
        elif income[i] == "$100,000 to $149,999":
            income[i] =  125000.0
        elif income[i] == "$150,000 or more":
            income[i] =  150000.0
        elif income[i] == "40,000 - $49,999":
            income[i] =  45000.0
        elif income[i] == "70,000 - $79,999":
            income[i] =  75000.0
        elif income[i] == "10,000 - $19,999":
            income[i] =  15000.0
        elif income[i] == "50,000 - $59,999":
            income[i] =  55000.0
        elif income[i] == "20,000 - $29,999":
            income[i] =  25000.0
        elif income[i] == "30,000 - $39,999":
            income[i] =  35000.0
        elif income[i] == "60,000 - $69,999":
            income[i] =  65000.0
        elif income[i] == "80,000 - $89,999":
            income[i] =  85000.0
        elif income[i] == "90,000 - $99,999":
            income[i] =  95000.0
        elif income[i] == "100,000 and up":
            income[i] =  100000.0
    
    for i in range(len(age)):
        if age[i] == "18-24":
            age[i] =  21.0
        elif age[i] == "25-34":
            age[i] = 29.5
        elif age[i] == "35-44":
            age[i] = 39.5
        elif age[i] == "45-54":
            age[i] = 49.5
        elif age[i] == "55-64":
            age[i] = 59.5
        elif age[i] == "65-74":
            age[i] = 69.5
        elif age[i] == "75 or older":
            age[i] = 75.0
        elif age[i] == "26-30":
            age[i] = 28.0
        elif age[i] == "61+":
            age[i] = 61.0
        elif age[i] == "22-25":
            age[i] = 23.5
        elif age[i] == "41-50":
            age[i] = 45.5
        elif age[i] == "31-40":
            age[i] = 35.5
        elif age[i] == "51-60":
            age[i] = 55.5
        elif age[i] == "18-21":
            age[i] = 19.5
            
    for i in range(len(sex)):
        if sex[i] == "Male":
            sex[i] = 0
        elif sex[i] == "Female":
            sex[i] = 1
    return income, age, sex
    #Normalizing Arrays from 0 to 1
'''
def normalize(income, howhappy, howsatisfied, howsafe, age)
       for this we have to do something like the following because there are some blank spaces:
            incomerange = np.max(income) - np.min(income)
            incomemin = np.min(income)
            for i in len(income)
                try:
                    income[i] = (income[i] - incomemin)/incomerange
                    


    income = (income-np.min(income))/((np.max(income))-np.min(income))
    howhappy = (howhappy-np.min(howhappy))/((np.max(howhappy))-np.min(howhappy))
    howsatisfied = (howsatisfied-np.min(howsatisfied))/((np.max(howsatisfied))-np.min(howsatisfied))
    howsafe = (howsafe-np.min(howsafe))/((np.max(howsafe))-np.min(howsafe))
    age = (age-np.min(age))/((np.max(age))-np.min(age))
    return income, howhappy, howsatisfied, howsafe, age
'''


        
