"""Create a loop that prints even numbers until
 it reaches your year of age or, 
if your age is an odd number, 
prints out odd numbers until it reaches your age.
Create a list containing five different sandwich ingredients.
 Then, create a loop that prints out the list (including the numbers)
If you were standing on the moon right now, your weight would be 16.5 percent of what it is on Earth. You can calculate that by multiplying your Earth weight by 0.165.  If you gained a kilo in weight every year for the next 15 years,
 what would your weight be when you visited the moon each year and at the end of the 15 years?
 Write a program using a for loop that prints your moon weight for each year.
"""

age=int(input("How old are you?: "))
if age == age in range(0,100,2):
    for age in range(0,age,+2):
        print(age, end=" ") 
elif age == age in range(1,99,2):
    for age in range(1,age,+2):
        print(age, end=" ") 

x = 1
results = ["ham","cheese","tomatos","lettuce","mayo"]
for i in results:
    print(f"{x} {i}")
    x = x + 1

weight=130
for year in range(1,16):
    weight = weight+1
    moon_weight= weight*0.165
    print(f"Year {year} is {moon_weight}")
#resubmit