# !/usr/bin/env python
# -*- coding:utf-8 -*-

import Queue
import paramiko
import threading
import time


class WorkManager(object):
    def __init__(self, ip, port, username, passwd, thread_num=4):
        self.work_queue = Queue.Queue()
        self.ssh = paramiko.SSHClient()
        self.threads = []
        self.__init_paramiko(ip, port, username, passwd)
        # self.__init_work_queue(work_num)
        self.__init_thread_pool(thread_num)

    # 初始化 paramiko
    def __init_paramiko(self, ip, port, username, passwd):
        # 用于允许连接不在known_hosts名单中的主机
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname=ip, port=port, username=username, password=passwd, timeout=5)

    # 初始化线程
    def __init_thread_pool(self, thread_num):
        for i in range(thread_num):
            self.threads.append(Work(self.work_queue))

    # # 初始化工作队列
    # def __init_work_queue(self, jobs_num):
    #     for i in jobs_num:
    #         self.add_job(ssh_paramiko(self.ssh, self.cmd))

    # 添加一项工作入队

    def add_job(self, func, *args):
        # 任务入队，Queue内部实现了同步机制
        self.work_queue.put((func, list(args)))

        # 等待所有线程运行完毕

    def wait_allcomplete(self):
        for item in self.threads:
            if item.isAlive():
                item.join()
        self.ssh.close()


class Work(threading.Thread):
    def __init__(self, work_queue):
        threading.Thread.__init__(self)
        self.work_queue = work_queue
        self.start()

    def run(self):
        # 死循环，从而让创建的线程在一定条件下关闭退出
        while True:
            try:
                # 任务异步出队，Queue内部实现了同步机制
                do, args = self.work_queue.get(block=False)
                do(args)
                # 通知系统任务完成
                self.work_queue.task_done()
            except Exception as e:
                print(e)
                break


# paramiko ssh 连接封装
def ssh_paramiko(ssh, cmd):
    try:
        # 当执行多条命令时，需要让get_pty=True，执行多条命令的格式为"cd /home;ls;cat z"
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
    except Exception as e:
        print('%s Error,\n' % e)


if __name__ == '__main__':
    start = time.time()
    work_manager = WorkManager('192.168.2.168', 22, 'root', 'Trans@2017', [x for x in range(1000)], 10)
    work_manager.wait_allcomplete()
    end = time.time()
    print "cost all time: %s" % (end - start)
