# We use the exceptional handling to find the exception or doing the exception handling in the code
try:
    a=345
    v="intw"
    z=a+v
except Exception as e:
    print(e)


try:
    # risky code
    x = int(input("Enter numerator: "))
    y = int(input("Enter denominator: "))
    result = x / y
    print("Result:", result)

except ZeroDivisionError:
    print("Zero error: You cannot divide by zero!")

except TypeError:
    print("Type error: Invalid type used in operation!")

except Exception as e:   # catches all other exceptions
    print("An unexpected error occurred:", e)

else:
    print("Division successful ✅")

finally:
    print("Execution complete ✅")
