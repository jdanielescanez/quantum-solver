import axios from 'axios';

const API_URL = import.meta.env.VITE_APP_API;


const loginToken = (token: string, guest_mode_flag: boolean) => {
  console.log("loginToken service", API_URL)
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