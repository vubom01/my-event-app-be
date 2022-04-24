import { ADD_ITEM, REMOVE_ITEM, UPDATE_LIST } from "../actions/type";
const initialState = [];
export default function (state = [], action) {
  switch (action.type) {
    case ADD_ITEM:
      return [...state, action.payload];
    case REMOVE_ITEM:
      return [...state].filter((element) => element.id !== action.payload.id);
    case UPDATE_LIST:
      return action.payload;
    default:
      return state;
  }
}
