import json

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

from NeetCode.solution import Solution

app = Flask(__name__, template_folder='./')

class GridForm(FlaskForm):
    grid = TextAreaField('Enter your grid (in JSON format):', validators=[DataRequired()])
    submit = SubmitField('Submit')

class App(Flask):
    def __init__(self):
        super().__init__(__name__, template_folder='./')
        self.config['SECRET_KEY'] = 'random_csrf_token'
        self.solution = Solution()
        self.route('/', methods=['GET', 'POST'])(self.home)

    def home(self):
        form = GridForm()
        time = None
        if form.validate_on_submit():
            grid = json.loads(form.grid.data)
            time = self.solution.orangesRotting(grid)
        return render_template('./home.html', form=form, time=time)
    
if __name__ == "__main__":
    app = App()
    app.run(debug=False)
