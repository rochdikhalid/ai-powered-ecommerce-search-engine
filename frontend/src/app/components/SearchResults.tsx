import React from 'react';
import { Card, Text, Group } from '@mantine/core';

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
  const formatPrice = (price: number) => {
    return price.toLocaleString();
  };

  return (
    <div className="p-4 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
      {results.map((car) => (
        <Card
          key={car.id}
          shadow="lg"
          padding="lg"
          radius="md"
          style={{
            backgroundColor: '#2E2E2E',
            color: '#FFFFFF',
          }}
        >
          <Group direction="column" spacing="xs">
            <Text weight={600} size="lg" color="white">
              {car.name}
            </Text>
            <Text weight={700} size="xl" color="yellow">
              ${formatPrice(car.price)}
            </Text>
            <Text style={{ color: '#f0f0f0', marginTop: '8px' }}>
              {car.features}
            </Text>
          </Group>
        </Card>
      ))}
    </div>
  );
};

export default SearchResults;
