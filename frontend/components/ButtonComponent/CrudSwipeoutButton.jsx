import { StyleSheet, Text, View, TouchableOpacity } from "react-native";
import React from "react";
import { Icon } from "react-native-elements";
import { background } from "../../theme";
const CrudSwipeoutButton = ({ onPress, icon = "edit", type }) => {
    return (
        <View style={[styles.center, styles[type]]}>
            <TouchableOpacity onPress={onPress} style={styles.swipeBtn}>
                <Icon name={icon} type="font-awesome" color="white" />
            </TouchableOpacity>
        </View>
    );
};

export default CrudSwipeoutButton;

const styles = StyleSheet.create({
    center: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        borderRadius: 10,
        overflow: "hidden",
    },
    delete: {
        marginHorizontal: 2,
        backgroundColor: background.brown,
    },
    edit: {
        marginHorizontal: 2,
        backgroundColor: background.gray,
    },
    swipeBtn: {
        width: "100%",
        height: "100%",
        alignItems: "center",
        justifyContent: "center",
    },
});
