from flask import Blueprint, jsonify, request
from src.backend.models.database import Session
from src.backend.models.models import Question, User, CoupleResponse
from typing import List, Dict

api_bp = Blueprint('api', __name__, url_prefix='/api')


@api_bp.route('/questions', methods=['GET'])
def get_questions():
    """Get all questions by type"""
    question_type = request.args.get('type', 'couple')
    
    session = Session()
    try:
        questions = session.query(Question).filter_by(question_type=question_type).all()
        return jsonify({
            'success': True,
            'count': len(questions),
            'questions': [
                {
                    'id': q.id,
                    'text': q.text,
                    'category': q.category,
                    'question_type': q.question_type,
                    'options': q.options
                }
                for q in questions
            ]
        })
    finally:
        session.close()


@api_bp.route('/questions/<int:question_id>', methods=['GET'])
def get_question(question_id: int):
    """Get a specific question"""
    session = Session()
    try:
        question = session.query(Question).get(question_id)
        if question:
            return jsonify({
                'success': True,
                'question': {
                    'id': question.id,
                    'text': question.text,
                    'category': question.category,
                    'question_type': question.question_type,
                    'options': question.options
                }
            })
        return jsonify({'success': False, 'error': 'Question not found'}), 404
    finally:
        session.close()


@api_bp.route('/responses/couple', methods=['POST'])
def submit_couple_responses():
    """Submit couple questionnaire responses"""
    data = request.get_json()
    
    if not data or 'responses' not in data:
        return jsonify({'success': False, 'error': 'Invalid request data'}), 400
    
    session = Session()
    try:
        # TODO: Create user and store responses in database
        # For now, just validate the structure
        
        return jsonify({
            'success': True,
            'message': 'Responses received successfully',
            'count': len(data.get('responses', []))
        })
    except Exception as e:
        session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        session.close()


@api_bp.route('/responses/parent', methods=['POST'])
def submit_parent_responses():
    """Submit parent questionnaire responses"""
    data = request.get_json()
    
    if not data or 'responses' not in data:
        return jsonify({'success': False, 'error': 'Invalid request data'}), 400
    
    session = Session()
    try:
        # TODO: Create user and store responses in database
        
        return jsonify({
            'success': True,
            'message': 'Responses received successfully',
            'count': len(data.get('responses', []))
        })
    except Exception as e:
        session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500
    finally:
        session.close()


@api_bp.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'LTM Backend API',
        'version': '0.1.0'
    })

