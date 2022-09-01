def encode(text, square):
    out = ''
    for i in range(len(square)):
        out += text[int(square[i]) - 1]
    print(out)
    return out


def decode(text, square):
    out = list(range(0, len(square)))
    for i in range(len(square)):
        out[int(square[i]) - 1] = text[i]
    return ''.join(out)


with open('input.txt', 'r', encoding='utf-8') as f:
    text = f.readline()[:-1]
    square = ''.join(f.read().splitlines())
    while len(text) < len(square):
        text += '_'

operation = input('Enter e for encoding, d for decoding: ')

with open('output.txt', 'w', encoding='utf-8') as f:
    if operation == 'e':
        f.write(encode(text, square))
    elif operation == 'd':
        f.write(decode(text, square))
    else:
        print('Wrong input!')
