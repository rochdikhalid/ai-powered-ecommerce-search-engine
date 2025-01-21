import React from 'react';


const LoadingIndicator: React.FC = () => {
  return (
    <div className="flex items-center justify-center p-4">
      <div className="loader border-t-4 border-blue-500 rounded-full w-6 h-6 animate-spin"></div>
    </div>
  );
};

export default LoadingIndicator;