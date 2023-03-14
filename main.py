import math

def getWeight():
  weight = float(input("Please enter your weight in pounds: "))
  return weight


def getHeight():
  inputString = input(
    "Please enter your height in feet and inches (ex: 5'8\"): ")
  splitString = inputString.split("'")
  feet = float(splitString[0])
  inches = float(splitString[1].strip('"'))
  height = (feet * 12) + inches
  return height


def calculateBMI(weight, height):
  ### Convert height(inches) to meters
  meterHeight = height * 0.0254
  ### Convert weight(pounds) to kilograms
  kilogramWeight = weight * 0.453592
  bmi = kilogramWeight / (meterHeight * meterHeight)
  return bmi


if __name__ == "__main__":
  print("Welcome to the BMI Calculator :)")

  weight = getWeight()
  height = getHeight()

  bmi = calculateBMI(weight, height)
  print(f"Your final BMI is: {round(bmi, 2)}")
