import pandas as pd

dataframe = pd.read_csv("https://raw.githubusercontent.com/prasertcbs/tutorial/master/mpg.csv")
print(dataframe.head()) #show first 5 row
#print(dataframe.tail()) #show last 5 row
print(dataframe.shape) #show number of row and number of colum (in tuple type)

print(dataframe.info()) #show information of dataframe
"""
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 234 entries, 0 to 233
Data columns (total 11 columns):
manufacturer    234 non-null object
model           234 non-null object
displ           234 non-null float64
year            234 non-null int64
cyl             234 non-null int64
trans           234 non-null object
drv             234 non-null object
cty             234 non-null int64
hwy             234 non-null int64
fl              234 non-null object
class           234 non-null object
dtypes: float64(1), int64(4), object(6)
memory usage: 20.2+ KB
None
"""

print(dataframe.sample(5)) #randomly data 5 rows
"""
    manufacturer              model  displ  year  cyl       trans drv  cty  hwy fl    class
171       subaru        impreza awd    2.5  2008    4  manual(m5)   4   19   25  p  compact
48         dodge  dakota pickup 4wd    3.7  2008    6  manual(m6)   4   15   19  r   pickup
45         dodge        caravan 2wd    3.8  1999    6    auto(l4)   f   15   21  r  minivan
85          ford    f150 pickup 4wd    4.6  1999    8  manual(m5)   4   13   16  r   pickup
141       nissan             altima    2.4  1999    4  manual(m5)   f   21   29  r  compact
"""
print(dataframe.sample(frac=.1)) #randomly 10% of dataframe
"""
    manufacturer                model  displ  year  cyl       trans drv  cty  hwy fl   class
54         dodge    dakota pickup 4wd    4.7  2008    8    auto(l5)   4    9   12  e  pickup
59         dodge          durango 4wd    4.7  2008    8    auto(l5)   4    9   12  e     suv
65         dodge  ram 1500 pickup 4wd    4.7  2008    8    auto(l5)   4    9   12  e  pickup
69         dodge  ram 1500 pickup 4wd    4.7  2008    8  manual(m6)   4    9   12  e  pickup
126         jeep   grand cherokee 4wd    4.7  2008    8    auto(l5)   4    9   12  e     suv
"""
#frequency
print(dataframe['manufacturer'].value_counts())
"""
dodge         37
toyota        34
volkswagen    27
ford          25
chevrolet     19
audi          18
subaru        14
hyundai       14
nissan        13
honda          9
jeep           8
pontiac        5
land rover     4
mercury        4
lincoln        3
"""
#transpose between row and column
print(dataframe.head().T)
"""
                     0           1           2         3         4
manufacturer      audi        audi        audi      audi      audi
model               a4          a4          a4        a4        a4
displ              1.8         1.8           2         2       2.8
year              1999        1999        2008      2008      1999
cyl                  4           4           4         4         6
trans         auto(l5)  manual(m5)  manual(m6)  auto(av)  auto(l5)
drv                  f           f           f         f         f
cty                 18          21          20        21        16
hwy                 29          29          31        30        26
fl                   p           p           p         p         p
class          compact     compact     compact   compact   compact
"""
#correlation of data (data must be int and float only)
print(dataframe.corr())
"""
          displ      year       cyl       cty       hwy
displ  1.000000  0.147843  0.930227 -0.798524 -0.766020
year   0.147843  1.000000  0.122245 -0.037232  0.002158
cyl    0.930227  0.122245  1.000000 -0.805771 -0.761912
cty   -0.798524 -0.037232 -0.805771  1.000000  0.955916
hwy   -0.766020  0.002158 -0.761912  0.955916  1.000000
"""
#find largest in top 5 of all dataframe
print(dataframe.nlargest(5,columns='cty'))
"""
    manufacturer       model  displ  year  cyl       trans drv  cty  hwy fl       class
221   volkswagen  new beetle    1.9  1999    4  manual(m5)   f   35   44  d  subcompact
212   volkswagen       jetta    1.9  1999    4  manual(m5)   f   33   44  d     compact
222   volkswagen  new beetle    1.9  1999    4    auto(l4)   f   29   41  d  subcompact
99         honda       civic    1.6  1999    4  manual(m5)   f   28   33  r  subcompact
196       toyota     corolla    1.8  2008    4  manual(m5)   f   28   37  r     compact
"""
#find smallest in top 5 of all dataframe
print(dataframe.nsmallest(5,columns='cty'))
"""
    manufacturer                model  displ  year  cyl       trans drv  cty  hwy fl   class
54         dodge    dakota pickup 4wd    4.7  2008    8    auto(l5)   4    9   12  e  pickup
59         dodge          durango 4wd    4.7  2008    8    auto(l5)   4    9   12  e     suv
65         dodge  ram 1500 pickup 4wd    4.7  2008    8    auto(l5)   4    9   12  e  pickup
69         dodge  ram 1500 pickup 4wd    4.7  2008    8  manual(m6)   4    9   12  e  pickup
126         jeep   grand cherokee 4wd    4.7  2008    8    auto(l5)   4    9   12  e     suv
"""
#concat dataframe
print(pd.concat([dataframe.head(3),dataframe.tail(3)])) #ps:focus num of row
"""
    manufacturer   model  displ  year  cyl       trans drv  cty  hwy fl    class
0           audi      a4    1.8  1999    4    auto(l5)   f   18   29  p  compact
1           audi      a4    1.8  1999    4  manual(m5)   f   21   29  p  compact
2           audi      a4    2.0  2008    4  manual(m6)   f   20   31  p  compact
231   volkswagen  passat    2.8  1999    6    auto(l5)   f   16   26  p  midsize
232   volkswagen  passat    2.8  1999    6  manual(m5)   f   18   26  p  midsize
233   volkswagen  passat    3.6  2008    6    auto(s6)   f   17   26  p  midsize
"""
#sort values
print(dataframe['displ'].head().sort_values())
"""
0    1.8
1    1.8
2    2.0
3    2.0
4    2.8
Name: displ, dtype: float64
"""
