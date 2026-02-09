#TempConvert.py
#Name: Jenna Kramer
#Date: 02/08/26
#Assignment:Lab 3


def main():
  #Prompt the user for a Fahrenheit temperature
  #Convert that temperature to celsius, rounding to 1 decimal percision
  #Output converted temperature.
  tempF = int(input("Please provide me a temperature in Fahrenheit."))
  #tempF = 80 

  tempC = (tempF - 32) * 5/9

  roundedTempC = round(tempC,1)


  print(tempF, "degrees fahrenheit is ", roundedTempC, "degrees celsius.")
if __name__ == '__main__':
  main()
