#!/usr/bin/python

import cgi,cgitb
form=cgi.FieldStorage()
_name1=form.getvalue('na')
_passwd1=form.getvalue('pa')
if _name1=='huyonghong' and _passwd1=='123456':
    print "Content-type:text/html"
    print
    print '<a href="../chaxun.html">chaxun</a>'
    print '<a href="../cunshu.html">huanshu</a>'
    print '<a href="../jieshu.html">jieshu</a>'
    print '<a href="../caigou.html">caigou jianyi</a>'
else:
    print "Content-type:text/html"
    print
    print '<html>'
    print '<body>'
    print "<h1>user:%s</h1>" % (_name1)
    print "<h2>password:%s</h2>" % (_passwd1)
    print '</body>'
    print '</html>'