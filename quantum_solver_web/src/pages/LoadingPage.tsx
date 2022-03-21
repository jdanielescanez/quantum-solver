import React, {useState, useEffect} from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function LoadingPage() {
  const navigate = useNavigate();
  const [state, setState] = useState({'algorithm': '', 'backend': '', 'params': ''});
  const goToOutput = () => {
    navigate('/menu/output', {replace: true});
  }
  useEffect(() => { 
    (async () => {
      const result = await fetch(`${API}/get-backend-algorithm-params`, {
        method: 'GET'
      });
      const data = await result.json();
      console.log(data)
      setState(data);
      await fetch(`${API}/run`, {
        method: 'POST'
      });
      goToOutput();
    })();
  }, []);
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
