import { View, Text, StyleSheet } from "react-native";
import React from "react";

const CustomTextBox = ({ text }) => {
    return (
        <View style={[styles.card, styles.elevation]}>
            <View>
                <Text style={styles.heading}>{text}</Text>
            </View>
        </View>
    );
};

const styles = StyleSheet.create({
    heading: {
        fontSize: 18,
        fontWeight: "600",
        marginBottom: 13,
    },
    card: {
        backgroundColor: "white",
        borderRadius: 8,
        paddingVertical: 20,
        paddingHorizontal: 25,
        width: "100%",
        marginVertical: 10,
    },
    elevation: {
        elevation: 20,
        shadowColor: "grey",
    },
});
export default CustomTextBox;
