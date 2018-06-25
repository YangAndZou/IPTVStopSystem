# coding=utf-8
import xlrd
import pymysql
from IPTVStopSystem import settings

import sys

reload(sys)
sys.setdefaultencoding('utf8')


def to_cdn(excel_name):
    data = xlrd.open_workbook(excel_name)
    sheets = data.sheet_names()
    status = 2
    for s in sheets:
        sheet = data.sheet_by_name(s)
        is_range = False
        if s == u'华为IPTV+ CDN':
            is_range = True
        elif s == u'中兴IPTV+ CDN':
            is_range = True
        conn = pymysql.connect(
            host=settings.DB_HSOT,
            user=settings.DB_USERNAME,
            passwd=settings.DB_PASSWD,
            db=settings.DB_NAME,
            port=3306,
            charset='utf8'
        )
        cur = conn.cursor()
        sql = 'insert into iptv.iptv_cdn_node (city, ip, device_name, paltform, status) values (%s, %s, %s, %s, %s)'
        if is_range:
            for row in range(sheet.nrows):
                city = sheet.cell(row, 0).value
                ip = sheet.cell(row, 1).value
                device_name = sheet.cell(row, 2).value
                platform = s
                values = (city, ip, device_name, platform, status)
                cur.execute(sql, values)
                conn.commit()
        else:
            for row in range(1, sheet.nrows):
                city = s[:-4]
                ip = sheet.cell(row, 0).value
                device_name = sheet.cell(row, 1).value
                platform = s
                values = (city, ip, device_name, platform, status)
                cur.execute(sql, values)
                conn.commit()
        cur.close()
        conn.close()


if __name__ == '__main__':
    to_cdn('cdns.xlsx')
