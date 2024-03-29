import { 
  SET_CURRENT_ALGORITHM_FAILED,
  SET_CURRENT_ALGORITHM_SUCCESS,
  SET_CURRENT_BACKEND_FAILED,
  SET_CURRENT_BACKEND_SUCCESS,
  SET_CURRENT_PARAMS_FAILED,
  SET_CURRENT_PARAMS_SUCCESS,
} from './typeActions';
import backendService from '../services/BackendAlgorithmsParamsData.service';
import { Dispatch } from 'redux';

export const setCurrentBackend = (token:string, backend:string): any => (dispatch: Dispatch): any => {
  return backendService.setBackend(token, backend).then(
    (response) => {
      dispatch({
        type: SET_CURRENT_BACKEND_SUCCESS,
        payload: response.data
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: SET_CURRENT_BACKEND_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}


export const setCurrentAlgorithm = (token:string, algorithm:number): any => (dispatch: Dispatch): any => {
  return backendService.setAlgorithm(token, algorithm).then(
    (response) => {
      dispatch({
        type: SET_CURRENT_ALGORITHM_SUCCESS,
        payload: response.data
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: SET_CURRENT_ALGORITHM_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}

export const setCurrentParams = (token:string, params:any): any => (dispatch: Dispatch): any => {
  return backendService.setParams(token, params).then(
    (response) => {
      dispatch({
        type: SET_CURRENT_PARAMS_SUCCESS,
        payload: response.data
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: SET_CURRENT_PARAMS_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}