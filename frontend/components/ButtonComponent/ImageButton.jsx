import React from "react";
import { View, Text, Image, StyleSheet, TouchableOpacity } from "react-native";

export const ImageButton = ({ source, onPress }) => {
  return (
    <TouchableOpacity onPress={onPress}>
      <Image style={styles.action} source={source} />
    </TouchableOpacity>
  );
};
const styles = StyleSheet.create({
  action: {
    maxHeight: 40,
    maxWidth: 40,
    marginHorizontal: 15,
    marginVertical: 5,
  },
});
