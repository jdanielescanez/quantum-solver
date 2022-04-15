import React, {useState, useEffect} from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function LoadingPage() {
  const navigate = useNavigate();
  const [state, setState] = useState({'algorithm': '', 'backend': '', 'params': ''});
  useEffect(() => { 
    (async () => {
      const token = window.sessionStorage.getItem('token') || '';
      const result = await fetch(`${API}/get-backend-algorithm-params`, {
        method: 'GET',
        headers: {token}
    });
      const data = await result.json();
      console.log('Get backend, algorithm and params', data);
      setState(data);
      await fetch(`${API}/run`, {
        method: 'POST',
        headers: {token}
      });
      navigate('/menu/output', {replace: true});
    })();
  }, [navigate]);
  return (
    <div>
      <h1>Loading...</h1>
      <h2>
        Executing "{state['algorithm']}" in "{state['backend']}"
        with parameters: "{state['params']}"
      </h2>
    </div>
  )
}
