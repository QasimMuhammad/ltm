import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <section style={{
        background: 'linear-gradient(to bottom right, #fff0f3, #ffe6ee)',
        padding: '80px 0',
        textAlign: 'center'
      }}>
        <div className="container">
          <h1 style={{ fontSize: '48px', marginBottom: '20px', color: 'var(--primary-color)' }}>
            Prepare for a Lifetime of Love
          </h1>
          <p style={{ fontSize: '20px', marginBottom: '40px', maxWidth: '700px', margin: '0 auto 40px', color: 'var(--dark-color)' }}>
            Marriage is a significant life change that requires preparation. LTM helps couples and families understand each other better before this important step.
          </p>
          <Link to="/questionnaire/couple" className="btn btn-primary">
            Start Questionnaire
          </Link>
        </div>
      </section>

      <section style={{ padding: '80px 0', background: 'white' }}>
        <div className="container">
          <h2 style={{ fontSize: '36px', textAlign: 'center', marginBottom: '50px' }}>
            Our Services
          </h2>
          <div style={{
            display: 'grid',
            gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))',
            gap: '30px'
          }}>
            <div style={{
              padding: '30px',
              borderRadius: '10px',
              boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
              textAlign: 'center'
            }}>
              <i className="fas fa-clipboard-list" style={{ fontSize: '48px', color: 'var(--primary-color)', marginBottom: '20px' }}></i>
              <h3 style={{ marginBottom: '15px' }}>Couple Questionnaires</h3>
              <p style={{ marginBottom: '20px' }}>
                Thoughtful questions to help couples understand each other better.
              </p>
              <Link to="/questionnaire/couple" className="btn btn-primary">Get Started</Link>
            </div>

            <div style={{
              padding: '30px',
              borderRadius: '10px',
              boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
              textAlign: 'center'
            }}>
              <i className="fas fa-heart" style={{ fontSize: '48px', color: 'var(--primary-color)', marginBottom: '20px' }}></i>
              <h3 style={{ marginBottom: '15px' }}>Family Questions</h3>
              <p style={{ marginBottom: '20px' }}>
                Bridge cultural and expectation gaps between families.
              </p>
              <Link to="/questionnaire/parent" className="btn btn-primary">Learn More</Link>
            </div>

            <div style={{
              padding: '30px',
              borderRadius: '10px',
              boxShadow: '0 2px 10px rgba(0,0,0,0.1)',
              textAlign: 'center'
            }}>
              <i className="fas fa-hands-helping" style={{ fontSize: '48px', color: 'var(--primary-color)', marginBottom: '20px' }}></i>
              <h3 style={{ marginBottom: '15px' }}>Conflict Resolution</h3>
              <p style={{ marginBottom: '20px' }}>
                Professional guidance for couples facing challenges.
              </p>
              <a href="#contact" className="btn btn-primary">Contact Us</a>
            </div>
          </div>
        </div>
      </section>
    </div>
  );
}

export default Home;

