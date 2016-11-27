#!/usr/bin/python

import pymysql
connection=pymysql.connect( host='localhost',port=3306,user='root',password='812666',db='item')
cur=connection.cursor()
cur.execute("select shuming from book where sunhui>=4;")
print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print "</head>"
print "<body>"
print "<h1>these books are deleted:</h1>"
for r in cur:
    print "<p>'%s'</p><br/>" %(r)
print "</body>"
print "</html>"
cur.execute("delete from book where sunhui>=4;")
