# coding=utf-8
import xlrd
import pymysql
from IPTVStopSystem import settings

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def new_to_mysql(excel_name):
    data = xlrd.open_workbook(excel_name)
    sheets = data.sheet_names()
    status = 2
    type_index = 0
    program_ip_type = ''
    program_types = []
    for s in sheets:
        sheet = data.sheet_by_name(s)
        if s == 'IPTV+':
            program_ip_type = 'IPTV+'
            program_types = ['高清', '4K', '省内', '央视', '卫视', '付费', '其他']
        elif s == 'IPTVB':
            program_ip_type = 'IPTV标清'
            program_types = ['央视', '省内', '卫视', '其他', '付费']
        elif s == 'IPTVG':
            program_ip_type = 'IPTV高清'
            program_types = ['高清', '央视', '省内', '卫视', '其他', '付费']
        conn = pymysql.connect(
            host=settings.DB_HSOT,
            user=settings.DB_USERNAME,
            passwd=settings.DB_PASSWD,
            db=settings.DB_NAME,
            port=3306,
            charset='utf8'
        )
        cur = conn.cursor()
        sql = 'insert into iptv.iptv_program (program_num, program_name, program_ip_type, program_type, status) values (%s, %s, %s, %s, %s)'
        for c in range(0, sheet.ncols, 2):
            for r in range(0, sheet.nrows):
                program_num = sheet.cell(r, c).value
                program_name = sheet.cell(r, c + 1).value
                if program_name != '' and program_num != '':
                    values = (program_num, program_name, program_ip_type, program_types[type_index], status)
                    cur.execute(sql, values)
                    conn.commit()
            type_index += 1
        cur.close()
        conn.close()
        type_index = 0


def new_update_mysql(excel_name):
    data = xlrd.open_workbook(excel_name)
    sheets = data.sheet_names()
    conn = pymysql.connect(
        host=settings.DB_HSOT,
        user=settings.DB_USERNAME,
        passwd=settings.DB_PASSWD,
        db=settings.DB_NAME,
        port=3306,
        charset='utf8'
    )
    cur = conn.cursor()
    sql_select = 'SELECT program_name FROM iptv_program'
    cur.execute(sql_select)
    program_names = cur.fetchall()
    names = []
    for i in range(len(program_names)):
        names.append(program_names[i][0])
    sheet = data.sheet_by_name('IPTV+')
    for row in range(sheet.nrows):
        program_name = sheet.cell(row, 0).value
        program_ip = sheet.cell(row, 1).value
        platform = '中兴'.encode()
        if program_name != '' and program_name != ' ':
            sql_update = "UPDATE iptv_program SET platform = {} ,program_ip = {} WHERE program_name = {}".format(
                platform, program_ip, program_name)
            cur.execute(sql_update)
            conn.commit()
    cur.close()
    conn.close()


if __name__ == '__main__':
    new_update_mysql('iptvs.xlsx')
