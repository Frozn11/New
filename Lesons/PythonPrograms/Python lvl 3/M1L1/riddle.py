def solev_riddle():
 for candies in range(1,100):
  if candies % 2 == 1 and candies % 3 == 1:
   return candies 
  return -1
 

result = solev_riddle()
print(f'да у гнома {result} шоколад')