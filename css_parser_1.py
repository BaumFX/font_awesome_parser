#note: probably really shitty inefficient implementation but it worked for me :flushed:
import os
import sys
import time
import urllib.request
import os.path

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

file_path = "input1.css"
base_url = "https://kit-free.fontawesome.com/"

content = ""
content_to_write = ""

with open(file_path, 'r') as content_file:
    content = content_file.read()

iterator = 0
content_to_write = content

for position in find_all(content, "../../../"):
    result = ""
    substr = content[position + 9 : position + 150]
    for char in substr:
        if(char is not '"'):
            result += char
        else:
            break

    if result.startswith("../../../"):
        result = result[10:]

    link = base_url + result

    extension = os.path.splitext(result)[1]

    extra_extension = ""

    if(extension[-6:] == "#iefix"):
        extension = extension[:-7]
        extra_extension = ".iefix"

    if(extension[-12:] == "#fontawesome"):
        extension = extension[:-13]
        extra_extension = ".fontawesome"

    save_path = "C:\\output_path\\f1\\" + str(iterator) + extra_extension + extension

    search = "\"../../../" + result + "\""
    target = "\"f1/" + str(iterator) + extra_extension + extension + "\""

    urllib.request.urlretrieve(link, save_path)

    content_to_write = content_to_write.replace(search, target, 1)
    print("replacing link #" + str(iterator))
    iterator += 1

f = open(file_path, "w")
f.write(content_to_write)
f.close()
