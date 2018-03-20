import re

cipher = {'01':'P', '05':'a', '10':'s', '02':'W', '11':'o', '09':'R', '12':'d'}
values_from_doc = []
password = ''

document = open('2017overwiew.txt').readlines()
regex_pattern = re.compile('-\d\d')

for line in document:
    doc_string = ''.join(document)
    searching = regex_pattern.findall(doc_string)

for elem in searching:
    new_string = elem.replace('-', '')
    values_from_doc.append(new_string)

for k,v in cipher.items():
    for i in values_from_doc:
        if i == k:
            password += v

print('\nYour password hidden in .txt doc is: ' + password)