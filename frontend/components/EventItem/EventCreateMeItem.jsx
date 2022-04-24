import { StyleSheet, Text, View, Image } from "react-native";
import React, { memo } from "react";
import { border, color, background } from "../../theme";
export const EventCreateMeItem = memo(({ name, status }) => {
    return (
        <View style={styles.containerWrap}>
            <View style={styles.container}>
                <Image
                    style={styles.image}
                    source={{ uri: "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b6/Image_created_with_a_mobile_phone.png/330px-Image_created_with_a_mobile_phone.png" }}
                />

                <Text style={styles.title}>{name}</Text>
            </View>
            <View style={[styles.status, { backgroundColor: status ? background.active : background.inactive }]}></View>
        </View>
    );
});

const styles = StyleSheet.create({
    containerWrap: {
        padding: 2,
    },
    status: {
        position: "absolute",
        top: 0,
        left: 0,
        width: 20,
        height: 20,
        borderRadius: 50,
        borderWidth: 2,
        zIndex: 99,
    },
    container: {
        borderWidth: 1,
        height: "100%",
        alignItems: "center",
        borderRadius: 10,
        borderColor: border.black,
        flexDirection: "row",
        overflow: "hidden",
    },
    image: {
        resizeMode: "cover",
        width: "30%",
        borderRadius: 10,
        height: "100%",
        marginLeft: -10,
    },
    title: {
        marginLeft: 10,
        fontWeight: "bold",
    },
});
