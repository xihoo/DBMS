#!/usr/bin/python

import cgi,cgitb,pymysql
form=cgi.FieldStorage()
c_shuming=form.getvalue('shuming')
if c_shuming==None:
    c_shuming='unknown'
c_writer=form.getvalue('writer')
if c_writer==None:
    c_writer='unknown'
c_shuhao=form.getvalue('shuhao')
if c_shuhao==None:
    c_shuhao='unknown'
c_chubanshe=form.getvalue('chubanshe')
if c_chubanshe==None:
    c_chubanshe='unknown'
c_sunhui=form.getvalue('sunhui')
if c_sunhui==None:
    c_sunhui=100
c_price=form.getvalue('price')
if c_price==None:
    c_price=0
connection=pymysql.connect( host='localhost',port=3306,user='root',password='812666',db='item')
cur=connection.cursor()
cur.execute("insert into book values('%s','%s','%s','%s',%d,1,%f);" %(c_shuming,c_writer,c_shuhao,c_chubanshe,int(c_sunhui),float(c_price)))
print "Content-type:text/html"
print
print "<html>"
print "<head>"
print "<meta charset='utf-8'>"
print "<head/>"
print "<body>"
print "<p>cunshu complete<p/>"
print "<body/>"
print "<html/>"
