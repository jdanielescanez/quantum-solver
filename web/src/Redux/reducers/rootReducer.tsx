import { combineReducers } from "redux";

import login_reducer from './loginReducer'
import getAlgorithms_reducer from './getAlgorithmData'
import drawer_reducer from "./drawerReducer";
import runAlgorithms_reducer from "./runAlgorithmReducer";

const rootReducers = combineReducers({
  login_reducer,
  getAlgorithms_reducer,
  drawer_reducer,
  runAlgorithms_reducer,
});


export default rootReducers;