camelCase = input("camelCase: ")
word_list = [camelCase[0].lower()]
for i in camelCase[1:]:
    if i in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        word_list.append('_')
        word_list.append(i.lower())
    else:
        word_list.append(i)

snake_case = ''.join(word_list)
print("snake_case: " + snake_case)


