import { View, Text, ScrollView } from "react-native";
import React from "react";

const ContainerScrollView = ({ ...props }) => {
    return <ScrollView>{...props}</ScrollView>;
};

export default ContainerScrollView;
