import { GET_ALGORITHMS_SUCCESS, GET_ALGORITHMS_FAILED, CLEAR_ALGORITHMS} from './typeActions';
import algorithmService from '../services/AlgorithmData.service';
import { Dispatch } from 'redux';

export const   getAlgorithms = (token: string): any => (dispatch: Dispatch): any => {
  return algorithmService.getAlgorithmsData(token).then(
    (response) => {
      dispatch({
        type: GET_ALGORITHMS_SUCCESS,
        payload: response.data
      });
      return Promise.resolve();
    }, (error) => {
      dispatch({
        type: GET_ALGORITHMS_FAILED,
        payload: error
      });
      return Promise.reject();
    }
  );
}

export const clearAlgorithms = (): any => (dispatch: Dispatch): any => {
  dispatch({
    type: CLEAR_ALGORITHMS,
    payload: ""
  });
}