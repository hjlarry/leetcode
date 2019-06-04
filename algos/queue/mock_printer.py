import random
from adt import ArrayQueue


# 当前打印机是否可以处理任务负载，如果它设置为打印更好的质量，较慢的页面速率。我们采用的方法是编写一个模拟打印任务作为各种页数和到达时间的随机事件的模拟。


class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm  # 打印机每分钟处理多少页，即处理速率
        self.current_task = None
        self.time_remaining = 0  # 处理当前任务剩余多少秒

    def tick(self):
        if self.current_task != None:
            self.time_remaining = self.time_remaining - 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def start_next(self, newtask):
        self.current_task = newtask
        self.time_remaining = newtask.get_pages() * 60 / self.pagerate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1, 21)

    def get_stamp(self):
        return self.timestamp

    def get_pages(self):
        return self.pages

    def wait_time(self, current_time):
        return current_time - self.timestamp


def simulation(num_seconds, pages_perminute):

    labprinter = Printer(pages_perminute)
    print_queue = ArrayQueue(32)
    waitingtimes = []

    for current_second in range(num_seconds):

        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not labprinter.busy()) and len(print_queue) != 0:
            nexttask = print_queue.dequeue()
            waitingtimes.append(nexttask.wait_time(current_second))
            labprinter.start_next(nexttask)

        labprinter.tick()

    average_wait = sum(waitingtimes) / len(waitingtimes)
    print(f"Average Wait {average_wait:.2f} secs {print_queue.size()} tasks remaining.")


def new_print_task():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


print("模拟每分钟5页的速率运行一小时：")
for i in range(10):
    simulation(3600, 5)
print()
print("模拟每分钟10页的速率运行一小时：")
for i in range(10):
    simulation(3600, 10)
