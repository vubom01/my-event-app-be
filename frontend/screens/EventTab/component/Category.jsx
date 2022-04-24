import { StyleSheet, Text, View, Image, TouchableOpacity } from "react-native";
import React from "react";
import { checkedCategory, categories } from "../data/image";

import { color, background } from "../../../theme";
export const Category = ({ id, onPress, name, select, image }) => {
    const { container, activeBg, inActiveBg, activeTx, inActiveTx, checked, logo } = styles;
    return (
        <TouchableOpacity style={[container, select === id ? activeBg : inActiveBg]} onPress={() => onPress(id)}>
            <Image style={logo} source={categories[image || "diamond"]} />
            <Text style={select === id ? activeTx : inActiveTx}>{name}</Text>
            {select === id && <Image style={checked} source={checkedCategory} />}
        </TouchableOpacity>
    );
};

const styles = StyleSheet.create({
    container: {
        width: 156,
        height: 130,
        justifyContent: "center",
        alignItems: "center",
        margin: 10,
        borderRadius: 10,
    },
    activeBg: {
        backgroundColor: background.activeCategory,
    },
    inActiveBg: {
        backgroundColor: background.inActiveCategory,
    },
    activeTx: {
        color: color.activeText,
    },
    inActiveTx: {
        color: color.inActiveText,
    },
    checked: {
        position: "absolute",
        top: 0,
        right: 0,
    },
    logo: {
        alignItems: "center",
        marginBottom: 0,
        borderWidth: 10,
    },
});
