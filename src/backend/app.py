from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_cors import CORS
import os
from dotenv import load_dotenv
from src.backend.models.database import init_db, Session
from src.backend.models.models import Question

# Load environment variables
load_dotenv()

app = Flask(__name__, 
            static_folder="../../static",
            template_folder="../../templates")
CORS(app)

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')

# Initialize the database
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/health')
def health_check():
    return jsonify({"status": "healthy"})

@app.route('/questionnaire/couple')
def couple_questionnaire():
    # Get all couple questions from the database
    db_session = Session()
    questions = db_session.query(Question).filter_by(question_type='couple').all()
    db_session.close()
    
    return render_template('couple_questionnaire.html', questions=questions)

@app.route('/questionnaire/parent')
def parent_questionnaire():
    # Get all parent questions from the database
    db_session = Session()
    questions = db_session.query(Question).filter_by(question_type='parent').all()
    db_session.close()
    
    return render_template('parent_questionnaire.html', questions=questions)

@app.route('/submit/couple_questionnaire', methods=['POST'])
def submit_couple_questionnaire():
    if request.method == 'POST':
        db_session = Session()
        
        # Get personal information
        name = request.form.get('name')
        status = request.form.get('status')
        email = request.form.get('email')
        
        # In a real app, you'd create or get the user here
        # For now, we'll just print the information
        print(f"Submission from: {name} ({email}) - Status: {status}")
        
        # Process each question response
        for key, value in request.form.items():
            if key.startswith('question_'):
                question_id = int(key.split('_')[1])
                
                # Get the question to log the category
                question = db_session.query(Question).get(question_id)
                if question:
                    print(f"Response to '{question.text}' ({question.category}): {value[:50]}...")
                
                # In a real app, you'd store this in the database
                # For now, we're just logging it
        
        db_session.close()
        
        # Redirect to a thank you page
        return redirect(url_for('thank_you'))
    
    # If not a POST request, redirect to the questionnaire
    return redirect(url_for('couple_questionnaire'))

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(debug=True) 