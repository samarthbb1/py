# 4a. ATM Withdrawal with Exception Handling
balance = 5000

try:
    amt = int(input("Enter amount to withdraw: "))
    if amt > balance:
        raise ValueError("Insufficient Balance! ")
    if amt <= 0:
        raise ValueError("Invalid Amount! ")
    balance -= amt
    print(f"Withdrawal Successful! New Balance: {balance}")
except ValueError as e:
    print(f"Error: {e}")


#4b Open the input file and read all lines
with open("input.txt", "r") as file:
    lines = file.readlines()

# Sort the lines alphabetically
lines.sort()

# Write the sorted lines to the output file
with open("output.txt", "w") as file:
    file.writelines(lines)

print("Lines have been sorted alphabetically and written to output.txt")

