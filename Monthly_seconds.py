from Num_to_Words_func import num_to_words_func

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
month = input("Please input a month: ")
Seconds_in_Month = secs_in_month(month)


print(f"You have {Seconds_in_Month}  seconds in {month} make each count.")
 
        
 


        
