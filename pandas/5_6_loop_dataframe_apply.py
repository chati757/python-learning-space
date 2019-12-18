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
  
print("\nIterating over rows using apply function :\n") 
  
# iterate through each row and concatenate 
# 'Name' and 'Percentage' column respectively. 
print(df.apply(lambda row: row["Name"] + " " + str(row["Percentage"]), axis = 1)) 

'''
Given Dataframe :
         Name  Age    Stream  Percentage
0      Ankit   21      Math          88
1       Amit   19  Commerce          92
2  Aishwarya   20      Arts          95
3   Priyanka   18   Biology          70

Iterating over rows using apply function :

0        Ankit 88
1         Amit 92
2    Aishwarya 95
3     Priyanka 70
dtype: object
'''