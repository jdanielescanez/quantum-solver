import React from 'react';
import {Link} from 'react-router-dom';

export function HomePage() {
  return (
    <div>
      <h1>QuantumSolver</h1>
      <Link to="/token">
        <button type="button">
          Start!
        </button>
      </Link>
    </div>
  )
}
