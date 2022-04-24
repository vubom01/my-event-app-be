import { createStore, applyMiddleware, combineReducers } from "redux";
import thunk from "redux-thunk";
import authReducers from "./reducers";

const middleware = [thunk];
const rootReducer = combineReducers({ authReducers });

export const store = createStore(rootReducer, applyMiddleware(...middleware));
