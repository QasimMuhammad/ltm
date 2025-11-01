import React from 'react';
import { Link } from 'react-router-dom';

function Navbar() {
  return (
    <header>
      <div className="container">
        <p className="tagline">License to Marry - Prepare for a Lifetime of Love</p>
        <nav>
          <ul>
            <li><a href="#hero">About</a></li>
            <li><a href="#services">Our Services</a></li>
            <li><Link to="/questionnaire/couple">Questionnaire</Link></li>
            <li><a href="#consultation">Consultation</a></li>
            <li><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Navbar;
