// mobile/__tests__/App.test.tsx
import React from 'react';
import { render } from '@testing-library/react-native';
import App from '../App';

describe('App', () => {
  it('renders without crashing', () => {
    const { getByText } = render(<App />);
    // Adjust to match something visible in your App component
    expect(getByText(/Welcome/i)).toBeTruthy();
  });
});
