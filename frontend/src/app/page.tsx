'use client';

import React, { useState } from 'react';
import SearchInput from '@/app/components/SearchInput';
import SearchResults from '@/app/components/SearchResults';
import LoadingIndicator from '@/app/components/LoadingIndicator';
import ErrorMessage from '@/app/components/ErrorMessage';

const HomePage: React.FC = () => {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async (query: string) => {
    setLoading(true);
    setError('');
    setResults([]);

    try {
      const response = await fetch(`http://localhost:8000/api/search/?query=${encodeURIComponent(query)}`, {
        method: 'GET',
      });

      if (response.ok) {
        const data = await response.json();
        const mappedResults = data.map((car: any) => ({
          id: car.id,
          name: `${car.make} ${car.model}`,
          price: car.price,
          features: `Year: ${car.year}, Transmission: ${car.transmission}, Fuel: ${car.fuel_type}`,
        }));
        setResults(mappedResults);
      } else {
        throw new Error('Failed to fetch results.');
      }
    } catch (err) {
      setError(err instanceof Error ? err.message : 'An unknown error occurred.');
    } finally {
      setLoading(false);
    }

  };

  return (
    <div className="min-h-screen bg-gray-100">
      <SearchInput onSearch={handleSearch} />
      {loading && <LoadingIndicator />}
      {error && <ErrorMessage message={error} />}
      <SearchResults results={results} />
    </div>
  );
};

export default HomePage;