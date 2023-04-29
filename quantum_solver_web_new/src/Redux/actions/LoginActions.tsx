import {
  LOGIN_SUCCESS,
  LOGIN_FAILED,
  LOGOUT_FAILED,
  LOGOUT_SUCCESS
} from './typeActions';
import loginService from '../services/loginToken.service';
import { Dispatch } from 'redux';

export const login = (token: string, guest_mode_flag: boolean): any => (dispatch: Dispatch): any => {
  return loginService.loginToken(token, guest_mode_flag).then(
    (response) => {
      if (response.data.err) {
        dispatch({
          type: LOGIN_FAILED,
          mode: guest_mode_flag,
          payload: response.data
        });
        return Promise.reject();
      } else {
        dispatch({
          type: LOGIN_SUCCESS,
          mode: guest_mode_flag,
          payload: response.data
        });
        return Promise.resolve();
      }
    }, (error) => {
      dispatch({
        type: LOGIN_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}

export const logout = (token: string): any => (dispatch: Dispatch): any => {
  return loginService.logout(token).then(
    (response) => {
      if (response.data.err) {
        dispatch({
          type: LOGOUT_FAILED,
          payload: response.data
        });
        return Promise.reject();
      } else {
        dispatch({
          type: LOGOUT_SUCCESS,
          payload: response.data
        });
        return Promise.resolve();
      }
    }, (error) => {
      dispatch({
        type: LOGOUT_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}