from tkinter import W


weeks = ["Sunday", "Monday", "Tuesday", "Wednesday",
         "Thursday", "Friday", "Saturday"]

weekday = 0

if isinstance(weekday, int) and weekday == 0 or weekday == 6:
    print("Week-end : ", weeks[weekday])
elif isinstance(weekday, int) and weekday < 6 and weekday > 0:
    print("Week : ", weeks[weekday])
else:
    print("Not valid value")
