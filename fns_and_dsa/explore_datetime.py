import datetime
from datetime import timedelta
from datetime import datetime
def display_current_datetime():
    current_date = datetime.datetime(2025,1,16,22,23)
number_of_days = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    future_date = datetime.now() + timedelta(days=number_of_days)
    print(f"Future date: {future_date}")
calculate_future_date()