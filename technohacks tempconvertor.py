def convert_temp(temp, unit):
  """
  Converts a temperature from Fahrenheit to Celsius or vice versa.

  Args:
    temp: The temperature to convert.
    unit: The unit of the temperature ("F" for Fahrenheit, "C" for Celsius).

  Returns:
    The converted temperature in the opposite unit.
  """

  if unit == "F":
    return (temp - 32) * 5/9
  elif unit == "C":
    return temp * 9/5 + 32
  else:
    raise ValueError("Invalid unit: {}".format(unit))

while True:
  try:
    temp_str = input("Enter the temperature you want to convert (e.g., 32F, 100C): ")
    temp = float(temp_str[:-1])  # Extract the numerical part of the temperature
    unit = temp_str[-1].upper()  # Extract the unit (last character)
    converted_temp = convert_temp(temp, unit)

    if unit == "F":
      print(f"{temp} degrees Fahrenheit is equal to {converted_temp:.1f} degrees Celsius")
    else:
      print(f"{temp} degrees Celsius is equal to {converted_temp:.1f} degrees Fahrenheit")

    repeat = input("Do you want to convert another temperature? (yes/no): ")
    if repeat.lower() != "yes":
      break
  except ValueError:
    print("Invalid input. Please enter a valid temperature with a unit (e.g., 32F, 100C).")