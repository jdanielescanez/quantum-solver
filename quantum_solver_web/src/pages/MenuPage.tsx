import React, {useState, useEffect} from 'react';
import {Link} from 'react-router-dom';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function MenuPage() {
  const navigate = useNavigate();
  const [state, setState] = useState({'backend': 'None', 'algorithm': 'None', 'params': 'None'});
  const goToHome = () => {
    navigate('/', {replace: true});
  }
  useEffect(() => { 
    (async () => {
      const result = await fetch(`${API}/get-backend-algorithm-params`, {
        method: 'GET'
      });
      const data = await result.json();
      console.log('Get backend, algorithm and params', data);
      setState(data);
    })();
  }, []);
  const showParamButton = () => {
    if (state['algorithm'] !== 'None') {
      return (
        <Link to='/menu/param'>
          <button className='button' type='button'>
            <span>Set Parameters Values</span>
          </button>
        </Link>
      );
    }
  }
  const showRunButton = () => {
    if (state['params'] !== 'None' && state['backend'] !== 'None') {
      return (
        <Link to='/menu/loading'>
          <button className='button' type='button'>
            <span>Run QuantumSolver</span>
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
      <h1>QuantumSolver</h1>
      <Link to='/menu/backend'>
        <button className='button' type='button'>
          <span>Select Backend</span>
        </button>
      </Link>
      <Link to='/menu/algorithm'>
        <button className='button' type='button'>
          <span>Select Algorithm</span>
        </button>
      </Link>
      {showParamButton()}
      {showRunButton()}
      {showVariables()}
      <button className='button' id='backBtn' onClick={goToHome}>
        <span>Back</span>
      </button>
    </div>
  )
}
