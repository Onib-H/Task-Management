import { API } from "./_axios";

export const getMessage = async () => {
    try {
        const response = await API.get('/', {
            headers: { 'Content-Type': 'application/json' }
        });
        console.log(response.data);
        return response.data;
    } catch (error) {
        console.error(`Error fetching message: ${error}`);
        throw error;
    }
}