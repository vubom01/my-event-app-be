import { StyleSheet, Text, View, Switch } from "react-native";
import React from "react";

const CustomSwitch = ({ isEnabled, toggleSwitch }) => {
    return (
        <View style={styles.container}>
            <Switch
                style={styles.switch}
                trackColor={{ false: "#767577", true: "#81b0ff" }}
                thumbColor={isEnabled ? "#f5dd4b" : "#f4f3f4"}
                ios_backgroundColor="#3e3e3e"
                onValueChange={toggleSwitch}
                value={isEnabled}
            />
            <Text style={styles.txt}>{isEnabled ? "ON" : "OFF"}</Text>
        </View>
    );
};

export default CustomSwitch;

const styles = StyleSheet.create({
    switch: {
        borderWidth: 1,
        padding: 0,
        margin: 0,
    },
    container: {
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        padding: 0,
    },
    txt: {
        marginTop: -18,
        fontWeight: "bold",
    },
});
