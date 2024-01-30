# from pytz import timezone, all_timezones
# from datetime import datetime
#
# zone = timezone('Europe/Moscow')
#
# print('Europe/Mosc' in all_timezones)

import phonenumbers

n = str(phonenumbers.parse('+79850665451').national_number)[:3]

print(n)