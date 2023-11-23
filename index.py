import requests
import bs4
from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    html = requests.get('https://www1.pu.edu.tw/~tcyang/course.html')
    html.encoding = "utf-8"
    a = bs4.BeautifulSoup(html.text,"html.parser")

    title = a.find("section",class_ = "testimonial-area")
    titles = title.find_all("div",class_= "team-box")

    # print(title)
    l = []
    for i in titles:
        print(i.h4.text)
        print(i.p.text)
        print(i.a["href"])
        print("https://www1.pu.edu.tw/~tcyang/"+i.a.img["src"])
        a = [i.h4.text,i.p.text,i.a["href"],"https://www1.pu.edu.tw/~tcyang/"+i.a.img["src"]]
        l.append(a)
    print(l)
    return render_template("index.html",a =l)
app.run()
