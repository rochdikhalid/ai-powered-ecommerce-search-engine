import React, { useState } from 'react';


interface SearchInputProps {
    onSearch: (query: string) => void;
}

const SearchInput: React.FC<SearchInputProps> = ({ onSearch }) => {
    const [query, setQuery] = useState('');
  
    const handleSearch = () => {
      if (query.trim()) {
        onSearch(query);
      }
    };
  
    return (
      <div className="flex items-center justify-center p-4">
        <input
          type="text"
          className="border border-gray-300 rounded-lg p-2 w-2/3"
          placeholder="Search for cars (e.g., manual cars under $30,000)"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
        />
        <button
          className="ml-4 bg-blue-500 text-white px-4 py-2 rounded-lg"
          onClick={handleSearch}
        >
          Search
        </button>
      </div>
    );
  };
  
  export default SearchInput;
