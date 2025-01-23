import React, { useState } from 'react';
import { TextInput, Button, Group } from '@mantine/core';

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
    <Group position="center" spacing="sm" mt="lg">
      <TextInput
        placeholder="Search for a car"
        value={query}
        onChange={(e) => setQuery(e.currentTarget.value)}
        size="md"
        style={{ flex: 1, maxWidth: 600 }}
      />
      <Button onClick={handleSearch} size="md">
        Search
      </Button>
    </Group>
  );
};

export default SearchInput;
