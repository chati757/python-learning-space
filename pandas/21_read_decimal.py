import pandas as pd
from decimal import Decimal, InvalidOperation

# ฟังก์ชันแปลงค่าจาก string → Decimal ปลอดภัย
def to_decimal(val):
    try:
        return Decimal(str(val)) if pd.notna(val) else pd.NA
    except (InvalidOperation, TypeError):
        return pd.NA

# โหลดข้อมูลและแปลงทันที
df = pd.read_csv("test_decimal.csv", converters={
    'amount': to_decimal,
    'price': to_decimal
})

import pdb;pdb.set_trace()

# คำนวณ total cost ด้วย Decimal
df['total_cost'] = df.apply(
    lambda row: row['amount'] * row['price'] if pd.notna(row['amount']) and pd.notna(row['price']) else pd.NA,
    axis=1
)

print(df)
