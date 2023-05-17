import { GET_ALGORITHMS_SUCCESS, GET_ALGORITHMS_FAILED, CLEAR_ALGORITHMS } from '../actions/typeActions';

export const default_login_state = {
  algorithmData: "",
};

const getAlgorithms_reducer = (state = default_login_state, action: { type: string, payload: any }) => {
  const { type, payload } = action;
  switch (type) {
    case GET_ALGORITHMS_SUCCESS:
      return {
        ...state,
        algorithmData: payload.algorithms,
      };
    case GET_ALGORITHMS_FAILED:
      return {
        ...state,
        error: payload.result,
      };
    case CLEAR_ALGORITHMS:
      return {
        ...state,
        algorithmData: "",
      };
    default:
      return state;
  }
}

export default getAlgorithms_reducer;