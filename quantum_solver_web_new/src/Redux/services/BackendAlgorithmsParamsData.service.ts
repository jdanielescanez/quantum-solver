import axios from 'axios';

const API_URL = "http://localhost:5000/";


const getBackendAlgorithmParams = (token: string) => {
  return axios.get(API_URL + "get-backend-algorithm-params", { headers: { token } });
}

const getBackends = (token: string) => {
  return axios.get(API_URL + "get-backends", { headers: { token } });
}

const getAlgorithms = (token: string) => {
  return axios.get(API_URL + "get-algorithms", { headers: { token } });
}

const getParams = (token: string) => {
  return axios.get(API_URL + "get-params", { headers: { token } });
}

const setBackend = (token: string, backend: string) => {
  return axios.post(API_URL + "set-backend",{
    name: backend
  }, {
    headers: {
      'Content-Type': 'application/json',
      token: token
    }
  });
}

const setAlgorithm = (token: string, algorithm: number) => {
  return axios.post(API_URL + "set-algorithm", {
    id: algorithm
  }, {
    headers: {
      'Content-Type': 'application/json',
      token: token
    }
  }
  );
}

const setParams = (token: string, params_values: any) => {
  return axios.post(API_URL + "set-params-values", {
    params_values: params_values
  }, {
    headers: {
      'Content-Type': 'application/json',
      token: token
    }
  }
  );
}

const backendService = {
  getBackendAlgorithmParams,
  getBackends,
  getAlgorithms,
  getParams,
  setBackend,
  setParams,
  setAlgorithm
}

export default backendService;