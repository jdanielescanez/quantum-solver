import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';

const API = process.env.REACT_APP_API;

export function MenuPage() {
  const [state, setState] = useState({'backend': 'None', 'algorithm': 'None', 'params': 'None'});
  useEffect(() => { 
    (async () => {
      const result = await fetch(`${API}/get-backend-algorithm-params`, {
        method: 'GET'
      });
      const data = await result.json();
      console.log(data)
      setState(data);
    })()
  }, []);
  const showParamButton = () => {
    if (state['algorithm'] !== 'None') {
      return (
        <Link to='/menu/param'>
          <button type='button'>
            Set Parameters Values
          </button>
        </Link>
      );
    }
  }
  const showRunButton = () => {
    if (state['params'] !== 'None' && state['backend'] !== 'None') {
      return (
        <Link to='/menu/loading'>
          <button type='button'>
            Run QuantumSolver
          </button>
        </Link>
      )
    }
  }
  const variablesString = [
      ((state['backend'] !== 'None') ? 'Current Backend: ' + state['backend'] : ''),
          ((state['algorithm'] !== 'None') ? 'Current Algorithm: ' + state['algorithm'] : ''),
              ((state['params'] !== 'None') ? ' Current Parameters: ' + state['params'] : '')
  ];
  const showVariables = () => {
    return (
      <div>
        <h3>{variablesString[0]}</h3>
        <h3>{variablesString[1]}</h3>
        <h3>{variablesString[2]}</h3>
      </div>
    );
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
      {showVariables()}
    </div>
  )
}
