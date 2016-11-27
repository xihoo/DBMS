#!/usr/bin/python

import cgi,cgitb,pymysql
form=cgi.FieldStorage()
c_shuming=form.getvalue('shuming')
#c_shuming='hhhh'
connection=pymysql.connect( host='localhost',port=3306,user='root',password='812666',db='item')
cur=connection.cursor()
cur.execute("select no from book where shuming='%s';" %(c_shuming))
for r in cur:
   # print r
    if r[0]<=0:
        print "Content-type:text/html"
        print
        print "<html>"
        print "<head>"
        print "<meta charset='utf-8'>"
        print "</head>"
        print "<body>"
        print "<p>number is 0</p>"
        print "</body>"
        print "</html>"
        break
    else:    
        cur.execute("update book set no=no-1 where shuming='%s';" %(c_shuming))
        print "Content-type:text/html"
        print 
        print "<html>"
        print "<body>"
        print "<p>jieshu success</p>"
        print "</body>"
        print "</html>"
        break
