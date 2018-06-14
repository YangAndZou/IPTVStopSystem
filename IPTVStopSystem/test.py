import paramiko
from threading import Thread
import subprocess
from Queue import Queue

num_threads = 3
queue = Queue()
ips = ["192.168.2.162", "192.168.2.163", "192.168.2.164", "192.168.2.165", "192.168.2.166", "192.168.2.167"]


def pinger(i, q):
    """Pings subnet"""
    while True:

        ip = '192.168.2.168'
        port = 22
        username = 'root'
        passwd = 'Trans@2017'

        ips = q.get()
        cd_cmd = 'cd /tmp/tmp_num;'
        nums = ['rm -rf {}'.format(str(i)) for i in range(0, 1000)]

        count = len(nums) / 10 if len(nums) % 10 == 0 else (len(nums) / 10) + 1
        for i in range(0, count):
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=ip, port=port, username=username, password=passwd)
            real_cmd = nums[i * 10: (i + 1) * 10]
            real_cmd = cd_cmd + ';'.join(real_cmd) + ';'
            print(real_cmd)
            stdin, stdout, stderr = ssh.exec_command(real_cmd, get_pty=True)
            ssh.close()
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
    ip = '192.168.2.168'
    port = 22
    username = 'root'
    passwd = 'Trans@2017'
    # transport = paramiko.Transport((ip, port))
    # transport.connect(username=username, password=passwd)
    # ssh = paramiko.SSHClient()
    # ssh._transport = transport

    cd_cmd = 'cd /tmp/tmp_num;'
    nums = ['rm -rf {}'.format(str(i)) for i in range(0, 1000)]
    # nums = ['touch {}'.format(str(i)) for i in range(0, 1000)]
    # nums = nums[0:100]
    # nums = ';'.join(nums) + ';'
    # print(nums)
    count = len(nums) / 20 if len(nums) % 20 == 0 else (len(nums) / 20) + 1
    for i in range(0, count):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=passwd)
        real_cmd = nums[i * 20: (i + 1) * 20]
        real_cmd = cd_cmd + ';'.join(real_cmd) + ';'
        print(real_cmd)
        stdin, stdout, stderr = ssh.exec_command(real_cmd, get_pty=True)
        ssh.close()
