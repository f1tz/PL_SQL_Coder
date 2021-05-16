# -*-coding:utf-8-*-
# F1tz
with open('encrypted.txt', 'r', encoding='utf-8') as f:
    for cryptText in f:
        cryptText = cryptText.strip()
        plainText = ""
        values = []
        i = 0
        while i < len(cryptText):
            values.append(int(cryptText[i:i + 4]))
            i += 4
        key = values[0]
        del values[0]
        i = 0
        while (i < len(values)):
            val = values[i] - 1000
            mask = key + (10 * (i + 1))
            res = (val ^ mask) >> 4
            plainText += chr(res)
            i += 1
        print(plainText)

