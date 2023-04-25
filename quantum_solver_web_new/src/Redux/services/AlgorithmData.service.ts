import axios from 'axios';

const API_URL = "http://localhost:5000/";


const getAlgorithmsData = (token: string) => {
  return axios.get(API_URL + "get-algorithms", { headers: { token } });
}

const algorithmService = {
  getAlgorithmsData
}

export default algorithmService;