
# exam : output day/ time
import datetime
 
# datetime.py
# @classmethod
# def now(cls, tz=None):
#     "Construct a datetime from time.time() and optional time zone info."
#     t = _time.time()
#     return cls.fromtimestamp(t, tz)

# print and get today/time
now = datetime.datetime.now()  

print(f"year: {now.year}")
print(f"month: {now.month}")
print(f"day: {now.day}")

print("-"*60)
print("{}년 {}월 {}일".format(now.year, now.month, now.day))
print("{} {} hour {} min {} sec".format("AM" if now.hour < 12 else "PM", now.hour, datetime.datetime.now().minute, datetime.datetime.now().second))

if now.hour < 12:
    print("AM")
else :
    print("PM")
print("-"*60)

# 봄 Spring : 3,4,5
# 여름 Summer: 6,7,8
# 가을 Autumn (Fall): 9,10,11
# 겨울 Winter: 12,1,2
 
mon = now.month
result = "Season :"
if 3 <= mon < 6 :
    print(result, "Spring")
elif 6 <= mon < 9:
    print(result, "Summer")
elif 9 <= mon < 12:
    print(result, "Autumn (Fall)")
elif 1 <= mon < 3 or mon == 12:
    print(result, "Winter")


