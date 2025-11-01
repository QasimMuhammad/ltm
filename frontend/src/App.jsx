import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import Home from './pages/Home';
import CoupleQuestionnaire from './pages/CoupleQuestionnaire';
import ParentQuestionnaire from './pages/ParentQuestionnaire';
import ThankYou from './pages/ThankYou';
import Navbar from './components/Navbar';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/questionnaire/couple" element={<CoupleQuestionnaire />} />
          <Route path="/questionnaire/parent" element={<ParentQuestionnaire />} />
          <Route path="/thank-you" element={<ThankYou />} />
        </Routes>
      </Router>
    </QueryClientProvider>
  );
}

export default App;

