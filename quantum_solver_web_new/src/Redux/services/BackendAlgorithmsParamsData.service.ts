import axios from 'axios';

const API_URL = "http://localhost:5000/";


const getBackendAlgorithmParams = (token: string) => {
  return axios.get(API_URL + "get-backend-algorithm-params", { headers: { token } });
}

const getBackends = (token: string) => {
  return axios.get(API_URL + "get-backends", {headers:{token}});
}

const getAlgorithms = (token: string) => {
  return axios.get(API_URL + "get-algorithms", {headers:{token}});
}

const getParams = (token: string) => {
  return axios.get(API_URL + "get-params", {headers:{token}});
}

const setBackend = (token: string, backend: string) => {
  return axios.post(API_URL + "set-backend", {
    token: token,
    name: backend
  });
}

const setAlgorithm = (token: string, algorithm: string) => {
  return axios.post(API_URL + "set-algorithm", {
    token: token,
    name: algorithm
  });
}

const backendService = {
  getBackendAlgorithmParams,
  getBackends,
  getAlgorithms,
  getParams,
  setBackend,
  setAlgorithm
}

export default backendService;