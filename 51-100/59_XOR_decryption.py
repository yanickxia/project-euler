__author__ = 'Yann'


def undecryption(to_undecryption: str, key: str):
    undecryption_result = []
    # key = key[::-1]
    count = 0
    for c in to_undecryption:
        # ord_c = ord(c)
        ord_c = int(c)
        ord_c ^= ord(key[count % len(key)])
        undecryption_result.append(chr(ord_c))
        count += 1
    return undecryption_result


chars = []
for i in range(0, 26):
    chars.append(chr(ord('a') + i))

all_keys = []

for i in range(0, 26):
    key = chars[i]
    for j in range(0, 26):
        key2 = key + chars[j]
        for k in range(0, 26):
            key3 = key2 + chars[k]
            all_keys.append(key3)

f = open("p059_cipher.txt")
line = f.readline()
decryptionValues = line.split(",")

# undecryptionValue = undecryption(decryptionValues, 'god')

# for key in all_keys:
#     flag = True
#     undecryptionValue = undecryption(decryptionValues, key)
#     for c in undecryptionValue:
#         if not ((ord(c) <= 112 and ord(c) >= 64) or (ord(c) <= 39 and ord(c) >= 41) or (ord(c) == 32)):
#             flag = False
#             break
#     if flag:
#         print(key)

undecryptionValue = undecryption(decryptionValues, 'god')

undecryptionValue  = [ ord(i) for i in undecryptionValue]
print(sum(undecryptionValue))