import urllib.parse
import os
encrypted = '''HERE''' # <-- Your encrypted string here | example: '''%3c%21%44%4f%43%54%59%50%45%20%68%74%6d%6c%3e%0d%0a'''
decrypt = urllib.parse.unquote(encrypted)
path = 'decrypted.txt'
with open(path, 'w') as file:
    file.write(decrypt)
print(f"Decrypted code has been saved to {os.path.abspath(path)}")
input()
