import axios from 'axios';

const API_URL = 'https://api.directlink.com';

const getToken = () => {
  return localStorage.getItem('token');
};

const api = axios.create({
  baseURL: API_URL,
});

// Add a request interceptor
api.interceptors.request.use(
  config => {
    const token = getToken();
    if (token) {
      config.headers['Authorization'] = `Bearer ${token}`;
    }
    return config;
  },
  error => {
    return Promise.reject(error);
  }
);

export default api;
