
import React from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function TokenPage() {
  let navigate = useNavigate();
  let token = '';
  let error_message = '';
  const getToken = (event: React.ChangeEvent<HTMLInputElement>) => {
    token = event.target.value;
  }
  const sendToken = async () => {
    console.log(token);
    const result = await fetch(`${API}/get-token`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({token})
    });
    const data = await result.json();
    console.log('DATA:', data);
    if (data['err']) {
      error_message = data['msg'];
      alert(error_message);
    }
    else {
      goToMenu();
    }
  }
  const goToMenu = () => {
    navigate('/menu', { replace: true });
  }
  const checkAndSend = async () => {
    token = token != '' ? token : 'empty_string_token';
    sendToken();
  }
  const guestMode = async () => {
    token = '';
    sendToken();
  }
  return (
    <div>
      <h1>QuantumSolver</h1>
      <p>Write your IBMQ token: </p>
      <input type='text' onChange={getToken} placeholder='IBMQ token'/>
      <button onClick={checkAndSend}>OK</button>
      <p>Or</p>
      <button onClick={guestMode}>Use Guest Mode</button>
    </div>
  )
}
