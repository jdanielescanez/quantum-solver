import axios from 'axios';

const API_URL = "http://localhost:5000/";


const RunNormalMode = (token: string) => {
  return axios.post(API_URL + "run",{
  } ,{
    headers: {
      'Content-Type': 'application/json',
      token: token
    }
  }
  );
}

const RunExpMode = (token: string, n_shots: number) => {
  return axios.post(API_URL + "run-experimental-mode", {
    n_shots: n_shots
  }, {
    headers: {
      'Content-Type': 'application/json',
      token: token
    }
  }
  );
}

const GetResult = (token: string) => {
  return axios.get(API_URL + "get-output", {headers:{token}});
}

const RunAlgorithmsService = {
  RunExpMode,
  RunNormalMode,
  GetResult
}

export default RunAlgorithmsService;
