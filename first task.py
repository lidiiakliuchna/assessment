from collections import Counter
string=input()
count=0

new_string=string.replace('a', '').replace('o', '').replace('u', '').replace('e', '').replace('i', '')
result = "".join(dict.fromkeys(new_string))
print(result)
for char in result:
    count+=1

print(count)



