#!/usr/bin/python

import cgi,cgitb,pymysql
form=cgi.FieldStorage()
_name1=form.getvalue('shuming')
#_name1='hhhh'

connection=pymysql.connect( host='localhost',port=3306,user='root',password='812666',db='item')
cur=connection.cursor()
cur.execute("select * from book where shuming = '%s';" %(_name1))
print "Content-type:text/html"
print
print '<html>'
print '<body>'
for r in cur:
    print '<p>shuming:%s</p>' %r[0]
    print '<p>writer:%s</p>' %r[1]
    print '<p>shuhao:%s</p>' %r[2]
    print '<p>chubanshe:%s</p>' %r[3]
    print '<p>sunhui:%d</p>' %r[4]
    print '<p>number:%d</p>' %r[5]
    print '<p>price:%f</p>' %r[6]
print
print '</body>'
print '</html>'