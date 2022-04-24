import React from "react";
import { Text, TouchableOpacity } from "react-native";

export const SmallButton = ({ title }) => {
  return (
    <TouchableOpacity
      style={{
        backgroundColor: "#E1ECF4",
        width: "20%",
        marginRight: 10,
        alignItems: "center",
        borderRadius: 5,
      }}
    >
      <Text style={{ fontWeight: "300", color: "#39739D" }}>{title}</Text>
    </TouchableOpacity>
  );
};
