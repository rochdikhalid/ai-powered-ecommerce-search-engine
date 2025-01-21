'use client';

import React, { useState } from 'react';
import SearchInput from '@/app/components/SearchInput';
import SearchResults from '@/app/components/SearchResults';
import LoadingIndicator from '@/app/components/LoadingIndicator';
import ErrorMessage from '@/app/components/ErrorMessage';

export default function HomePage() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSearch = async (query: string) => {
    setLoading(true);
    setError('');
    setResults([]);

    try {
      const response = await fetch('/api/search', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query }),
      });

      if (response.ok) {
        const data = await response.json();
        setResults(data.results);
      } else {
        throw new Error('Failed to fetch results.');
      }
    } catch (err) {
      if (err instanceof Error) {
        console.error(err.message);
      } else {
        console.error('An unknown error occurred:', err);
      }
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