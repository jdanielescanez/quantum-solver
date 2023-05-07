import { OPEN_DRAWER, CLOSE_DRAWER } from './typeActions';

const setDrawer = (open: boolean):any => (dispatch: any):any => {
  if (open) {
    dispatch({
      type: OPEN_DRAWER,
      payload: open,
    });
  } else {
    dispatch({
      type: CLOSE_DRAWER,
      payload: open,
    });
  }
}

export default setDrawer;