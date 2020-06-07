import pandas as pd
df1 = pd.DataFrame([['a', 1], ['b', 2]],columns=['letter', 'number'])
df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']],columns=['letter', 'number', 'animal'])

pd.concat([df1, df3], join="outer")

'''
default : concat : join = outer
default : concat : sort = false
__main__:1: FutureWarning: Sorting because non-concatenation axis is not aligned. A future version
of pandas will change to not sort by default.

To accept the future behavior, pass 'sort=False'.

To retain the current behavior and silence the warning, pass 'sort=True'.

output:

  animal letter  number
0    NaN      a       1
1    NaN      b       2
0    cat      c       3
1    dog      d       4

จะขึ้น warn เพราะ columns animal 
ปกติที่เป็น default concat ระหว่าง df1 กับ df3 จะเป็น inner นั้นหมายความว่า col ที่ติด NaN จะไม่แสดงตามที่เห็นด้านล่าง

pd.concat([df1, df3], join="inner")
  letter  number
0      a       1
1      b       2
0      c       3
1      d       4

แต่เมื่อเราระบุเป็น outer แม้จะมี NaN ปนใน series ของ col animal ก็จะเอา col animal มาแสดงแต่ระบบยังไม่รู้แน่ชัดว่าถ้าเกิด
เอามาแสดงแล้วควรแสดงแบบเรียง หรือ ไม่ต้องเรียงดี จึงขอความชัดเจนจากผู้เขียนโปรแกรมให้ระบุ Sort ด้วยเพื่อจะได้รู้ว่าควรเรียงหรือไม่เรียง
ดังนั้นหากเราระบุ Sort warn จะหายไป โดยเขามีเตือนไว้ว่า เวอร์ชั่นหน้าเนี่ยจะระบุ sort เป็น false เป็นค่าตั้งต้นนะ ระวังด้วย!

ในกรณี join เป็น outer และมีพวก NaN ปนใน row ของ col ใดก็ตามจะต้องเตือนผู้ใช้เพราะหากผู้เขียนโปรแกรมเปลี่ยนเป็น join = inner ขึ้นมา
รับรองว่าการเรียงตัวของ columns อาจเกิดความไม่แน่นอนขึ้นได้เพราะเมื่อปรับเป็น inner col animal จะไม่อยู่อันดับแรกอีกต่อไปใน columns แต่จะหายไปด้วย!
บางครั้งเราอาจอ้าง col animal หรือ อ้างอิง col แรกต่อจากการทำงานส่วนนี้อยู่เพราะคิดว่าเป็น animal col ยังอยู่ แต่พอมาตรวจอาจจะงงได้เพราะมันอาจหายไป
เนื่องจากระบุเป็น inner ดังนั้นจากส่วนนี้จึงสรุปได้ว่า join = inner คือความไม่แน่นอนระวังเรื่องการใช้ แม้ sort ก็ไม่อาจช่วยให้มันคงอยู่ไว้ได้ถ้า NaN ใน row ของ col นั้นเกิดขึ้น 

โดยระบบพิจารณาจากการเติอนจาก ขนาด col ที่ไม่ทำกันทั้ง 2 dataframe หรือ ขนาดเท่านั้นแต่ดันมีลำดับ columns ที่สลับกัน เช่น df1 columns มี a , b แต่ df2 columns มี b , a
เป็นต้น

ทางที่ดีควรระบุ sort ทุกกรณีที่เราใช้ concat ไปเลยจบ
'''