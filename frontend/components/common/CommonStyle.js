import { StyleSheet } from "react-native";

export default StyleSheet.create({
    spaceBetween: {
        flexDirection: "row",
        justifyContent: "space-between",
    },
    flexCenter: {
        flexDirection: "row",
        justifyContent: "center",
        alignItems: "center",
    },
});

const BORDER_COLOR = "rgba(0, 0, 0, 0.2)";
const MAIN_COLOR = "rgba(75,119,190,1)";
const SECOND_COLOR = "rgba(173, 216, 230,1)";

export { BORDER_COLOR, MAIN_COLOR, SECOND_COLOR };
