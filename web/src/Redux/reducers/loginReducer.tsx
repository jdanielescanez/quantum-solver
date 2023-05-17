// type actions import 
import {
  LOGIN_SUCCESS,
  LOGIN_FAILED,
  LOGOUT_SUCCESS,
  LOGOUT_FAILED,
} from '../actions/typeActions';

export const default_login_state = {
  guest: false,
  isToken: false,
  flagError: "none",
  token: "",
};

const login_reducer = (state = default_login_state, action: { type: string, mode: boolean, payload: { msg: string } }) => {
  switch (action.type) {
    case LOGIN_SUCCESS:
      state = {
        ...state,
        guest: action.mode,
        isToken: true,
        flagError: "none",
        token: action.payload.msg,
      };
      break;
    case LOGIN_FAILED:
      state = {
        ...state,
        guest: action.mode,
        isToken: false,
        flagError: "error",
        token: "",
      };
      break;
    case LOGOUT_SUCCESS:
      state = {
        ...state,
        guest: true,
        isToken: false,
        flagError: "none",
        token: "",
      };
      break;
    case LOGOUT_FAILED:
      state = {
        ...state,
        guest: true,
        isToken: false,
        flagError: "none",
        token: "",
      };
      break;
  }
  return state;
}

export default login_reducer;