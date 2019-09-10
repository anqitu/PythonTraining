# Python Essential Training
# Module 12: Intro to Numpy, Matplotlib, Pandas
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Numpy demo

a = [3,4,5,6]
b = [6,5,4,3]
print(a+b)

a1 = np.array(a)
b1 = np.array(b)
print(a1+b1)

a1 * 2
a * 2

# a = [3,4,5,6,7,8]
# a1 = np.array(a)
# print(a1>5)
# b = filter(lambda x:x>5,a)
# print(list(b))


# Matplolib demo
x = np.linspace(0,4*np.pi,200)
y = np.sin(x)
plt.plot(x,y, 'or')
plt.title('Sin Curve')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Pandas demo
# https://data.gov.sg/dataset/government-fiscal-position-annual?view_id=d8d74a6d-ac54-4b85-a2ab-1f79a90c3894&resource_id=98856a60-33cd-482a-9dc4-1ed52e562d5d
import pandas as pd
data = pd.read_csv('government-expenditure-by-type.csv')
data.shape
data.info()
data.head(10)
data.tail()
data.columns
data.groupby(['type', 'category', 'class']).size()

subset = data[data['class'] == 'Direct Development']
subset = subset.set_index('financial_year')
subset[['amount']].plot(figsize=(15,8))
subset[['amount']].plot.bar()

plt.plot(subset.index, subset.amount)

data = pd.DataFrame(data = {'Name': ['A', 'B', 'C'],
                            'Height': [170, 160, 180]})

data.to_csv('text.csv')
