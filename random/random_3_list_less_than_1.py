result = []

for i in range(100,-1,-1):
    for j in range((100 - i),-1,-1):
        num1 = i / 100.0
        num2 = j / 100.0

        k = 100 - i - j
        num3 = k / 100.0

        if num1 + num2 + num3 <= 1.001:
            result.append([num1, num2, num3])

#print(result)
print(len(result))
import pdb;pdb.set_trace()