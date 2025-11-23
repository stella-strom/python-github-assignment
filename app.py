# Welcome message
print("Welcome to my Python program!")
# Input from user
hours = input("How many hours did you work today?")
hours = float(hours)
# Calculate weekly hours
weekly_hours = hours * 5
# Display output clearly
print(f"You worked {weekly_hours} hours this week.")
# Convert to float with error handling
try:
    hours = float(hours)
except ValueError:
    print("Please enter a valid number.")
    exit()
