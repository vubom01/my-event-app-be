import { SET_ROUTER } from "../actions/type";
const initialState = {
    router: "",
};

export default function (state = initialState, payload) {
    switch (payload.type) {
        case SET_ROUTER:
            return { ...state, router: payload.router };
        default:
            return state;
    }
}
