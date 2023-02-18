user_input = input("Input: ")

user_output = ""
for i in user_input:
    if i not in "aeiouAEIOU":
        user_output = user_output + i

user_input = user_output

print("Output: " + user_input)