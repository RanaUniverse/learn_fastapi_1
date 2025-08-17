# This will help me to write some of my own code for reuse purpose.

import datetime


def current_indian_time():
    gmt_now = datetime.datetime.now(tz=datetime.timezone.utc)
    ist_now = gmt_now + datetime.timedelta(hours=5, minutes=30)
    # print("✨ Behold! The current Indian Standard Time is:", ist_now.strftime('%Y-%m-%d %H:%M:%S'))
    return ist_now


# Summon the time, brave coder!
print(current_indian_time().strftime("%Y-%m-%d %H:%M:%S"))
