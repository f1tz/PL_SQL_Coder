# -*-coding:utf-8-*-
# F1tz
key = 2333
plaintext = "user/password@server"
result = str(key)
i = 0
while i < len(plaintext):
    mask = ord(plaintext[i]) << 4
    n = (mask ^ (key + (i + 1) * 10)) + 1000
    result += str(n)
    i += 1
print(result)
