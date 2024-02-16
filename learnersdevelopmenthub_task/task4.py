#  Time-Based Greetings Script! 🌞🌜 
# Run the script to get personalized greetings - 
# ‘Good Morning’, ‘Good Afternoon’, ‘Good Evening’, or ‘Good Night’ based on the current time.

import datetime as t

time=t.datetime.now().hour
print("time :::: ",time)

if time<12:
    print('Good morning')
elif time<16:
    print('Good afternoon')
elif time<21:
    print('Good evening')
else:
    print('good night')