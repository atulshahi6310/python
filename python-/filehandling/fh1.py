file = open("text.txt" , "r"  )

line1 = file.readlines()

for line in range [0:2:1]:
      print(line.strip())
file.close()
