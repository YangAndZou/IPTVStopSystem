from IPTVStopSystem import utils

if __name__ == '__main__':
    cmd = 'cd /tmp/;touch ZLF'
    utils.ssh_paramiko('127.0.0.1', 22, 'zoulf', '8620303', cmd)
