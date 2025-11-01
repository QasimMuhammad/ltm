import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useQuery, useMutation } from '@tanstack/react-query';
import { questionsApi, responsesApi } from '../api/client';

function CoupleQuestionnaire() {
  const navigate = useNavigate();
  const [responses, setResponses] = useState({});
  
  const { data: questionsData, isLoading, error } = useQuery({
    queryKey: ['coupleQuestions'],
    queryFn: () => questionsApi.getAll('couple'),
    select: (data) => data.data.questions,
  });
  
  const submitMutation = useMutation({
    mutationFn: responsesApi.submitCouple,
    onSuccess: () => {
      navigate('/thank-you');
    },
    onError: (error) => {
      alert('Error submitting questionnaire: ' + error.message);
    },
  });
  
  const handleSubmit = (e) => {
    e.preventDefault();
    const formattedResponses = Object.entries(responses).map(([questionId, answer]) => ({
      question_id: parseInt(questionId),
      response: answer,
    }));
    
    submitMutation.mutate({ responses: formattedResponses });
  };
  
  const handleChange = (questionId, value) => {
    setResponses(prev => ({
      ...prev,
      [questionId]: value,
    }));
  };
  
  if (isLoading) return <div className="loading">Loading questions...</div>;
  if (error) return <div className="error">Error loading questions: {error.message}</div>;
  
  return (
    <div className="questionnaire-container">
      <h1 style={{ marginBottom: '30px', color: 'var(--primary-color)' }}>Couple Questionnaire</h1>
      <p style={{ marginBottom: '30px', color: '#666' }}>
        Please answer the following questions honestly and thoughtfully. This will help us provide you with meaningful insights.
      </p>
      
      <form onSubmit={handleSubmit}>
        {questionsData?.map((question, idx) => (
          <div key={question.id} className="question-group">
            <label>
              <span className="question-number">{idx + 1}.</span>
              {question.text}
              {question.category && (
                <span className="category">({question.category})</span>
              )}
            </label>
            <textarea
              value={responses[question.id] || ''}
              onChange={(e) => handleChange(question.id, e.target.value)}
              placeholder="Your response..."
              rows={4}
              required
            />
          </div>
        ))}
        
        <div className="form-actions">
          <button 
            type="submit" 
            disabled={submitMutation.isPending}
            className="btn btn-primary"
          >
            {submitMutation.isPending ? 'Submitting...' : 'Submit Answers'}
          </button>
        </div>
      </form>
    </div>
  );
}

export default CoupleQuestionnaire;

