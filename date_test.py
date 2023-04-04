from datetime import datetime

# RFC 2822 format
# time zone can be expressed as +0800 or GMT
# parse +0800 as %z
# parse GMT as %Z

# date_string = "Thu, 17 Mar 2022 12:34:56 +0800"
# date_format = "%a, %d %b %Y %H:%M:%S %z"
date_string = "Sat, 01 Apr 2023 22:57:51 GMT"
date_format = "%a, %d %b %Y %H:%M:%S %Z"
datetime_object = datetime.strptime(date_string, date_format)
edited_date = datetime_object.strftime("%B %d, %Y")
print(datetime_object)
print(edited_date)
