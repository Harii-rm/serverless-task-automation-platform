import axios from 'axios';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

export const authService = {
    login: async (email, password) => {
        const response = await api.post('/auth/login', { email, password });
        if (response.data.access_token) {
            localStorage.setItem('token', response.data.access_token);
        }
        return response.data;
    },
    logout: () => {
        localStorage.removeItem('token');
    },
    isAuthenticated: () => {
        return !!localStorage.getItem('token');
    }
};

export const rulesService = {
    getDashboardStats: async () => {
        const response = await api.get('/dashboard-stats');
        return response.data;
    },
    getRules: async () => {
        const response = await api.get('/rules');
        return response.data;
    },
    createRule: async (ruleData) => {
        const response = await api.post('/rules', ruleData);
        return response.data;
    },
    updateRule: async (id, ruleData) => {
        const response = await api.put(`/rules/${id}`, ruleData);
        return response.data;
    },
    deleteRule: async (id) => {
        const response = await api.delete(`/rules/${id}`);
        return response.data;
    },
    getLogs: async () => {
        const response = await api.get('/logs');
        return response.data;
    }
};

export default api;
