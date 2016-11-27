#!/usr/bin/python

import cgi,cgitb
form=cgi.FieldStorage()
_name1=form.getvalue('na')
_passwd1=form.getvalue('pa')
if _name1=='ypb' and _passwd1=='123456': 
    print "Content-type:text/html"
    print
    print '<a href="../cunshu.html">cunshu</a>'
    print '<a href="caigou.py">caigou</a>'
    print '<a href="taotai.py">taotai</a>'
    print '<a href="yilan.py">yilan</a>'
else:
    print "Content-type:text/html"
    print
    print '<html>'
    print '<body>'
    print "<h1>user:%s</h1>" % (_name1)
    print "<h2>password:%s</h2>" % (_passwd1)
    print '</body>'
    print '</html>'
