from flask import Flask, render_template, request
import requests
from smtplib import SMTP

OWN_EMAIL = "YOUR EMAIL"
OWN_PASSWORD = "YOUR PASSWORD"
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

@app.get("/contact")
def contact():
    header_title = "Contact"
    return render_template("contact.html", title=header_title, msg_sent=False)

@app.post("/contact")
def receive_data():
    header_title = "Contact"
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]

    send_email(name, email, phone, message)

    return render_template("contact.html", title=header_title, msg_sent=True)

@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in data:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, email_message)

if __name__ == "__main__":
    app.run(debug=True)
