import React from 'react';
import { Card, Text } from '@mantine/core';

interface Car {
  id: number;
  name: string;
  price: number;
  features: string;
}

interface SearchResultsProps {
  results: Car[];
}

const SearchResults: React.FC<SearchResultsProps> = ({ results }) => {
  return (
    <div className="p-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      {results.map((car) => (
        <Card key={car.id} shadow="sm" padding="lg" className="w-full">
          <Text weight={500} size="lg">
            {car.name}
          </Text>
          <Text>Price: ${car.price}</Text>
          <Text>{car.features}</Text>
        </Card>
      ))}
    </div>
  );
};

export default SearchResults;
