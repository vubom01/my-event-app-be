import { ADD_EVENT, DELETE_EVENT, EDIT_EVENT } from "./type";

const idGenerator = () => {
    let id = 0;
    const increase = () => {
        id++;
    };
    const getId = () => id;
    return { getId, increase };
};
const id = idGenerator();

export const addEvent = (event) => async (dispatch) => {
    try {
        id.increase();
        event.id = id.getId();
        dispatch({ type: ADD_EVENT, events: event });
    } catch (error) {
        console.warn(err);
    }
};

export const editEvent = (event) => async (dispatch) => {
    try {
        dispatch({ type: EDIT_EVENT, event: event });
    } catch (error) {
        console.log(error);
    }
};

export const deleteEvent = (id) => async (dispatch) => {
    try {
        dispatch({ type: DELETE_EVENT, id: id });
    } catch (error) {
        console.log(error);
    }
};
