from flask import Flask, render_template
app = Flask(__name__)

@app.route("/myname/<name>")
def hello_world(name):
    return f"Hello, Worlddddddd........! {name}"

@app.route("/myprofile")
def myprofile():
    return render_template("my_profile.html", username="Wanarase", age=26, title="My Profile", is_admin = True)

@app.route("/tickets/<int:ticket_id>")
def ticket_detail(ticket_id):
    return f"Ticket #{ticket_id}"

@app.route("/")
def index():
    return render_template("home.html", title="Home")


@app.route("/about")
def about():
    print("call about page!!!!!!!!!!!")
    return render_template("about.html", title="about")


request = [
    {"ids": 1, "case_name": "แจ้งซ่อมพัดลม"},
    {"ids": 2, "case_name": "แจ้งซ่อมแอร์"},
    {"ids": 3, "case_name": "แจ้งซ่อมประตู"}
    ]

@app.route("/listRequest")
def list_request(): 
    return render_template("request_cases.html", request_cases=request, title = "Case")

@app.route("/new_case")
def new_case():
    return render_template("new.html")


if __name__ == "__main__":
  app.run(debug=True, port =8000, host='0.0.0.0')