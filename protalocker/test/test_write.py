import pickle

# ข้อมูล dict
data = {
    'Forest': {'level': -1, 'parent': None, 'children': ['1', '5']},
    '1': {'b': 'test', 'level': 1, 'parent': 'Forest', 'children': ['2', '4']},
    '5': {'b': 'test', 'level': 1, 'parent': 'Forest', 'children': ['6']},
    '2': {'b': '1', 'level': 2, 'parent': '1', 'children': []},
    '4': {'b': 'test', 'level': 2, 'parent': '1', 'children': []},
    '6': {'b': 'test', 'level': 2, 'parent': '5', 'children': []}
}

# เขียนข้อมูลลงในไฟล์ pickle
with open('data.pkl', 'wb') as file:  # 'wb' หมายถึงเขียนแบบไบนารี
    pickle.dump(data, file)

print("Data has been written to 'data.pkl'")