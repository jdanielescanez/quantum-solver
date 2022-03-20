import React from 'react';
import {Link} from 'react-router-dom';

export function MenuPage() {
  return (
    <div>
      <h1>Main Menu</h1>
      <Link to='/menu/backend'>
        <button type='button'>
          Select Backend
        </button>
      </Link>
      <Link to='/menu/algorithm'>
        <button type='button'>
          Select Algorithm
        </button>
      </Link>
      <Link to='/menu/params'>
        <button type='button'>
          Select Params
        </button>
      </Link>
      <Link to='/menu/loading'>
        <button type='button'>
          Run QuantumSolver
        </button>
      </Link>
    </div>
  )
}
