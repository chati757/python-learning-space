# import pandas package as pd 
import pandas as pd 
  
# Define a dictionary containing students data 
data = {'Name': ['Ankit', 'Amit', 'Aishwarya', 'Priyanka'], 
                'Age': [21, 19, 20, 18], 
                'Stream': ['Math', 'Commerce', 'Arts', 'Biology'], 
                'Percentage': [88, 92, 95, 70]} 
  
# Convert the dictionary into DataFrame 
df = pd.DataFrame(data, columns = ['Name', 'Age', 'Stream', 'Percentage']) 
  
print("Given Dataframe :\n", df) 
  
print("\nIterating over rows using iloc function :\n") 
  
# iterate through each row and select  
# 0th and 2nd index column respectively. 
for i in range(len(df)) : 
  print(df.iloc[i, 0], df.iloc[i, 2]) 

'''
Given Dataframe :
         Name  Age    Stream  Percentage
0      Ankit   21      Math          88
1       Amit   19  Commerce          92
2  Aishwarya   20      Arts          95
3   Priyanka   18   Biology          70

Iterating over rows using iloc function :

Ankit Math
Amit Commerce
Aishwarya Arts
Priyanka Biology
'''