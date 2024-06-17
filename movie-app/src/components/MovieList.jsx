import React, { useState, useEffect } from 'react';
import { getMovies } from '../services/api.jsx';

const MovieList = () => {
  const [movies, setMovies] = useState([]);

  useEffect(() => {
    const fetchMovies = async () => {
      try {
        const response = await getMovies();
        setMovies(response.data);
      } catch (error) {
        console.error('Error fetching movies:', error);
      }
    };
    fetchMovies();
  }, []);

  return (
    <div>
      <h2>Movie List</h2>
      <ul>
        {movies.map((movie) => (
          <li key={movie.id}>
            {movie.title} ({movie.year}) - {movie.genre} - Directed by {movie.director_id} - Rating: {movie.rating}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MovieList;