test_str1="/meganmgaglio/collections/robots/page:1"
result=test_str1.find("page:")
print(result)
print(len("page:"))
print(result+len("page:"))
print(test_str1[38:])
print(test_str1[result+len("page:"):])

#-------------function type---------------

def cut_high_then(full_str,cut_str):
    finder=full_str.find(cut_str)
    result=full_str[finder+len(cut_str):]
    return result

def cut_low_then(full_str,cut_str):
    finder=full_str.find(cut_str)
    result=full_str[:finder+len(cut_str)]
    return result


print(cut_high_then("/meganmgaglio/collections/robots/page:1234","page:"))

print(cut_low_then("/meganmgaglio/collections/robots/page:1234","page:"))