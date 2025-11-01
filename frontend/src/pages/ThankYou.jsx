import React from 'react';
import { Link } from 'react-router-dom';

function ThankYou() {
  return (
    <div style={{ textAlign: 'center', padding: '80px 0' }}>
      <div className="container">
        <i className="fas fa-check-circle" style={{ fontSize: '80px', color: 'var(--primary-color)', marginBottom: '30px' }}></i>
        <h1 style={{ fontSize: '42px', marginBottom: '20px', color: 'var(--primary-color)' }}>
          Thank You!
        </h1>
        <p style={{ fontSize: '20px', marginBottom: '40px', color: '#666', maxWidth: '600px', margin: '0 auto 40px' }}>
          Your responses have been received successfully. We appreciate you taking the time to complete the questionnaire.
        </p>
        <Link to="/" className="btn btn-primary">
          Return to Home
        </Link>
      </div>
    </div>
  );
}

export default ThankYou;

