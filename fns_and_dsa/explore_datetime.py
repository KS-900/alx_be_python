import datetime
from datetime import timedelta
from datetime import datetime
def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(current_date)
display_current_datetime()
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    future_date = datetime.now() + timedelta(days=number_of_days)
    future_date = future_date.strftime(("%Y-%m-%d"))
    print(f"Future date: {future_date}")
calculate_future_date()