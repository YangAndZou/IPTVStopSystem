# coding=utf-8
import xlrd
import pymysql
from IPTVStopSystem import settings

if __name__ == '__main__':
    data = xlrd.open_workbook('iptvs.xlsx')
    sheet = data.sheet_by_name('IPTV+')

    conn = pymysql.connect(
        host=settings.DB_HSOT,
        user=settings.DB_USERNAME,
        passwd=settings.DB_PASSWD,
        db=settings.DB_NAME,
        port=3306,
        charset='utf8'
    )

    cur = conn.cursor()
    sql = 'insert into iptv.iptv_program (program_name, program_ip, platform, ' \
          'program_ip_type, program_type, status) values (%s, %s, %s, %s, %s, %s)'
    gq = []
    ws = []
    cctv = []
    sn = []
    qt = []
    for r in range(1, sheet.nrows):
        str = sheet.cell(r, 1).value.strip()
        if len(str) > 0:
            if str[-2:] == u'高清' or str[-4:] == u'（高清）' or str[-2:] == u'HD':
                gq.append(str)
                values = (sheet.cell(r, 1).value, sheet.cell(r, 5).value, '中兴', 'iptv+', '高清', 2)
                cur.execute(sql, values)
                conn.commit()
                continue
            elif str[:2] == u'湖南' or str[:2] == u'长沙' or str[:2] == u'芒果':
                sn.append(str)
                values = (sheet.cell(r, 1).value, sheet.cell(r, 5).value, '华为', 'iptv+', '省内', 2)
                cur.execute(sql, values)
                conn.commit()
                continue
            elif str[-2:] == u'卫视':
                ws.append(str)
                values = (sheet.cell(r, 1).value, sheet.cell(r, 5).value, '华为', 'iptv+', '卫视', 2)
                cur.execute(sql, values)
                conn.commit()
                continue
            elif str[:4] == u'CCTV':
                cctv.append(str)
                values = (sheet.cell(r, 1).value, sheet.cell(r, 5).value, '华为', 'iptv+', '央视', 2)
                cur.execute(sql, values)
                conn.commit()
                continue
            else:
                qt.append(str)
                values = (sheet.cell(r, 1).value, sheet.cell(r, 5).value, '华为', 'iptv+', '其他', 2)
                cur.execute(sql, values)
                conn.commit()

    cur.close()
    conn.close()
