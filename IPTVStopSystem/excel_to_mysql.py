# coding=utf-8
import xlrd
import pymysql
import os

data = xlrd.open_workbook('iptvs.xlsx')
sheet = data.sheet_by_name('IPTV+')
print(data)
print(os.path.split('iptv.xlsx'))

conn = pymysql.connect(
    host='192.168.2.168',
    user='root',
    passwd='Mysql123',
    db='iptv',
    port=3306,
    charset='utf8'
)

cur = conn.cursor()
sql = 'insert into iptv.iptv_program (program_name, program_ip, platform, ' \
      'program_ip_type, program_type, status) values (%s, %s, %s, %s, %s, %s)'

for r in range(1, sheet.nrows):
    values = (sheet.cell(r, 1).value, sheet.cell(r, 2).value, '华为', 'iptv+', '省内', 2)
    cur.execute(sql, values)
    conn.commit()

cur.close()
conn.close()