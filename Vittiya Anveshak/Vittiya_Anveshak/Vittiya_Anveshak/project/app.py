# Importing required libraries
from flask import Flask, render_template
from financial_analysis import financial_analysis_bp
from fund_trail import fund_trail_bp

app = Flask(__name__)

# Registering blueprints
app.register_blueprint(financial_analysis_bp)
app.register_blueprint(fund_trail_bp)

# Home page
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)

