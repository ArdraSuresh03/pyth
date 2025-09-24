import datetime
name=input("enter your name:")
age=int(input("enter your age:"))
current_year=datetime.datetime.now().year
year_100=current_year + (100 - age)
print(f"Hi {name},you turn 100 in {year_100}.")