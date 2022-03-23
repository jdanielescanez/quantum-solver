import React from 'react';
import {Link} from 'react-router-dom';
import quantumSolverImage from '../images/QuantumSolver_icon.png';

const API = process.env.REACT_APP_API;

export function HomePage() {
  const resetQExecute = async () => {
    await fetch(`${API}/reset-qexecute`, {
      method: 'POST'
    });
  }
  return (
    <div>
      <img id='iconImg' src={quantumSolverImage} alt='QuantumSolver icon'></img>
      <h1>QuantumSolver</h1>
      <Link to='/token'>
        <button className='button' id='startBtn' onClick={resetQExecute}>
          <span>Start!</span>
        </button>
      </Link>
    </div>
  )
}
