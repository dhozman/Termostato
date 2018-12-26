#!/usr/bin/python3
# -*- coding: UTF-8 -*-# enable debugging
import cgitb
import datetime
cgitb.enable()
from database import lee_estado,lee_programa

print("Content-Type: text/html;charset=utf-8\n")
print
print("<html>")
print("<head>")
print("<link rel=\"stylesheet\" href=\"/style.css?v=6\">")
print("<script>")
print("    function clock() {")
print("        var dt = new Date();")
print("        var hrs = dt.getHours();")
print("        var min = dt.getMinutes();")
print("        min = Ticking(min);")
print("        document.getElementById(\'dc\').innerHTML = hrs + \":\" + min;")
print("        if (hrs > 12) {")
print("            document.getElementById(\'dc_hour\').innerHTML = \'PM\';")
print("        }")
print("        else {")
print("            document.getElementById(\'dc_hour\').innerHTML = \'AM\';")
print("        }")
print("    }")
print("    function Ticking(ticVal) {")
print("        if (ticVal < 10) {")
print("            ticVal = \"0\" + ticVal;")
print("        }")
print("        return ticVal;")
print("    }")
print("</script>")
print("</head>")
print("<body onload=\"clock();\">")
print("<br>")
print("<br>")
print("<br>")
print("<br>")
print("<br>")
print("<div style=\"background-color:#F3F3F3;")
print("        max-width:220px;width:100%;margin:0 auto;padding:20px;\">")
print("        <table class=\"tabBlock\" align=\"center\" cellspacing=\"0\" cellpadding=\"0\" border=\"0\">")
print("            <tr><td class=\"clock\" id=\"dc\"></td>")
print("                <td>")
print("                    <table cellpadding=\"0\" cellspacing=\"0\" border=\"0\">")
print("                        <tr><td class=\"clocklg\" id=\"dc_hour\"></td></tr>")
print("                    </table>")
print("                </td>")
print("            </tr>")
print("        </table>")
print("</div>")
print("</td>")
print("</tr>")
print("</table>")
print("<br>")

fecha = datetime.datetime(2016,1,3,8,30,20)

fecha = fecha.now()
vector_fecha= fecha.timetuple()

fecha = fecha.strftime("%A, %d. %B %Y %I:%M%p")

#for dato in vector_fecha:
#    print(str(dato))

estado = lee_estado("ducha")
if estado == True:
    switch = "checked"
else:
    switch = "unchecked"

estado2 = lee_estado("encendido")
if estado2 == True:
    switch2 = "checked"
else:
    switch2 = "unchecked"

Monday=""
Tuesday=""
Wednesday=""
Thursday=""
Friday=""
Saturday=""
Sunday=""

programa = lee_programa("*","*")
for row in programa:
    if(row[1]=="MON"):
        Monday+=str(row[2])
        Monday= Monday[:-3] + " / "

    elif(row[1]=="TUE"):
        Tuesday+=str(row[2])
        Tuesday= Tuesday[:-3] + " / "

    elif(row[1]=="WED"):
        Wednesday+=str(row[2])
        Wednesday= Wednesday[:-3] + " / "

    elif(row[1]=="THU"):
        Thursday+=str(row[2])
        Thursday= Thursday[:-3] + " / "

    elif(row[1]=="FRI"):
        Friday+=str(row[2])
        Friday= Friday[:-3] + " / "

    elif(row[1]=="SAT"):
        Saturday+=str(row[2])
        Saturday= Saturday[:-3] + " / "

    elif(row[1]=="SUN"):
        Sunday+=str(row[2])
        Sunday= Sunday[:-3] + " / "

print("<br>")
print("<br>")
print("<form method=\"post\" id=\"Ducha\" name=\"Ducha\" action=\"/cgi-bin/ducha.py\">")
print("<table style=\"width:100%\">")
print("  <tr>")
print("  </tr>")
print("  <tr>")
print("<td>")
print("        <td align=\"left\">")
print("<table class=\"blueTable\">")
print("<thead>")
print("<tr>")
print("<th>DIA</th>")
print("<th>HORAS</th>")
print("</tr>")
print("</thead>")
print("<tbody>")
print("<tr>")
print("<td>MON</td><td>"+Monday+"</td></tr>")
print("<tr>")
print("<td>TUE</td><td>"+Tuesday+"</td></tr>")
print("<tr>")
print("<td>WED</td><td>"+Wednesday+"</td></tr>")
print("<tr>")
print("<td>THU</td><td>"+Thursday+"</td></tr>")
print("<tr>")
print("<td>FRI</td><td>"+Friday+"</td></tr>")
print("<tr>")
print("<td>SAT</td><td>"+Saturday+"</td></tr>")
print("<tr>")
print("<td>SUN</td><td>"+Sunday+"</td></tr>")
print("</tbody>")
print("</tr>")
print("</table>")
print("</td>")
print("        <td><img src=\"/images/Ducha.jpg\" alt=\"Ducha\"style=\"width:150px;height:250px;\">")
print("                <div class=\"onoffswitch\">")
print("                <input type=\"checkbox\" name=\"onoffswitch\" class=\"onoffswitch-checkbox\" id=\"myonoffswitch\"" + switch + ">")
print("                <label class=\"onoffswitch-label\" for=\"myonoffswitch\">")
print("                <span class=\"onoffswitch-inner\"></span>")
print("                <span class=\"onoffswitch-switch\"></span>")
print("                </label>")
print("                </div>")
print("        <button id='submitButton'  class=\"push_button blue\">Actualizar</button>")
print("        </td>")
print("</form>")
print("<form method=\"post\" id=\"Manual\" name=\"Manual\" action=\"/cgi-bin/manual.py\">")
print("        <td><img src=\"/images/Caldera.jpg\" alt=\"Caldera\"style=\"width:150px;height:250px;\">")
print("                <div class=\"onoffswitch\">")
print("                <input type=\"checkbox\" name=\"onoffswitch2\" class=\"onoffswitch-checkbox\" id=\"myonoffswitch2\"" + switch2 + ">")
print("                <label class=\"onoffswitch-label\" for=\"myonoffswitch2\">")
print("                <span class=\"onoffswitch-inner\"></span>")
print("                <span class=\"onoffswitch-switch\"></span>")
print("                </label>")
print("                </div>")
print("        <button id='submitButton'  class=\"push_button blue\">Actualizar</button>")
print("        </td>")

print("<br>")
print("<br>")
print("<table>")
print("  <tr>")
print("        <td width=\"71%\"></td>")
print("        <td></td>")
print("        <td align=\"left\">")
#print("             <button id='submitButton' class='button'>Update</button>")
print("        </td>")
print("  </tr>")
print("</table>")
print("</form>")
print("</body>")
print("</html>")
