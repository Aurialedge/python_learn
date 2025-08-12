# converting the celcius to fahrenheit
celcius=int(input("Enter the Celcius"))

def convert(celcius):
    f=celcius*(9/5) + 32
    return f
print(convert(celcius))