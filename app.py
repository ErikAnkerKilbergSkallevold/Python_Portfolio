from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def my_home():  # put application's code here
    return render_template("index.html")

@app.route('/')
def my_index():  # put application's code here
    return render_template("index.html")

@app.route('/<string:page_name>')
def html_page(page_name):  # put application's code here
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        except:
            return "Could not save to database"
    else:
        return "Something is wrong"

def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        file = database.write(f"\n{email},{subject},{body}")

def write_to_csv(data):
    with open("database.csv", mode="a", newline='') as database:
        email = data["email"]
        subject = data["subject"]
        body = data["body"]
        csv_writer = csv.writer(database, delimiter=",", quotechar="'", quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, body]),

if __name__ == '__main__':
    app.run()
