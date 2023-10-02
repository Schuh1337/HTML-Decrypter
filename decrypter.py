import urllib.parse

encrypted = '''HERE''' # <--- encrypted string here | example: '''%3c%21%44%4f%43%54%59%50%45%20%68%74%6d%6c%3e%0d%0a%3c%68%74'''
decrypt = urllib.parse.unquote(encrypted)

print(decrypt)
input()
