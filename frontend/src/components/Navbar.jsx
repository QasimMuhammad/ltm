import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <header style={{
      background: 'white',
      boxShadow: '0 2px 5px rgba(0,0,0,0.1)',
      position: 'sticky',
      top: 0,
      zIndex: 100
    }}>
      <div className="container">
        <div style={{
          display: 'flex',
          justifyContent: 'space-between',
          alignItems: 'center',
          padding: '20px 0'
        }}>
          <Link to="/" style={{ textDecoration: 'none', color: 'var(--primary-color)' }}>
            <h1 style={{ fontSize: '24px', fontWeight: 'bold' }}>License to Marry</h1>
          </Link>
          <nav>
            <Link to="/" style={{ marginRight: '20px', textDecoration: 'none', color: 'var(--dark-color)' }}>Home</Link>
            <Link to="/questionnaire/couple" style={{ marginRight: '20px', textDecoration: 'none', color: 'var(--dark-color)' }}>Questionnaire</Link>
          </nav>
        </div>
      </div>
    </header>
  );
}

export default Navbar;

