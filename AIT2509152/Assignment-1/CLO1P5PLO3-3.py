import string

palindrome = input("Insert a word to check if it's a palindrome or not: ").lower().strip()
for p in string.punctuation:
    palindrome = palindrome.replace(p,'')
clean = palindrome.replace(' ','')

def palindromechecker():
    for i in range(len(clean) // 2):
        if clean[i] == clean[-i-1]:
            continue
        else:
            return 0
    return 1

if palindromechecker():
    print(f"{palindrome} is a palindrome")
else:
    print(f"{palindrome} is not a palindrome")