import { View, Text, StyleSheet, Pressable } from "react-native";
import React from "react";
import { Icon } from "react-native-elements";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import CommonStyle, { BORDER_COLOR } from "../common/CommonStyle";
import { color, background } from "../../theme";

const EventPostBtn = ({ title, iconName, bgColor, text, onPress }) => {
    return (
        <View style={[styles.btnContainer, { backgroundColor: bgColor || "white" }]}>
            <View style={styles.selected}>
                <Text style={styles.text}>{title}</Text>
                <MaterialCommunityIcons size={30} style={[styles.icon]} name={iconName} color="black" />
            </View>
            <Pressable style={styles.option} onPress={onPress}>
                <Text style={styles.title}>{text}</Text>
            </Pressable>
        </View>
    );
};

export default EventPostBtn;

const styles = StyleSheet.create({
    title: {
        fontSize: 16,
        fontWeight: "bold",
        marginLeft: 5,
        color: color.white,
    },
    btnContainer: {
        flexDirection: "row",
        alignItems: "center",
        width: "100%",
        height: 60,
        marginTop: 20,
        borderRadius: 10,
        overflow: "hidden",
        borderWidth: 2,
        borderColor: background.gray,
    },
    selected: {
        flex: 2,
        paddingHorizontal: 10,
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "space-between",
    },
    text: {
        color: color.blackText,
        fontWeight: "700",
    },
    option: {
        flex: 5,
        justifyContent: "center",
        backgroundColor: background.gray,
        height: "100%",
        borderRadius: 8,
        padding: 5,
        borderWidth: 2,
        borderColor: color.activeText,
        paddingHorizontal: 10,
    },
    icon: {
        paddingHorizontal: 10,
        position: "absolute",
        right: 0,
    },
});
