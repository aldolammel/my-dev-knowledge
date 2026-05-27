from datetime import datetime, timedelta


# Calculate the date 85 years ago from today:

ago = (datetime.now() - timedelta(days=365.25 * 85)).date()
print(ago)


# Calculate the date 85 years to future from today:

future = (datetime.now() + timedelta(days=365.25 * 85)).date()
print(future)


