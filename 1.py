import help_func
import datetime as dt


a = int(input())

# LBYL - посмотри прежде чем прыгнуть

if a > 0:
    print(help_func.set_robot_power(a))
else:
    print('не нужно вводить значение меньше либо равно нуля')


# 2 EAFP

try:
    print(help_func.set_robot_power(a))
except help_func.NegativeValueException as error:
    print(
        error,
        (
            dt.datetime.utcnow() + dt.timedelta(hours=3)
        ).strftime('%Y-%m-%d %H:%M')
    )
except Exception as error:
    print('!'*10)
    print(
        error,
        (
            dt.datetime.utcnow() + dt.timedelta(hours=3)
        ).strftime('%Y-%m-%d %H:%M')
    )
    print('!'*10)
else:
    print('hello')