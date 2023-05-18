import {
  RUN_MODE,
  RUN_NORMAL_MODE_SUCCESS,
  RUN_NORMAL_MODE_FAILED,
  RUN_EXPERIMENTAL_MODE_SUCCESS,
  RUN_EXPERIMENTAL_MODE_FAILED,
  GET_RESULT_SUCCESS,
  GET_RESULT_FAILED,
  CLEAR_PARAMS_RESULT,
  SET_N_SHOTS
} from './typeActions';
import RunAlgorithmsService from '../services/runAlgorithm.service';
import { Dispatch } from 'redux';


export const setRunMode = (mode: string): any => (dispatch: Dispatch): any => {
  dispatch({
    type: RUN_MODE,
    payload: mode,
  })
  return Promise.resolve();
}

export const runNormalMode = (token: string): any => (dispatch: Dispatch): any => {
  return RunAlgorithmsService.RunNormalMode(token).then(
    (response) => {
      dispatch({
        type: RUN_NORMAL_MODE_SUCCESS,
        payload: response.data,
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: RUN_NORMAL_MODE_FAILED,
        payload: error,
      });
      return Promise.reject();
    }
  );
}

export const runExperimentalMode = (token: string, n_shots: number): any => (dispatch: Dispatch): any => {
  return RunAlgorithmsService.RunExpMode(token, n_shots).then(
    (response) => {
      dispatch({
        type: RUN_EXPERIMENTAL_MODE_SUCCESS,
        payload: response.data,
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: RUN_EXPERIMENTAL_MODE_FAILED,
        payload: error,
      });
      return Promise.reject();
    }
  );
}

export const getResult = (token: string): any => (dispatch: Dispatch): any =>  {
  return RunAlgorithmsService.GetResult(token).then(
    (response) => {
      dispatch({
        type: GET_RESULT_SUCCESS,
        payload: response.data,
      });
      return Promise.resolve();
    },
    (error) => {
      dispatch({
        type: GET_RESULT_FAILED,
        payload: error,
      });
      return Promise.reject();
    }
  );
}

export const clearExecutionData = (): any => (dispatch: Dispatch): any => {
  dispatch({
    type: CLEAR_PARAMS_RESULT,
    payload: ""
  });
  return Promise.resolve();
}

export const setNShots = (n_shots: number): any => (dispatch: Dispatch): any => {
  dispatch({
    type: SET_N_SHOTS,
    payload: n_shots,
  })
  return Promise.resolve();
}