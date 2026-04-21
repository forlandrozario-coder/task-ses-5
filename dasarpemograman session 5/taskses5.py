for i in range (5):
    for j in range (5):
        if (j == 2) or (i == 2):
         print("*", end = " ")
        else:         
         print("_", end = " ")
    print(" ")
print("------------------------------")
for i in range (5):
    for j in range (5):
        if (i == 0) or (i == 4) or (j == 0) or (j == 4):
         print("*", end = " ")
        else:         
         print("_", end = " ")
    print(" ")
print("------------------------------")
for i in range (5):
   for j in range (5):
       if (i == 0) or (i == 2) or (j == 0):
         print("0", end=" ")
       else:
         print("_", end=" ")
   print(" ")
print()
for i in range (5):
    for j in range (5):
        if (i == 0) or (i == 4) or (j == 0) or (j == 4):
         print("0", end = " ")
        else:         
         print("_", end = " ")
    print(" ")
print()
for i in range (5):
   for j in range (5):
      if (i<=1) or(j == i) or (j == 1-i-5) or (j == 0):
         print("0", end=" ")
      else:
         print("_", end=" ")
   print(" ")
print()
for i in range (5):
   for j in range (5):
      if (i == 4) or (j == 0):
         print("0", end=" ")
      else:
         print("_", end=" ")
   print(" ")
print()
for i in range (5):
   for j in range (5):
      if (j == 0) or (j == 4) or (i == 0) or (i ==2):
         print("0", end=" ")
      else:
         print("_", end=" ")
   print(" ")
print()
for i in range (5):
   for j in range (5):
      if (j == 0) or (j == 4) or (i == j):
         print("0", end=" ")
      else:
         print("_", end=" ")
   print(" ")