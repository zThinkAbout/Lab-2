import random
import xml.etree.ElementTree as ET

print("Task 1:")
s = [x.split(';') for x in open('books-en.csv')]
names = 0
for book in s[1:]:
    name = book[1]
    if len(name)>30:
        names+=1
print('There are ', names, ' books with a title longer than 30 symbols!')

print("Press Enter to launch Task 2")
ps = str(input())
print("Task 2:")
print('Input the name of the author: ')
requested = str(input()).strip()
reqbooks = []
for book in s[1:]:
    author  = book[2].strip()
    if author == requested and int(book[3]) < 1990:
        reqbooks.append(f'{book[1]} ({book[3]})')
print(f"Here are all of {requested}'s books written before 1990:")
for i in reqbooks:
    print(i)

print("")
print("Press Enter to launch Task 3")
ps = str(input())
print("Task 3 done")
recs = random.sample(s[1:], 20)
for i in range(len(recs)):
    rec = recs[i]
    author = rec[2].strip()
    name = rec[1]
    year = rec[3]
    recs[i] = f'{i+1}. {author}. {name} - {year}'
with open('library.txt', 'w') as f:
    for i in recs:
        f.write(i + '\n')

print("")
print("Press Enter to launch Task 4")
ps = str(input())
print("Task 4:")
tree = ET.parse('currency.xml')
root = tree.getroot()
print("Names of the currencies with nominal = 1:")
for currency in root.findall('Valute'):
    nominal = currency.find('Nominal').text
    name = currency.find('Name').text
    if nominal == '1':
        print(name)

print("")
print("Press Enter to launch Bonus Task 1")
ps = str(input())
print("Bonus Task 1:")
publishers = []
for book in s:
    publishers.append(book[4].strip())
publishers = sorted(list(set(publishers)))
for i in publishers: print(i)


print("")
print("Press Enter to launch Bonus Task 2")
ps = str(input())
print("Bonus Task 2:")
s = s[1:]
s.sort(key = lambda x: int(x[5]) if x[5].isdigit() and int(x[5])<1000 else 0, reverse=True)
for i in range(20):
    print(f'{i+1}. {s[i][1]} - Downloads: {s[i][5]}')