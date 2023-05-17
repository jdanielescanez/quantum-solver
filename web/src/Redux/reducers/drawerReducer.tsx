import { OPEN_DRAWER, CLOSE_DRAWER } from '../actions/typeActions';

const default_drawer_state = {
  open: false,
};

const drawer_reducer = (state = default_drawer_state, action: { type: string, payload: any }) => {
  const { type, payload } = action;
  switch (type) {
    case OPEN_DRAWER:
      return {
        ...state,
        open: payload,
      };
    case CLOSE_DRAWER:
      return {
        ...state,
        open: payload,
      };
    default:
      return state;
  }
}

export default drawer_reducer;