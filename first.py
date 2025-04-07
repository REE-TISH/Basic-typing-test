from time import *
from faker import Faker

fake = Faker('en_US')
def generate_paragraph():
    word = []
    while len(word) < 50:
        para = fake.text().split()
        word.extend(para)
    trimmed = word[:50]
    return " ".join(trimmed)

paragraph = generate_paragraph()
print(paragraph)
paraList = paragraph.split()
start = time()
text = input("Start:").split()
end = time()
rightWords = 0
wrongWords = 0
for i in range(len(text)):
    if paraList[i] != text[i]:
        wrongWords += 1
    else:
        rightWords += 1 
time = end - start
wpm = int((rightWords/(end - start))*60)
if wpm == 0:
    print("Speed:",0,"accuracy:100%")
else:
    print("wpm:",wpm,"accuracy:",(rightWords/(rightWords + wrongWords))*100,"%")





