# m. Use the datetime module to: 
# a. Display the current date and time. 
# b. Compute the difference between two dates.

from datetime import datetime

# Current date and time
now = datetime.now()

print("Current Date and Time:", now)

# Difference between dates
d1 = datetime(2025, 1, 1)
d2 = datetime(2025, 5, 1)

print("Difference:", d2 - d1)