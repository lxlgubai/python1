from bs4 import BeautifulSoup
with open("datacenter.html", "r+", encoding='utf-8') as html:
    html_bf = BeautifulSoup(html, 'lxml')
    divs = html_bf.select('.chart-container')
    divs[0]["style"] = "width:10%;height:10%;position:absolute;top:0;left:2%;"
    divs[1]["style"] = "width:40%;height:40%;position:absolute;top:12%;left:0;"
    divs[2]["style"] = "width:35%;height:10%;position:absolute;top:2%;left:30%;"
    divs[3]["style"] = "width:40%;height:40%;position:absolute;top:10%;left:28%;"
    divs[4]["style"] = "width:40%;height:35%;position:absolute;top:12%;left:55%;"
    divs[5]["style"] = "width:30%;height:35%;position:absolute;top:60%;left:2%;"
    divs[6]["style"] = "width:60%;height:50%;position:absolute;top:45%;left:15%;"
    divs[7]["style"] = "width:35%;height:40%;position:absolute;top:50%;left:60%;"
    body = html_bf.find("body")
    body["style"] = "background-image: "  # 背景颜色
    html_new = str(html_bf)
    html.seek(0, 0)
    html.truncate()
    html.write(html_new)
    html.close()
