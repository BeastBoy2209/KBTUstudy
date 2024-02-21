#required libraries
import datetime

#1
nowtime = datetime.date.today()
fivedays =datetime.timedelta(5)
substracted5 = nowtime - fivedays
print(substracted5)
#2
oneday = datetime.timedelta(1)
print("yesterday: ", nowtime - oneday)
print("today: ", nowtime)
print("tomorrow: ", nowtime + oneday)

#3
dt_with_microseconds = datetime.datetime.now()
dt_without_microseconds = dt_with_microseconds.replace(microsecond=0)

print("Datetime with seconds: ", dt_with_microseconds)
print("Datetime without seconds: ", dt_without_microseconds)
#4
def two_days_dif_sec():
    print("format: date1 - date 2 ")
    print("data format: yyyy.mm.dd ")
    variable1 = input("Input 1st data: ")
    date1 = datetime.datetime.strptime(variable1, "%Y.%m.%d" )
    variable2 = input("Input 2st data: ")
    date2 = datetime.datetime.strptime(variable2, "%Y.%m.%d" )
    result = date1 - date2
    print(round(result.total_seconds()))
two_days_dif_sec()

