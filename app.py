from flask import Flask,render_template,request,redirect

app = Flask(__name__)

students = [
    {"name":"张三", "chinese":80, "math":75, "english":85},
    {"name":"李四", "chinese":60, "math":95, "english":80},
    {"name":"王五", "chinese":70, "math":85, "english":90},
    {"name":"赵六", "chinese":90, "math":70, "english":75},
    {"name":"钱七", "chinese":85, "math":80, "english":70}
]

@app.route("/")
def helloworld():
    return "Hello World!"

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # TODO：登录成功之后，链接数据库，校验账户密码
        print("Username: {} Password: {}".format(username,password))
        return redirect("/admin")

    return render_template("login.html")

@app.route("/admin")
def admin():

    return render_template("admin.html", students=students)

@app.route("/add",methods=["GET","POST"])
def add():
    if request.method == "POST":
        name = request.form.get("username")
        chinese = request.form.get("chinese")
        math = request.form.get("math")
        english = request.form.get("english")
        students.append({"name":name,"chinese":chinese,"math":math,"english":english})
        return redirect("/admin")
    return render_template("add.html")

@app.route("/delete")
def delete():
    name = request.args.get("name")
    for i in students:
        if i["name"] == name:
            students.remove(i)
    return redirect("/admin")

@app.route("/change",methods=["GET","POST"])
def change():
    username = request.args.get("name")
    if request.method == "POST":
        username = request.form.get("username")
        chinese = request.form.get("chinese")
        math = request.form.get("math")
        english = request.form.get("english")
        for stu in students:
            if stu["name"] == username:
                stu["chinese"] = chinese
                stu["math"] = math
                stu["english"] = english
        return redirect("/admin")
    for stu in students:
        if stu["name"] == username:
            return render_template("change.html",students=stu)
        

if __name__ == "__main__":
    app.run(debug=True)