FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius *CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

temperature = float(input("Enter the temperature to convert: "))
c_or_f = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

if c_or_f == "C":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature}°C is {fahrenheit}°F")
elif c_or_f == "F":
    celsius = convert_to_celsius(temperature)
    print(f"{temperature}°F is {fahrenheit}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")