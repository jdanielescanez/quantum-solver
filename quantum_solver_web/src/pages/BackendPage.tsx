
import React, {useState} from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

type Backend = {
  'name': string,
  'n_qubits': number,
  'n_shots': number,
  'jobs_in_queue': number
};

export function BackendPage() {
  const navigate = useNavigate();
  let currentBackend = '';
  const [state, setState] = useState({'backends': [], 'current_backend': ''});
  const goToMenu = () => {
    navigate('/menu', { replace: true });
  }
  const getAvailableBackends = async () => {
    const result = await fetch(`${API}/get-backends`, {
      method: 'GET'
    });
    const data = await result.json();
    setState(data);
  }
  if (state['backends'].length === 0) {
    getAvailableBackends();
  }
  const selectBackend = (event: React.ChangeEvent<HTMLSelectElement>) => {
    state['current_backend'] = event.target.value;
  }
  const setBackend = async () => {
    const result = await fetch(`${API}/set-backend`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({'name': state['current_backend']})
    });
    const data = await result.json();
    console.log('setBackend: ', data);
    goToMenu();
  }
  const getOptions = state['backends'].map((item: Backend, i: number) => {
    return <option key={i} value={item.name}>
      {item.name} (qubits: {item.n_qubits}, shots: {item.n_shots}, queue: {item.jobs_in_queue})
    </option>
  });
  return (
    <div>
    <h1>Select Backend</h1>
    <select name='backends' onChange={selectBackend}>
    <option value="" hidden>Choose a backend here</option>
      {getOptions} 
    </select>
    <button onClick={setBackend}>
      OK
    </button>
    </div>
  )
}
