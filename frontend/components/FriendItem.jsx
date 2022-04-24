import React from "react";
import { View, StyleSheet, Text, Image,TouchableOpacity } from "react-native";
import { Avatar } from "react-native-elements";
export const FriendItem = ({ name, avatar }) => {
  return (
    <TouchableOpacity style={styles.main}>
      <View style={styles.avatar}>
        <Avatar
          rounded
          source={{
            uri: avatar,
          }}
        />
      </View>
      <Text style={styles.name}>{name}</Text>
    </TouchableOpacity>
  );
};
const styles = StyleSheet.create({
  main: {
    height: 50,
    width: "80%",
    paddingLeft: 10,
    paddingTop: "auto",
    flexDirection: "row",
    marginLeft: 10
  },
  avatar: {
    paddingBottom: 10,
  },
  name: {
    paddingVertical: 7
  }
});
