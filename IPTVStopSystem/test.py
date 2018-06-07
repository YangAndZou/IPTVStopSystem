from threading import Thread
import subprocess
from Queue import Queue

num_threads = 3
queue = Queue()
ips = ["192.168.2.162", "192.168.2.163", "192.168.2.164", "192.168.2.165", "192.168.2.166", "192.168.2.167"]


def pinger(i, q):
    """Pings subnet"""
    while True:
        ip = q.get()
        print "Thread %s: Pinging %s" % (i, ip)
        ret = subprocess.call("ping -c 1 %s" % ip,
                              shell=True,
                              stdout=open('/dev/null', 'w'),
                              stderr=subprocess.STDOUT)
        if ret == 0:
            print "%s: is alive" % ip
        else:
            print "%s: did not respond" % ip
        q.task_done()


def main():
    for i in range(num_threads):
        worker = Thread(target=pinger, args=(i, queue))
        worker.setDaemon(True)  # to avoid zombies thread
        worker.start()

    for ip in ips:
        queue.put(ip)

    print "Main Thread Waiting"
    queue.join()
    print "Done"


if __name__ == '__main__':
    main()
