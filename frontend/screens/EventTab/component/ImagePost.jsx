import { StyleSheet, Text, View, Dimensions, Image, TouchableOpacity } from "react-native";
import React from "react";
import { Icon } from "react-native-elements";
import { color } from "../../../theme";

const windowWidth = Dimensions.get("window").width;
export const ImagePost = ({ uri, onPressDelete, index }) => {
    return (
        <View style={styles.container}>
            <Image source={{ uri: uri }} style={styles.images} />
            <TouchableOpacity style={styles.icon} onPress={() => onPressDelete(index)}>
                <Icon name="close" type="font-awesome" color={color.red} />
            </TouchableOpacity>
        </View>
    );
};

const styles = StyleSheet.create({
    images: {
        width: windowWidth - 20,
        height: windowWidth / 2,
        borderRadius: 10,
    },
    container: {
        margin: 5,
    },
    icon: {
        position: "absolute",
        right: 5,
        top: 0,
        zIndex: 100000,
    },
});
