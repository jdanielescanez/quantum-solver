import axios from 'axios';

const API_URL = import.meta.env.VITE_APP_API;


const getAlgorithmsData = (token: string) => {
  return axios.get(API_URL + "get-algorithms", { headers: { token } });
}

const algorithmService = {
  getAlgorithmsData
}

export default algorithmService;