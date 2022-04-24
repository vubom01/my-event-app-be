import { ADD_EVENT, EDIT_EVENT, DELETE_EVENT } from "../actions/type";

// [
//     {
//         topic: "",
//         event_name: "",
//         start_at: "",
//         end_at: "",
//         description: "",
//         status: 0,
//         lat: 120,
//         long: 120,
//         images: [],
//         location_name: "",
//     },
// ];

export default function (state = [], payload) {
    switch (payload.type) {
        case ADD_EVENT:
            return [...state, payload.events];
        case EDIT_EVENT:
            return state.map((event) => {
                if (event.id === payload.event.id) {
                    return payload.event;
                } else {
                    return event;
                }
            });
        case DELETE_EVENT: {
            const { id } = payload;
            let newEventList = state.filter((event) => event.id !== id);
            return [...newEventList];
        }
        default:
            return state;
    }
}
