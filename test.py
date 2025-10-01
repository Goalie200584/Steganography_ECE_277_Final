
for i in range(0,10):
    try:
        result = 10 / i  # This line will cause an error
    except:
        print("Oops! An error occurred. This message is from the except block.")

# Output:
# Attempting to divide by zero...
# Oops! An error occurred. This message is from the except block.