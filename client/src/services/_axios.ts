import axios from "axios";

export const API = axios.create({
    baseURL: `${import.meta.env.VITE_API_URL}/api`,
    withCredentials: true,
});

export const ADMIN = axios.create({
    baseURL: `${import.meta.env.VITE_API_URL}/admin`,
    withCredentials: true,
});