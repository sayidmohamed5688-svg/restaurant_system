import random
secret=random.randint(1,49)
iskuday=3
print("\n welcome guess game \n dhawan la furay")
while iskuday>0:
  guess=int(input("enter your number"))
  if guess==secret:
    print("waa sax")
    break
  
  else:
     iskuday-=1
     print(f"qalad mrkle try {iskuday} ")
     if iskuday ==0:
      print(f"over ,  watan jawaabtu {secret}")
     