import datetime
class age_calculator:
    def __init__(self , year ):
        self.year = year 
    def greet(self):

        current_year = datetime.date.today().year
        ageIs =  current_year - self.year 
        if self.year <= current_year :
             ageInHour= ageIs * 365 *24 
             ageInMins = ageIs * 365 *24*60
             ageInsec =ageIs * 365 *24*60*60
             print(f"\n--- Age Details ---")
             print(f"Birth Year: {self.year}") 
             print(f"Current Year: {current_year}")
             print(f"Your age is approximately: {ageIs} years old.")
             print(f"You have lived approximately: {ageInHour:,} hours.")
             print(f"You have lived approximately: {ageInMins:,} minutes.")
             print(f"You have lived approximately: {ageInsec:,} seconds.")
        else:
           print("you come  to early in this planet")

year_you_born = int(input("enter your brith year:"))
person1 = age_calculator( year_you_born)
print(person1.greet())         
