n=int(input("Enter integer "))
count=0
for i in range(2 , n//2):
  if(n%i != 0):
      continue
      count+=1     
  else:
      
      count+=1
      break
if(count>=0):
    print(n , " is not prime ")
else:
   print(n , " is prime")