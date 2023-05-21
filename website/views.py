from flask import Blueprint, render_template, request, url_for, redirect

views = Blueprint('views', __name__) 

@views.route('/', methods=["GET", "POST"])
def index():
    # Redirects to dorms page if search is submitted
    if request.method == "POST":
        search = request.form["search"]
        return redirect(url_for('ratings.dorms'))
    return render_template('index.html')