import { 
  GET_BACKEND_ALGORITHM_PARAMS_SUCCESS, 
  GET_BACKEND_ALGORITHM_PARAMS_FAILED,
  GET_BACKEND_DATA_SUCCESS,
  GET_ALGORITHM_DATA_SUCCESS,
  GET_PARAMS_DATA_SUCCESS,
  GET_BACKEND_DATA_FAILED,
  GET_ALGORITHM_DATA_FAILED,
  GET_PARAMS_DATA_FAILED,
  CLEAR_BACKEND_ALGORITHM_PARAMS
} from './typeActions';
import backendService from '../services/BackendAlgorithmsParamsData.service';
import { Dispatch } from 'redux';

export const getBackendAlgorithmsParams = (token:string): any => (dispatch: Dispatch): any => {
  return backendService.getBackendAlgorithmParams(token).then(
    (response) => {
      console.log("getBackendAlgorithmsParams: ")
      console.log(response.data);
      dispatch({
        type: GET_BACKEND_ALGORITHM_PARAMS_SUCCESS,
        payload: response.data
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: GET_BACKEND_ALGORITHM_PARAMS_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}

export const getBackendData = (token:string): any => (dispatch: Dispatch): any => {
  return backendService.getBackends(token).then(
    (response) => {
      console.log("getBackendData: ")
      console.log(response.data);
      dispatch({
        type: GET_BACKEND_DATA_SUCCESS,
        payload: response.data
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: GET_BACKEND_DATA_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}

export const getAlgorithmData = (token:string): any => (dispatch: Dispatch): any => {
  return backendService.getAlgorithms(token).then(
    (response) => {
      console.log("getAlgorithmData: ")
      console.log(response.data);
      dispatch({
        type: GET_ALGORITHM_DATA_SUCCESS,
        payload: response.data
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: GET_ALGORITHM_DATA_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}

export const getParamsData = (token:string): any => (dispatch: Dispatch): any => {
  return backendService.getParams(token).then(
    (response) => {
      console.log("getParamsData: ")
      console.log(response.data);
      dispatch({
        type: GET_PARAMS_DATA_SUCCESS,
        payload: response.data
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: GET_PARAMS_DATA_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}

export const clearBackendAlgorithmsParams = (): any => (dispatch: Dispatch): any => {
  dispatch({
    type: CLEAR_BACKEND_ALGORITHM_PARAMS,
    payload: ""
  });
  return Promise.resolve();
}