import { API } from "./_axios";

interface LoginPayload {
    email: string;
    password: string;
}

interface RegisterPayload {
    username: string;
    email: string;
    password: string;
}

interface User {
    id: number;
    username: string;
    email: string;
}

interface AuthResponse {
    message: string;
    user: User;
}

export const login = async (email: string, password: string): Promise<AuthResponse> => {
    try {
        const response = await API.post('/login', {
            email,
            password
        }, {
            headers: { 'Content-Type': 'application/json' },
            withCredentials: true
        });
        return response.data;
    } catch (error) {
        console.error(`Error during login:`, error);
        throw error;
    }
}

export const register = async (username: string, email: string, password: string): Promise<AuthResponse> => {
    try {
        const response = await API.post('/register', {
            username,
            email,
            password
        }, {
            headers: { 'Content-Type': 'application/json' },
            withCredentials: true
        });
        return response.data;
    } catch (error) {
        console.error(`Error during registration:`, error);
        throw error;
    }
}

export const logout = async (): Promise<{ message: string }> => {
    try {
        const response = await API.post('/logout', {}, {
            withCredentials: true
        });
        return response.data;
    } catch (error) {
        console.error(`Error during logout:`, error);
        throw error;
    }
}

export const getCurrentUser = async (): Promise<{ user: User }> => {
    try {
        const response = await API.get('/user', {
            withCredentials: true
        });
        return response.data;
    } catch (error) {
        console.error(`Error getting current user:`, error);
        throw error;
    }
}