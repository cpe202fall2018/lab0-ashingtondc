def weight_on_planets():
   # write your code here
   
   #ask for weight, store, and convert
   earthWeight = float(input('What do you weigh on earth? '))
   marsWeight = earthWeight * 0.38
   jupiterWeight = earthWeight * 2.34
   
   #print weights
   print("\nOn Mars you would weigh", round(marsWeight, 3), "pounds.\nOn Jupiter you would weigh", round(jupiterWeight, 3), "pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()