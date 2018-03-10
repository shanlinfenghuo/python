import MySQLdb
import wmi
import socket
import getpass

name = socket.gethostname()
acct = getpass.getuser()
mac = ''
c = wmi.WMI()
for i in c.Win32_NetworkAdapter():
    try:
        if i:
            if (i.PNPDeviceID[0:3] == 'PCI') and (i.NetConnectionStatus == 2):
                mac = i.MacAddress
    except TypeError , e:
        continue
    except AttributeError, e:
        continue

inf = c.Win32_ComputerSystemProduct()
sn = c.Win32_ComputerSystemProduct()[0].IdentifyingNumber
md = c.Win32_ComputerSystemProduct()[0].Version
print name, acct, mac, md, sn

value = [name, acct, mac, md, sn, '']
try:
    conn = MySQLdb.connect(host='localhost', user='******', passwd='*******', db='test', port=3306)
    cur = conn.cursor()
    cur.execute('insert into info values(%s, %s, %s, %s, %s, %s)', value)

    conn.commit()
    cur.close()
    conn.close()
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
else:
    print "Complete!"
    
    
    
