#https://www.e-olymp.com/uk/submissions/9842050
letters_list = set(input())
word = input()

if [c for c in word if c not in letters_list]:
    print('No')

else:
        print("Ok")