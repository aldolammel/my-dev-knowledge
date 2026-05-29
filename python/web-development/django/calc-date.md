




    from django.utils import timezone
    from datetime import timedelta

    

    
    # Calculate the date 85 years ago from today:
    
    date_85_years_ago = (timezone.now() - timedelta(days=365.25 * 85)).date()    
    Output: 1939-10-30




    # Calculate the date 85 years to future from today:

    date_85_years_ago = (timezone.now() + timedelta(days=365.25 * 85)).date()    
    Output: 2109-10-30
