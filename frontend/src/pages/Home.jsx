import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      {/* Hero Section */}
      <section id="hero">
        <div className="container">
          <h2>About LTM</h2>
          <p>
            Marriage is a significant life change that requires preparation. LTM helps couples 
            and families understand each other better before this important step. Our questionnaires 
            and consultations bridge gaps in understanding, align expectations, and build stronger 
            foundations for a happy married life.
          </p>
          <div className="cta-buttons">
            <a href="#services" className="btn primary">Explore Our Services</a>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services">
        <div className="container">
          <h2>Our Services</h2>
          <div className="service-cards">
            <div className="card">
              <div className="card-icon">
                <i className="fas fa-clipboard-list"></i>
              </div>
              <h3>Couple & Family Questionnaires</h3>
              <p>Thoughtful questions to help couples and their families understand each other better and bridge cultural and expectation gaps.</p>
              <ul className="service-features">
                <li>Personalized questions for couples</li>
                <li>Family culture assessment</li>
                <li>Expectation alignment tools</li>
                <li>Guided discussion prompts</li>
              </ul>
              <Link to="/questionnaire/couple" className="btn">Start Questionnaire</Link>
            </div>
            
            <div className="card featured">
              <div className="card-icon">
                <i className="fas fa-heart"></i>
              </div>
              <h3>Pre-Marriage Consultation</h3>
              <p>Expert-facilitated discussions to help couples prepare for marriage with clarity and confidence.</p>
              <ul className="service-features">
                <li>One-on-one sessions with experts</li>
                <li>Customized preparation plans</li>
                <li>Communication skill building</li>
                <li>Conflict resolution strategies</li>
              </ul>
              <a href="#consultation" className="btn">Book Consultation</a>
            </div>
            
            <div className="card">
              <div className="card-icon">
                <i className="fas fa-hands-helping"></i>
              </div>
              <h3>Marriage Conflict Resolution</h3>
              <p>Professional guidance for married couples facing challenges, helping restore harmony and understanding.</p>
              <ul className="service-features">
                <li>Mediated discussions</li>
                <li>Relationship rebuilding techniques</li>
                <li>Emotional intelligence coaching</li>
                <li>Long-term harmony strategies</li>
              </ul>
              <a href="#consultation" className="btn">Book Now</a>
            </div>
          </div>
        </div>
      </section>

      {/* Process Section */}
      <section id="process">
        <div className="container">
          <h2>How It Works</h2>
          <div className="process-steps">
            <div className="step">
              <div className="step-number">1</div>
              <h3>Complete Questionnaires</h3>
              <p>Both partners and family members fill out our thoughtfully designed questionnaires.</p>
            </div>
            <div className="step">
              <div className="step-number">2</div>
              <h3>Review Results</h3>
              <p>Receive personalized insights about compatibility and potential areas for growth.</p>
            </div>
            <div className="step">
              <div className="step-number">3</div>
              <h3>Optional Consultation</h3>
              <p>Book a session with our experts to discuss results and develop strategies.</p>
            </div>
            <div className="step">
              <div className="step-number">4</div>
              <h3>Build a Stronger Foundation</h3>
              <p>Enter marriage with greater understanding and preparation for a lifetime of love.</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer>
        <div className="container">
          <p>&copy; 2023 LTM.com - License to Marry. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default Home;
