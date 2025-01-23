import React from 'react';
import { Loader } from '@mantine/core';

const LoadingIndicator: React.FC = () => {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', padding: '16px' }}>
      <Loader size="lg" color="blue" />
    </div>
  );
};

export default LoadingIndicator;
