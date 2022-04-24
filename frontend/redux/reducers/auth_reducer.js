import { LOGIN_SUCCESS, LOGOUT, GET_USER_INFO } from "../actions/type";
const initialState = {
    user: {
        id: "",
        username: "",
        imageUrl: "",
    },
    token: "",
};

export default function (state = initialState, payload) {
    switch (payload.type) {
        case LOGIN_SUCCESS:
            return { ...state, token: payload.token };
        case LOGOUT:
            return { token: null };
        case GET_USER_INFO:
            return { ...state, user: payload.user };
        default:
            return state;
    }
}
