import { API } from "./_axios";

export const login = async (username: string, password: string) => {
    try {
        const response = await API.post('/login', {
            username,
            password
        }, {
            headers: { 'Content-Type': 'application/json' },
            withCredentials: true
        });
        return response.data;
    } catch (error) {
        console.error(`Error during login: ${error}`);
        throw error;
    }
}