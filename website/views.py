from flask import Blueprint, redirect, render_template, request, flash, jsonify, url_for
# from flask_login import login_required, current_user
# from .models import Note
# from . import db
# from sqlalchemy.sql import func
import json

# courseText
# quizQuestions
# response
# summary
# images

prompt = "default"
courseParagraphs = []
courseImages = []

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
            global prompt, courseParagraphs, courseImages
            prompt = query
            for i in range(8):
                courseParagraphs.append("Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse sequi omnis facere, \
                iure earum odit vel eum similique eaque sapiente alias, dicta praesentium placeat harum eveniet. \
                Natus quasi saepe eum?")
                courseImages.append(url_for('static', filename='images/Fantasy.jpeg'))
            return redirect(url_for('views.query'))
            # new_note = Note(data=note, user_id=current_user.id)
            # print(current_user.id)
            # db.session.add(new_note)
            # db.session.commit()
            # flash("Note added!")

    return render_template("home.html")

@views.route('/query', methods=['GET', 'POST'])
def query():
    return render_template('query.html', prompt=prompt, courseParagraphs=courseParagraphs, courseImages=courseImages)

@views.route('/generate-response', methods=['POST'])
def generate_response():
    prompt = json.loads(request.data)
    promptText = prompt['text']
    print(promptText)
    return jsonify({"resp": "Hello User!"})

@views.route('/generate-summary', methods=['POST'])
def generate_summary():
    # prompt = json.loads(request.data)
    # promptText = prompt['text']
    # print(promptText)
    return jsonify({"resp": "Hello User!skjdfnkjsf;ksdjf;sdkjfs;dkjf;kld\nsdijfkdsjfkdsjf"})

@views.route('/generate-quiz', methods=['POST'])
def generate_quiz():
    # prompt = json.loads(request.data)
    # promptText = prompt['text']
    # print(promptText)
    return jsonify({"question": "What are the first 10 digits of pi?", "answer": "3.141592653", "reference": 3})

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