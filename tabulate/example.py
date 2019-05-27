#pandas dataframe as a nice text-based table with tabulate
#ref : https://pypi.org/project/tabulate/

from tabulate import tabulate
import pandas as pd

df = pd.DataFrame({'col_two' : [0.0001, 1e-005 , 1e-006, 1e-007],'column_3' : ['ABCD', 'ABCD', 'long string', 'ABCD']})

print(tabulate(df,headers='keys', tablefmt='psql',colalign=("center","center","left")))

"""
+----+-----------+-------------+
|    |  col_two  |  column_3   |
|----+-----------+-------------|
| 0  |  0.0001   |    ABCD     |
| 1  |   1e-05   |    ABCD     |
| 2  |   1e-06   | long string |
| 3  |   1e-07   |    ABCD     |
+----+-----------+-------------+
"""

print(tabulate(df,showindex="never", headers='keys', tablefmt='psql',colalign=("center","left")))
"""
+-----------+-------------+
|  col_two  | column_3    |
|-----------+-------------|
|  0.0001   | ABCD        |
|   1e-05   | ABCD        |
|   1e-06   | long string |
|   1e-07   | ABCD        |
+-----------+-------------+
"""