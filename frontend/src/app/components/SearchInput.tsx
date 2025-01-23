import React, { useState } from 'react';
import { TextInput, Button } from '@mantine/core';

interface SearchInputProps {
  onSearch: (query: string) => void;
}

const SearchInput: React.FC<SearchInputProps> = ({ onSearch }) => {
  const [query, setQuery] = useState('');

  const handleSearch = () => {
    if (query.trim()) onSearch(query);
  };

  return (
    <div className="p-4">
      <TextInput
        placeholder="Search for cars (e.g., manual cars under $30,000)"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        className="w-full sm:w-2/3"
      />
      <Button onClick={handleSearch} className="mt-2">
        Search
      </Button>
    </div>
  );
};

export default SearchInput;
