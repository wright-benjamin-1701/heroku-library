from flask import Flask, Blueprint, render_template

from src.models import top_df

# Create a blueprint
home_bp = Blueprint('home', __name__, template_folder='templates')

@home_bp.route('/list/<type>')
def test(type):
    return render_template('top.html',items=top_df[top_df['type']==type])


