import string

uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)

message = list(input("Enter a message to encrypt\n"))
shift = int(input("Enter the amount to shift: "))

for i in range(len(message)):
    if message[i] in uppercase:
        index = uppercase.index(message[i])
        new_index = index + shift
        if new_index > 22:
            new_index = new_index - 23
        message[i] = uppercase[new_index]
    elif message[i] in lowercase:
        index = lowercase.index(message[i])
        new_index = index + shift
        if new_index > 22:
            new_index = new_index - 23
        message[i] = lowercase[new_index]
    else:
        continue

print("".join(message))