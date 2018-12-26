#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import subprocess
import cgi, cgitb
from database import actualiza_estado

form = cgi.FieldStorage()
status = form.getvalue('onoffswitch')
if status == "on":
    try:
        actualiza_estado("ducha",True)
        subprocess.Popen(['/usr/bin/python','/usr/lib/cgi-bin/tplink_smartplug.py','-t','192.168.100.58','-c','on'])
    except:
        print("except")
else:
    try:
        actualiza_estado("ducha",False)
        subprocess.call(['/usr/bin/python', '/usr/lib/cgi-bin/tplink_smartplug.py','-t','192.168.100.58','-c','off'])
    except:
        print("except")

print("Content-type: text/html\n\n")
print("<html>")
print("<head>")
print("<meta http-equiv=\"refresh\" content=\"0; url=http://192.168.100.49/cgi-bin/test.py\"/>")
print("<link rel=\"stylesheet\" href=\"style.css\">")
print("<title>")
print("Response Form")
print("</title>")
print("</head>")
print("<body>")
print("</body>")
print("</html>")
