import React, {useState, useEffect} from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function LoadingExperimentPage() {
  const navigate = useNavigate();
  const [state, setState] = useState({'algorithm': '', 'backend': '', 'params': '', 'n_shots': ''});
  useEffect(() => { 
    (async () => {
      const n_shots = Number(prompt('[&] Number of repetitions: ', '1000'));
      if (n_shots <= 0) {
        alert('Number of repetitions must be positive, try again');
        navigate('/menu', {replace: true});
      }
      const token = window.sessionStorage.getItem('token') || '';
      const result = await fetch(`${API}/get-backend-algorithm-params`, {
        method: 'GET',
        headers: {token}
      });
      const data = await result.json();
      console.log('Get backend, algorithm and params', data);
      data['n_shots'] = n_shots;
      setState(data);
      await fetch(`${API}/run-experimental-mode`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json', token},
        body: JSON.stringify({'n_shots': n_shots})
      });
      navigate('/menu/output', {replace: true});
    })();
  }, [navigate]);
  return (
    <div>
      <h1>Loading...</h1>
      <h2>
        Executing {state['n_shots']} times "{state['algorithm']}"
        in "{state['backend']}" with parameters: "{state['params']}"
      </h2>
    </div>
  )
}
