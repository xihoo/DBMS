#!/usr/bin/python

import pymysql
connection=pymysql.connect( host='localhost',port=3306,user='root',password='812666',db='item')
cur=connection.cursor()
cur.execute("select * from book;")
print "Content-type:text/html"
print 
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print "</head>"
print "<body>"
for r in cur:
    print '<table border="1">'
    print '<tr>'
    print '<td><p>shuming:%s</p></td>' %r[0]
    print '<td><p>writer:%s</p></td>' %r[1]
    print '<td><p>shuhao:%s</p></td>' %r[2]
    print '<td><p>chubanshe:%s</p></td>' %r[3]
    print '<td><p>sunhui:%d</p></td>' %r[4]
    print '<td><p>number:%d</p></td>' %r[5]
    print '<td><p>price:%f</p></td>' %r[6]
    print '<br/>'
print "</body>"
print "</html>"    
