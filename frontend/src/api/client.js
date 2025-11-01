import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Question API
export const questionsApi = {
  getAll: (type = 'couple') => 
    apiClient.get('/questions', { params: { type } }),
  
  getById: (id) => 
    apiClient.get(`/questions/${id}`),
};

// Responses API
export const responsesApi = {
  submitCouple: (responses) => 
    apiClient.post('/responses/couple', { responses }),
  
  submitParent: (responses) => 
    apiClient.post('/responses/parent', { responses }),
};

