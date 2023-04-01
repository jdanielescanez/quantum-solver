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
} from '../actions/typeActions';

export const default_login_state = {
  algorithmsData: "",
  backendData: "",
  paramsData: "",
  currentBackend: "",
  currentAlgorithm: "",
  currentParams: "",
};

const run_Algorithm_reducer = (state = default_login_state, action: { type: string, payload: any }) => {
  const { type, payload } = action;
  switch (type) {
    case GET_BACKEND_ALGORITHM_PARAMS_SUCCESS:
      return {
        ...state,
        algorithmsData: payload.algorithm,
        backendData: payload.backend,
        paramsData: payload.params,
      };
    case GET_BACKEND_ALGORITHM_PARAMS_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case GET_BACKEND_DATA_SUCCESS:
      return {
        ...state,
        backendData: payload.backends,
        currentBackend: payload.current_backend,
      };
    case GET_ALGORITHM_DATA_SUCCESS:
      return {
        ...state,
        algorithmsData: payload.algorithms,
        currentAlgorithm: payload.current_algorithm,
      };
    case GET_PARAMS_DATA_SUCCESS:
      return {
        ...state,
        paramsData: payload,
      };
    case GET_BACKEND_DATA_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case GET_ALGORITHM_DATA_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case GET_PARAMS_DATA_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case CLEAR_BACKEND_ALGORITHM_PARAMS:
      return {
        ...state,
        algorithmsData: "",
        backendData: "",
        paramsData: "",
      };
    default:
      return state;
  }
}


export default run_Algorithm_reducer;