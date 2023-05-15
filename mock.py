# The objective of this code is to create a mock dataset to represent the grades of a class


# importing libraries
from faker import Faker
import pandas as pd
import numpy as np
import random as rd

# Creates a dataframe with 100 students with grades corresponding to 3 test and 2 quizes
fake = Faker()

fake_students = [[fake.name(),
                  rd.randint(80,99),
                  rd.randint(10,100),
                  rd.randint(30,90),
                  rd.randint(50,100), 
                  rd.randint(30,80)] for x in range(100)]

fake_columns = ['Nombre','Examen_1','Examen_2','Examen_3','Quiz_1', 'Quiz_2']

fake_df = pd.DataFrame(fake_students,columns = fake_columns)

fake_df.head(5)


fake_df2 = fake_df
fake_df2['Nota_final'] = fake_df.iloc[:,1:].mean(axis=1)
fake_df2.head()


fake_df2['Condicion'] = np.where(fake_df2['Nota_final'] >= 70,'aprobado', 'reprobado')


fake_df2.head()

fake_df2.to_csv('notas_falsas_100.csv', index= False)