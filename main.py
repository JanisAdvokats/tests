num = input("cipars:")
import sys
print(sys.version)
if num.isnumeric() == True:
  if int(int(num)/2)*2 == int(num):
    print("para skaitlis")
  else:
    print("nepar skiatlis")
else:
  print("nav cipars")