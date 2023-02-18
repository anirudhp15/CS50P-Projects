def main():
    answer = input()
    print(convert(answer))

    
def convert(word):
    count1 = word.count(':)')
    count2 = word.count(':(')
    if (count1 != 0):
        word = word.replace(':)','🙂')
    if (count2 != 0):
        word = word.replace(':(','🙁')

    return word


main()