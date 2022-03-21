import React from 'react';
import {Link} from 'react-router-dom';

const API = process.env.REACT_APP_API;

export function HomePage() {
  const resetQExecute = async () => {
    await fetch(`${API}/reset-qexecute`, {
      method: 'POST'
    });
  }
  return (
    <div>
      <h1>QuantumSolver</h1>
      <Link to='/token'>
        <button onClick={resetQExecute}>
          Start!
        </button>
      </Link>
    </div>
  )
}
