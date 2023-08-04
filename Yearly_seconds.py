

def secs_in_month(month):
    if month == "January":
        ans = 31*24*60*60
    elif month == "February":
        ans = 28*24*60*60
    elif month == "March":
        ans = 31*24*60*60
    elif month == "April":
        ans = 30*24*60*60
    elif month == "May":
        ans = 31*24*60*60
    elif month == "June":
        ans = 30*24*60*60
    elif month == "July":
        ans = 31*24*60*60
    elif month == "August":
        ans = 31*24*60*60
    elif month == "September":
        ans = 30*24*60*60
    elif month == "October":
        ans = 31*24*60*60
    elif month == "November":
        ans = 30*24*60*60
    elif month == "December":
        ans = 31*24*60*60

    return ans

Seconds_in_Jan = secs_in_month("January")
Seconds_in_Feb = secs_in_month("February")
Seconds_in_Mar = secs_in_month("March")
Seconds_in_April = secs_in_month("April")
Seconds_in_May = secs_in_month("May")
Seconds_in_June = secs_in_month("June")
Seconds_in_July = secs_in_month("July")
Seconds_in_Aug = secs_in_month("August")
Seconds_in_Sept = secs_in_month("September")
Seconds_in_Oct = secs_in_month("October")
Seconds_in_Nov = secs_in_month("November")
Seconds_in_Dec = secs_in_month("December")

Seconds_in_year= Seconds_in_Jan + Seconds_in_Feb + Seconds_in_Mar  + Seconds_in_April + Seconds_in_May  + Seconds_in_June  + Seconds_in_July  + Seconds_in_Aug + Seconds_in_Sept +  Seconds_in_Oct  + Seconds_in_Nov  + Seconds_in_Dec  
print(f"You have {Seconds_in_year} seconds in this year. Make them count. Trust in God")



        
