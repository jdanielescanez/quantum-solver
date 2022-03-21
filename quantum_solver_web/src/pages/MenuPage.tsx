import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';

const API = process.env.REACT_APP_API;

export function MenuPage() {
  const [state, setState] = useState({'is_algorithm': false, 'are_params': false});
  useEffect(() => { 
    (async () => {
      const result = await fetch(`${API}/are-algorithm-params`, {
        method: 'GET'
      });
      const data = await result.json();
      setState(data);
    })()
  }, []);
  const showParamButton = () => {
    if (state['is_algorithm']) {
      return (
        <Link to='/menu/param'>
          <button type='button'>
            Select Params
          </button>
        </Link>
      );
    }
  }
  const showRunButton = () => {
    if (state['are_params']) {
      return (
        <Link to='/menu/loading'>
          <button type='button'>
            Run QuantumSolver
          </button>
        </Link>
      )
    }
  }
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
      {showParamButton()}
      {showRunButton()}
    </div>
  )
}
