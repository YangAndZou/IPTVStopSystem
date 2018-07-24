# coding=utf-8
import paramiko


# paramiko ssh 连接封装
def ssh_paramiko(ip, port, username, passwd, cmd, sudo=False):
    result = {}
    try:
        ssh = paramiko.SSHClient()
        # 用于允许连接不在known_hosts名单中的主机
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=ip, port=port, username=username, password=passwd, timeout=5)
        # 当执行多条命令时，需要让get_pty=True，执行多条命令的格式为"cd /home;ls;cat z"
        stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True)
        if sudo:
            stdin.write(passwd + '\n')
        print('%s OK\n' % ip)
        ssh.close()
    except Exception as e:
        print('%s Error,  %s\n' % (ip, e))
        return result


# TODO 开启接口
def turn_on(position_head, position_x, position_y):
    pass


# TODO 关停接口
def turn_off(position_head, position_x, position_y):
    pass

