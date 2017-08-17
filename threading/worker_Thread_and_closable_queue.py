from queue import Queue

from threading import Thread


# Pipeline jobs.
class ClossableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                else:
                    yield item
            finally:
                self.task_done()


class WorkerThread(Thread):
    def __init__(self, input_queue, output_queue, func):
        super(WorkerThread, self).__init__()
        self.input_queue = input_queue
        self.output_queue = output_queue
        self.func = func

    def run(self):
        for item in self.input_queue:
            result = self.func()
            self.output_queue.put(result)


download_queue = ClossableQueue()
resize_queue = ClossableQueue()
upload_queue = ClossableQueue()
done_queue = ClossableQueue()


def download():
    print("download")
    return object()


def resize():
    print("resize")
    return object()


def upload():
    print("upload")
    return object()


wt1 = WorkerThread(download_queue, resize_queue, download)
wt2 = WorkerThread(resize_queue, upload_queue, resize)
wt3 = WorkerThread(upload_queue, done_queue, upload)
threads = [wt1, wt2, wt3]
for th in threads:
    th.start()
for _ in range(10):
    download_queue.put(object())
download_queue.close()
download_queue.join()
resize_queue.close()
resize_queue.join()
upload_queue.close()
upload_queue.join()
print(done_queue.qsize())
