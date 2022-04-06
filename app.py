from flask import Flask
from flask import render_template, redirect, request, url_for

app = Flask(__name__)

price_estimate = [{"price": ""}]

@app.route('/')
def index():
    return render_template('index.html', pageTitle='Vertical Tank Maintenance')

@app.route('/about')
def about():
    return render_template('about.html', pageTitle='About VTM')

@app.route('/estimate')
def estimate():
    return render_template('estimate.html', pageTitle='Price Estimator', estimates = price_estimate)

@app.route('/estimate_price', methods=['GET', 'POST'])
def add_friend():
    if request.method == 'POST':
        form = request.form
        radius = int(form['radius'])
        height = int(form['height'])
        pi = 3.14
        area_t = pi * (radius*radius)
        area_s = 2*(pi*(radius * height))
        tot_area = area_t + area_s
        tot_sf = tot_area/144
        tot_mc = tot_sf * 25
        tot_lc = tot_sf * 15
        total_cost = tot_mc + tot_lc
        tot_cost = "$" + str(round(total_cost, 2))
        cost_dict = {"price": tot_cost}
        price_estimate.append(cost_dict)
        return redirect(url_for('estimate'))
    return redirect(url_for('estimate'))
    

if __name__ == '__main__':
    app.run(debug=True)
