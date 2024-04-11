# Method 1
str=input("Enter a string with digit:")
count=0
for x in str:
  if x=="0" or x=="1" or x=="2" or x=="3" or x=="4" or x=="5" or x=="6" or x=="7" or x=="8" or x=="9":
    count=count+1
print(count)

# Method 2
# Prompt the user to enter a string
str_input = input("Enter a string with digits: ")

# Initialize a count variable to keep track of the number of digits
count = 0

# Iterate through each character in the input string
for x in str_input:
    # Check if the character is a digit (0-9)
    if x.isdigit():
        # Increment the count if the character is a digit
        count += 1

# Print the total count of digits in the string
print(count)
