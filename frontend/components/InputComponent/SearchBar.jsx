import { View, Text, TextInput, StyleSheet, TouchableOpacity } from "react-native";
import React from "react";
import { Icon } from "react-native-elements";

const SearchBar = ({ value, setValue, onPress, setToggleNav, ...props }) => {
    const onFocus = () => {
        setToggleNav(true);
    };
    const onBlur = () => {
        setToggleNav(false);
    };
    return (
        <View style={styles.container}>
            <TextInput {...props} style={styles.input} onChangeText={setValue} value={value} onFocus={onFocus} onBlur={onBlur} />
            <TouchableOpacity onPress={onPress}>
                <Icon name="search" style={styles.icon} type="font-awesome"></Icon>
            </TouchableOpacity>
        </View>
    );
};

export default SearchBar;

const styles = StyleSheet.create({
    container: {
        borderWidth: 2,
        flexDirection: "row",
        justifyContent: "space-between",
        alignItems: "center",
        marginTop: 5,
        marginBottom: 5,
        marginHorizontal: 10,
        borderRadius: 10,
        margin: "auto",
    },
    icon: {
        width: 30,
        right: 0,
    },
    input: {
        paddingLeft: 15,
        paddingRight: 15,
        paddingVertical: 10,
        width: "92%",
    },
});
