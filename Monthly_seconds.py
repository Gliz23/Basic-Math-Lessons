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

    return f"You have {ans} seconds in this month. Make each count :)"

Seconds_in_Jan = secs_in_month("January")


print(Seconds_in_Jan)

        
