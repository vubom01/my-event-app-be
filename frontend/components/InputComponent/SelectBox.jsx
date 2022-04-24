import React from "react";
import { StyleSheet, View, Text } from "react-native";
import {Picker} from '@react-native-picker/picker'
export default SelectBox = ({
  titleInput,
  selectedValue,
  setSelectedValue,
  values,
}) => {
  return (
    <View>
      <Text style={styles.titleInput}>{titleInput}</Text>
      <Picker
        selectedValue={selectedValue}
        style={{ height: 50, width: 150 }}
        onValueChange={(itemValue, itemIndex) => setSelectedValue(itemValue)}
      >
        {values.map((value) => (
          <Picker.Item label={value} value={value} key={value} />
        ))}
      </Picker>
    </View>
  );
};

const styles = StyleSheet.create({
  titleInput: {
    color: "grey",
    fontSize: 15,
    fontWeight: "bold",
  },
});
