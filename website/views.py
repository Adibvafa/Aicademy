from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
# from flask_login import login_required, current_user
# from .models import Note
# from . import db
# from sqlalchemy.sql import func
import json

# courseText
# quizQuestions
# response


# usually easier to keep the name the same as the file
views = Blueprint('views', __name__)

# homepage
@views.route('/', methods=['GET', 'POST'])
# @login_required
def home():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)

        if len(query) < 1:
            flash('Query is too short!', category="error")
        else:
            return redirect(url_for('views.query'))
            # new_note = Note(data=note, user_id=current_user.id)
            # print(current_user.id)
            # db.session.add(new_note)
            # db.session.commit()
            # flash("Note added!")

    return render_template("home.html")

@views.route('/query', methods=['GET', 'POST'])
def query():
    return render_template('query.html', text="Hello World")

# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)      # loads as a dictionary object
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()
    
#     return jsonify({})