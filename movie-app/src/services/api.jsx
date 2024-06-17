import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

export const getMovies = () => axios.get(`${API_BASE_URL}/movies`);
export const createMovie = (movie) => axios.post(`${API_BASE_URL}/movies`, movie);
export const updateMovie = (movieId, movie) => axios.put(`${API_BASE_URL}/movies/${movieId}`, movie);
export const deleteMovie = (movieId) => axios.delete(`${API_BASE_URL}/movies/${movieId}`);

export const getDirectors = () => axios.get(`${API_BASE_URL}/directors`);
export const createDirector = (director) => axios.post(`${API_BASE_URL}/directors`, director);
export const updateDirector = (directorId, director) => axios.put(`${API_BASE_URL}/directors/${directorId}`, director);
export const deleteDirector = (directorId) => axios.delete(`${API_BASE_URL}/directors/${directorId}`);