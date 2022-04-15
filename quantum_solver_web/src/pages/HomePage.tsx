import React from 'react';
import {Link} from 'react-router-dom';
import quantumSolverImage from '../images/QuantumSolver_icon.png';

export function HomePage() {
  return (
    <div>
      <img id='iconImg' src={quantumSolverImage} alt='QuantumSolver icon'></img>
      <h1>QuantumSolver</h1>
      <Link to='/token'>
        <button className='button' id='startBtn'>
          <span>Start!</span>
        </button>
      </Link>
    </div>
  )
}
