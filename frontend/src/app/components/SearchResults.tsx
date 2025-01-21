import React from 'react';


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
    <div className="p-4">
      {results.length > 0 ? (
        <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
          {results.map((car) => (
            <li key={car.id} className="border p-4 rounded-lg">
              <h3 className="text-lg font-bold">{car.name}</h3>
              <p>Price: ${car.price}</p>
              <p>Features: {car.features}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p className="text-center text-gray-500">No results found.</p>
      )}
    </div>
  );
};

export default SearchResults;