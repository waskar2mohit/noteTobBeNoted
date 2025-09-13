from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from .models import Note
from . import db

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/add-note', methods=['POST'])
@login_required
def add_note():
    note_data = request.form.get('note')
    if note_data:
        new_note = Note(data=note_data, user_id=current_user.id)
        db.session.add(new_note)
        db.session.commit()
    return redirect(url_for('views.home'))
