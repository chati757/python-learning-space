import pandas as pd
from datetime import datetime

se = pd.Series({'date':datetime.now()},dtype="datetime64[ns]")

print(se)

print(se.date.to_pydatetime())