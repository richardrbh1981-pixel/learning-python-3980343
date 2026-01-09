#
# Example file for working with timedelta objects
# LinkedIn Learning Python course by Joe Marini
#


from datetime import date
from datetime import datetime
from datetime import timedelta

# construct a basic timedelta and print it
print(timedelta(days=365, hours=5, minutes=1)) 
today = datetime.now()

# print today's date
print("Today's date is:", today)

# print today's date one year from now
print("In one year it will be:", today + timedelta(days=365))

# create a timedelta that uses more than one argument
print("In two years and 3 weeks it will be: ", today + timedelta(days=2*365, weeks=3))

# calculate the date 1 week ago, formatted as a string
t = today - timedelta(weeks=1)
print("One week ago it was:", t.strftime("%Y/%m/%d"))

### How many days until April Fools' Day?
t = date.today()
Christmas = date(t.year, 12, 25)
if Christmas < t:
    print(f"Christmas Day has already gone by {(t - Christmas).days} days ago" )
    Christmas = Christmas.replace(year=t.year + 1)

time_to_christmas = Christmas - t
print(f"There are {time_to_christmas.days} days until Christmas!")
