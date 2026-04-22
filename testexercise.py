sentence = "mang kasir aplikasi sederhana"
total_words = 1
total_characters = 0
for characters in sentence:
    if characters == (" "):
        total_words += 1
    if characters != (" "):
        total_characters +=1
print(f"there are {total_words} words in your sentence")
print(f"there are {total_characters} characters in your sentence")
print()
for i in range (4):
    for j in range (5):
        if (j == 2):
            print("0",end=" ")
        else:
         print("x",end=" ")
    print(" ")
print()
for i in range (4):
    for j in range (5):
        if (j == 2):
            print("0",end=" ")
        elif(i==2 or i == 1) and (j == 1 or j ==3):
            print("0",end=" ")
        else:
            print("x",end=" ")
    print(" ")