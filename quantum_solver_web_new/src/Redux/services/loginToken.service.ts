import axios from 'axios';

const API_URL = "http://localhost:5000/";


const loginToken = (token: string, guest_mode_flag: boolean) => {
  return axios.post(API_URL + 'set-token', {
    token: token,
    guest_mode_flag: guest_mode_flag
  })
}

const logout = (token: string) => {
  return axios.post(API_URL + 'logout', {
    token: token
  })
}

const loginService = {
  loginToken,
  logout,
}

export default loginService;