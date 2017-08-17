import threading

a_int = 0
lock = threading.Lock()
threads = []


def increment(times):
    global a_int
    for _ in range(times):
        with lock:
            a_int += 1


for _ in range(15):
    times = 10
    t = threading.Thread(target=increment, args=(times,))
    threads.append(t)
    t.start()

for th in threads:
    th.join()

print(a_int)
