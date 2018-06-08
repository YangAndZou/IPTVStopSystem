# coding=utf-8
import socket
import string
from threading import Thread

import paramiko
from Queue import Queue


def test_create_code(*args):
    return 'cd /tmp/;ls;touch {};touch {}'.format(args[0], args[1])


def test_rm_code(*args):
    return 'cd /tmp/;ls;rm -rf {};rm -rf {}'.format(args[0], args[1])


def epg_shutdown_cmd(*args):
    return 'interface GigabitEthernet3/0/2;shutdown;interface GigabitEthernet6/0/2;shutdown;interface gei_2/25;shutdown'


def program_shutdown_cmd(*args):
    return 'acl number 3991;rule 200 deny ip source 10.255.0.0 0.0.255.255 destination {} 0.0.0.0;' \
           'rule 205 deny ip source 10.255.0.0 0.0.255.255 destination {} 0.0.0.0'.format(args[0], args[1])


def huawei_cdn_shutdown_cmd():
    return 'acl number 3991;undo rule 605'


def ZTE_cdn_shutdown_cmd():
    return 'ipv4-access-list 199;no rule 605'


def ZTE_cdn_pop_shutdown_cmd(number):
    return 'acl extended number {};no rule 605'.format(number)


# # paramiko ssh 连接封装
# def ssh_paramiko(ip, port, username, passwd, cmd, sudo=False):
#     result = {}
#     try:
#         ssh = paramiko.SSHClient()
#         # 用于允许连接不在known_hosts名单中的主机
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(hostname=ip, port=port, username=username, password=passwd, timeout=5)
#         # 当执行多条命令时，需要让get_pty=True，执行多条命令的格式为"cd /home;ls;cat z"
#         stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
#         if sudo:
#             stdin.write(passwd + '\n')
#         print('%s OK\n' % ip)
#         ssh.close()
#     except Exception as e:
#         print('%s Error,  %s\n' % (ip, e))
#         return result


if __name__ == '__main__':
    # # paramiko 使用
    # # 方法一SSHClient
    # ssh = paramiko.SSHClient()
    # # 允许连接不在know_hosts文件中的主机
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect('192.168.2.167', 22, 'root')
    #
    # # 方法二Transport
    # t = paramiko.Transport(('192.168.2.168', '22'), )
    # t.connect(username='root', password='123')
    # # 连接远程主机需要提供密钥
    # t.connect(username='root', password='123', hostkey='zz')
    # # paramiko.transport对象也支持以socket的方式进行连接
    # # 用socket连接
    # tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcpsock.settimeout(5)
    # tcpsock.connect(('192.168.2.167', 22), )
    # ssh = paramiko.Transport(tcpsock)
    # ssh.connect(username='root', password='12')
    # sftpConnect = paramiko.SFTPClient.from_transport(ssh)
    #
    # # 日志输出文件
    # # paramiko.util.log_to_file('/tmp/sshout')
    #
    # ssh_paramiko("45.76.22.112", "root", "password", "ls")

    print(
        'acl number 3991;rule 200 deny ip source 10.255.0.0 0.0.255.255 destination {} 0.0.0.0;rule 205 deny ip source 10.255.0.0 0.0.255.255 destination {} 0.0.0.0')
    print('acl number 3991;rule 200 deny ip '
          'source 10.255.0.0 0.0.255.255 destination {} '
          '0.0.0.0;rule 205 deny ip source 10.255.0.0 0.0.255.255 '
          'destination {} 0.0.0.0')
