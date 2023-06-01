from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    data = request.form
    count = int(data["strawberry"])+int(data["raspberry"])+int(data["apple"])
    print(f'Charging {data["first_name"]} for {count} fruits.')
    return render_template("checkout.html", data=data)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    