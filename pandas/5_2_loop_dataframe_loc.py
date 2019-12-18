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
  
print("\nIterating over rows using loc function :\n") 
  
# iterate through each row and select  
# 'Name' and 'Age' column respectively. 
for i in range(len(df)) : 
  print(df.loc[i, "Name"], df.loc[i, "Age"])

'''
Given Dataframe :
         Name  Age    Stream  Percentage
0      Ankit   21      Math          88
1       Amit   19  Commerce          92
2  Aishwarya   20      Arts          95
3   Priyanka   18   Biology          70

Iterating over rows using loc function :

Ankit 21
Amit 19
Aishwarya 20
Priyanka 18
'''