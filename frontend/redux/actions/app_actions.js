import { SET_ROUTER } from "./type";

export const setRouter = (router) => async (dispatch) => {
    try {
        dispatch({ type: SET_ROUTER, router: router });
    } catch (error) {
        console.warn(err);
    }
};
