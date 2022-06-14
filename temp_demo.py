import pandas as pd


def get_temperature():
    return pd.read_csv(r'temperature.txt', sep=" ")


print(get_temperature())


# def temp_file():
#     with open('temperature.txt') as f:
#         return f.readlines()[0]


def should_go_outside(temp, limit):
    if temp > limit:
        return False
    else:
        return True


def get_limit():
    return input.int(('How hot is too hot?'))


limit = get_limit()
temp = get_temperature()

go_outside = should_go_outside(temp, limit)

print(go_outside)
