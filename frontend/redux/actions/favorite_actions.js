import { ADD_ITEM, REMOVE_ITEM, UPDATE_LIST } from "./type"
export const addItem = (item) => {
    return {
        type: ADD_ITEM, payload: item
    }
}

export const removeItem = (item) => {
    return { type: REMOVE_ITEM, payload: item }
}

export const updateList = (list) => {
    return { type: UPDATE_LIST, payload: list }
}
