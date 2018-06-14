# coding=utf-8
import paramiko


# 测试用例, 在连接服务器的 /tmp/ 目录下创建一个以传入的参数命名的空文件
def test_create_code(*args):
    return 'cd /tmp/;touch {}'.format(args[0])


# 测试用例, 在连接服务器的 /tmp/ 目录下删除一个以传入的参数命名的空文件
def test_rm_code(*args):
    return 'cd /tmp/;rm -rf {}'.format(args[0])


# EPG一键关停 , 是连续的操作
def epg_shutdown_cmd_continuous():
    return 'interface GigabitEthernet3/0/2;shutdown;interface GigabitEthernet6/0/2;shutdown;interface gei_2/25;shutdown'


# EPG一键关停, 根据传入的参数返回对应的值
def epg_shutdown_cmd_split(*args):
    if args[0] == 'NE40E 124.232.139.1':
        return 'interface GigabitEthernet3/0/2;shutdown'
    elif args[0] == 'NE40E 124.232.139.2':
        return 'interface GigabitEthernet6/0/2;shutdown'
    elif args[0] == '124.232.230.1' or args[0] == '124.232.230.2':
        return 'interface gei_2/25;shutdown'


def program_shutdown_cmd_both(*args):
    return 'acl number 3991;rule 200 deny ip source 10.255.0.0 0.0.255.255 destination {} 0.0.0.0;' \
           'rule 205 deny ip source 10.255.0.0 0.0.255.255 destination {} 0.0.0.0'.format(args[0], args[1])


# 根据传入的check( ip 地址) 返回对应指令
def program_shutdown_cmd_split(check, *args):
    if check == '124.232.139.4':
        return 'acl number 3991;rule 200 deny ip source 10.255.0.0 0.0.255.255 destination {} 0.0.0.0'.format(args[0])
    elif check == '124.232.139.63':
        return 'acl number 3991;rule 205 deny ip source 10.255.0.0 0.0.255.255 destination {} 0.0.0.0'.format(args[0])


# 广告关停,需传入 ip
def advert_shutdown_cmd(*args):
    return 'Ip route-static {} 32 null0'.format(args[0])


def huawei_cdn_shutdown_cmd():
    return 'acl number 3991;undo rule 605'


def ZTE_cdn_shutdown_cmd():
    return 'ipv4-access-list 199;no rule 605'


def ZTE_cdn_pop_shutdown_cmd(number):
    return 'acl extended number {};no rule 605'.format(number)


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
