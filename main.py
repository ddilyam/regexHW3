#Solve using Datetime & Date
# Write function that returns today's date in a format (day.month.year) (30)
# from datetime import date
# from datetime import datetime
# def get_today() -> str:
#     dt = date.today()
#     result = dt.strftime("%d.%m.%Y")
#     # result = date.today()
#     print("todays date: ", result)
#
# result = get_today()
# print(result)


#Date Format (40)
# from datetime import date
# from datetime import datetime
# def format_date(old_format) -> str:
#     new_format = ''.join(old_format.split('/')[::-1])
#     return new_format
#
# result = format_date("11/12/2019")
# print(result) # Example output: '20191211'

#Write a function that returns the future date in a format (year/month/day) after the entered number of the days (40)
# from datetime import date
# from datetime import datetime, timedelta
# def get_future_date(day_number) -> str:
#     res = datetime.today() + timedelta(day_number)
#     result = res.strftime('%d:%m:%Y')
#     return result
#
# result = get_future_date(3)
# print(result) # Example output: '2022/12/03'

# Solve using Datetime & Date and File IO
# Write function that receives date ranges in "DD.MM.YYYY" format and writes all dates between this dates to file.txt (100)
# def get_dates_in_range(date_from, date_to):
#
# date_from = "01.01.2022"
# date_to = "03.05.2022"
# get_dates_in_range(date_from, date_to)
