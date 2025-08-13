from flask import Flask, render_template
import requests

app = Flask(__name__)

connect = requests.get("https://api.npoint.io/b6b7303ef710d7319459")
connect.raise_for_status()
data = connect.json()
print(data)

@app.route("/")
def home():
    header_title = "Home"
    return render_template("index.html", data=data, title=header_title)

@app.route("/about")
def about():
    header_title = "About"
    return render_template("about.html", title=header_title)

@app.route("/contact")
def contact():
    header_title = "Contact"
    return render_template("contact.html", title=header_title)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True)
