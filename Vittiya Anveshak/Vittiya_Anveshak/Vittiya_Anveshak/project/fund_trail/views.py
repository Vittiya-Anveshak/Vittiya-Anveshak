from . import fund_trail_bp
from flask import render_template

# Fund Trail route
@fund_trail_bp.route('/fund_trail')
def fund_trail():
    # Add your fund trail specific features here
    return render_template('fund_trail.html')
