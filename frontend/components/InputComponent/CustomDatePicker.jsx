import React, { useState } from "react";
import { Button, StyleSheet, Text, View } from "react-native";
import DateTimePicker from "@react-native-community/datetimepicker";
import { Icon } from "react-native-elements";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";

export default CustomDatePicker = ({ title, date, setDate, open, setOpen }) => {
    const onChange = (event, selectedDate) => {
        if (event.type == "set") {
            const currentDate = selectedDate;
            setOpen(false);
            setDate(currentDate.toISOString().split("T")[0]);
        } else {
            return null;
        }
    };

    return (
        <View>
            <View>
                <Text style={styles.titleInput}>{title}</Text>
                <Text onPress={() => setOpen(true)}>
                    <MaterialCommunityIcons name="calendar" size={30} />
                    <Text style={styles.boxDate}>{date}</Text>
                </Text>
            </View>
            {open && <DateTimePicker testID="dateTimePicker" value={new Date(date)} is24Hour={true} onChange={onChange} />}
        </View>
    );
};

const styles = StyleSheet.create({
    titleInput: {
        color: "grey",
        fontSize: 15,
        fontWeight: "bold",
    },
    boxDate: {
        paddingHorizontal: 10,
    },
});
