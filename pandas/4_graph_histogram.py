import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("https://raw.githubusercontent.com/prasertcbs/tutorial/master/mpg.csv")

#display all dataframe to histogram (per column)
dataframe.hist()

#display one column to histogram
dataframe['cty'].hist()

#in jupyter dataframe['cty'].hist(); #this ; meaning hide matplotlib in console (show graph only)

#display (make more detial) default is bins=10
dataframe['cty'].hist(bins=20)

#display 2 graph (cty and hwy) of dataframe
dataframe[['cty','hwy']].hist()

#remove grid on graph  and make another color and share axis of x
#share axis of x mean , make a same in all graph
dataframe[['cty','hwy']].hist(grid=False,color='orange',sharex=True)

#display histogram plot in overlap between two graph on one graph
dataframe[['cty','hwy']].plot.hist(alpha=.2)

#display kde or line of histogram
dataframe['cty'].plot.density()
#dataframe['cty'].plot.kde() # Is a same