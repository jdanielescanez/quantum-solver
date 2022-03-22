
import React from 'react';
import {useNavigate} from "react-router-dom";

const API = process.env.REACT_APP_API;

export function TokenPage() {
  const navigate = useNavigate();
  let token = '';
  const getToken = (event: React.ChangeEvent<HTMLInputElement>) => {
    token = event.target.value;
  }
  const sendToken = async () => {
    console.log(token);
    const result = await fetch(`${API}/set-token`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({token})
    });
    const data = await result.json();
    console.log('sendToken:', data);
    if (data['err']) {
      alert(data['msg']);
    }
    else {
      goToMenu();
    }
  }
  const goToMenu = () => {
    navigate('/menu', {replace: true});
  }
  const checkAndSend = async () => {
    token = token !== '' ? token : 'empty_string_token';
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
      <button className='button' id='okBtn' onClick={checkAndSend}>
        <span>OK</span>
      </button>
      <p>Or</p>
      <button className='button' onClick={guestMode}>
        <span>Use Guest Mode</span>
      </button>
    </div>
  )
}
