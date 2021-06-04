import string

alphabet = " " + string.ascii_lowercase
print(alphabet)

positions = {" ": 0, "a": 1, "b": 2, "c": 3, "d": 4, "e": 5,
             "f": 6, "g": 7, "h": 8, "i": 9, "j": 10,
             "k": 11, "l": 12, "m": 13, "n": 14, "o": 15,
             "p": 16, "q": 17, "r": 18, "s": 19, "t": 20,
             "u": 21, "v": 22, "w": 23, "x": 24, "y": 25,
             "z": 26}

message = "hi my name is caesar"
new_message = ""
for i in message:
    x = positions[i]
    x += 1
    if x > 26:
        x -= 25
    new_message += alphabet[x]
print(new_message)


def encoding(message, int):
    encoded_message = ""
    for i in message:
        x = positions[i]
        x += int
        if x > 26:
            x = x - 26
            encoded_message += alphabet[x]
        elif x < 0:
            x = 26 + x
            encoded_message += alphabet[x]
        else:
            encoded_message += alphabet[x]
    return encoded_message


encode = encoding(message, 3)
print("encoded \n" + encode)
decoded = encoding(encode, -3)
print(decoded)