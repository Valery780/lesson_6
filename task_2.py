import time

def count_down(func):
    def wrapper():
        for i in range(1, 4):
            print(i)
            time.sleep(1)
        func()
    return wrapper()
@count_down
def what_time_is_it_now():
    print(time.strftime('%H:%M'))
