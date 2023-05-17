import {
  GET_BACKEND_ALGORITHM_PARAMS_SUCCESS,
  GET_BACKEND_ALGORITHM_PARAMS_FAILED,
  GET_BACKEND_DATA_SUCCESS,
  GET_ALGORITHM_DATA_SUCCESS,
  GET_PARAMS_DATA_SUCCESS,
  GET_BACKEND_DATA_FAILED,
  GET_ALGORITHM_DATA_FAILED,
  GET_PARAMS_DATA_FAILED,
  SET_CURRENT_BACKEND_SUCCESS,
  SET_CURRENT_BACKEND_FAILED,
  SET_CURRENT_ALGORITHM_SUCCESS,
  SET_CURRENT_ALGORITHM_FAILED,
  SET_CURRENT_PARAMS_SUCCESS,
  SET_CURRENT_PARAMS_FAILED,
  CLEAR_BACKEND_ALGORITHM_PARAMS,
  RUN_NORMAL_MODE_SUCCESS,
  RUN_NORMAL_MODE_FAILED,
  RUN_MODE,
  RUN_EXPERIMENTAL_MODE_SUCCESS,
  RUN_EXPERIMENTAL_MODE_FAILED,
  GET_RESULT_SUCCESS,
  GET_RESULT_FAILED,
  CLEAR_PARAMS_RESULT,
  SET_N_SHOTS
} from '../actions/typeActions';

export const default_login_state = {
  algorithmsData: "",
  backendData: "",
  paramsData: "",
  currentBackend: "",
  currentAlgorithm: "",
  currentParams: "",
  RunMode: "None",
  n_shots: "",
  RunAlgorithmData: "",
  result: ""
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
        currentBackend: "",
      };
    case GET_ALGORITHM_DATA_SUCCESS:
      return {
        ...state,
        algorithmsData: payload.algorithms,
        currentAlgorithm: "",
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
        paramsData: "None",
        currentBackend: "",
        currentAlgorithm: "",
        currentParams: "None",
        RunMode: "None",
        n_shots:"",
        RunAlgorithmData: "",
        result: ""
      };
    case SET_CURRENT_BACKEND_SUCCESS:
      return {
        ...state,
        currentBackend: payload,
      };
    case SET_CURRENT_BACKEND_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case SET_CURRENT_ALGORITHM_SUCCESS:
      return {
        ...state,
        currentAlgorithm: payload,
      };
    case SET_CURRENT_ALGORITHM_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case SET_CURRENT_PARAMS_SUCCESS:
      return {
        ...state,
        currentParams: payload,
      };
    case SET_CURRENT_PARAMS_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case RUN_MODE:
      return {
        ...state,
        RunMode: payload,
      };
    case RUN_NORMAL_MODE_SUCCESS:
      return {
        ...state,
        RunAlgorithmData: payload,
      };
    case RUN_NORMAL_MODE_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case RUN_EXPERIMENTAL_MODE_SUCCESS:
      return {
        ...state,
        RunAlgorithmData: payload,
      };
    case RUN_EXPERIMENTAL_MODE_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case GET_RESULT_SUCCESS:
      return {
        ...state,
        result: payload,
      };
    case GET_RESULT_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case CLEAR_PARAMS_RESULT:
      return {
        ...state,
        currentParams: "",
        RunMode: "None",
        RunAlgorithmData: "",
        n_shots:"",
        result: ""
      };
    case SET_N_SHOTS:
      return {
        ...state,
        n_shots: payload,
      };
    default:
      return state;
  }
}


export default run_Algorithm_reducer;