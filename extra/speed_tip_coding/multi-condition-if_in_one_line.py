'''
#original
def grading(score):
    if(score >= 80):
        grade = 'a'
    elif(score >= 70):
        grade = 'b'
    elif(score >= 60):
        grade = 'c'
    elif(score >= 50):
        grade = 'd'
    else:
        grade = 'f'
    return grade
'''

def grading2(score):
    return 'fdcbaa'[score//10-4] if 50 <= score <= 100 else 'f'
