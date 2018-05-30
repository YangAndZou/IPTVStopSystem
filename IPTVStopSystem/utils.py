# coding=utf-8
import socket
import paramiko


# paramiko ssh 连接封装
def ssh_paramiko(ip, username, passwd, cmd):
    result = {}
    try:
        ssh = paramiko.SSHClient()
        # 用于允许连接不在known_hosts名单中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=22, username=username, password=passwd, timeout=5)
        stdin, stdout, stderr = ssh.exec_command(cmd)
        # 与服务器交互，输出Y，这里的交互是指后面的cmd需要的执行的程序可能
        # 出现交互的情况下，可以通过该参数进行交互。
        # stdin.write("Y")
        print(stdout.read())
        print('%s OK\n' % ip)
        ssh.close()
    except Exception as e:
        print('%s Error,  %s\n' % (ip, e))
        return result


if __name__ == '__main__':
    # paramiko 使用
    # 方法一SSHClient
    ssh = paramiko.SSHClient()
    # 允许连接不在know_hosts文件中的主机
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('192.168.2.167', 22, 'root')

    # 方法二Transport
    t = paramiko.Transport(('192.168.2.168', '22'), )
    t.connect(username='root', password='123')
    # 连接远程主机需要提供密钥
    t.connect(username='root', password='123', hostkey='zz')
    # paramiko.transport对象也支持以socket的方式进行连接
    # 用socket连接
    tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpsock.settimeout(5)
    tcpsock.connect(('192.168.2.167', 22), )
    ssh = paramiko.Transport(tcpsock)
    ssh.connect(username='root', password='12')
    sftpConnect = paramiko.SFTPClient.from_transport(ssh)

    # 日志输出文件
    # paramiko.util.log_to_file('/tmp/sshout')

    ssh_paramiko("45.76.22.112", "root", "password", "ls")
