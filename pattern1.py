# Print the table header
print("  i  |  i  |  i^2  |  i^3  |  i^4")
print("-----+-----+-------+-------+-------")

# Loop through the values of i from 1 to 5
for i in range(1, 6):
    # Calculate the powers of i
    i_squared = i ** 2
    i_cubed = i ** 3
    i_to_fourth = i ** 4

    # Print the current row of the table
    print(f"  {i}  |  {i}  |  {i_squared}  |  {i_cubed}  |  {i_to_fourth}  ")