import { StyleSheet, Text, View, FlatList } from "react-native";
import { categories } from "../data/category";
import React, { memo } from "react";
import { Category } from "./Category";

export const CategoryList = memo(({ onPress, data, select }) => {
    const { flatList } = styles;
    return (
        <FlatList
            contentContainerStyle={flatList}
            numColumns={2}
            data={data}
            keyExtractor={(category) => String(category.id)}
            renderItem={({ item }) => <Category id={item.id} name={item.name} image={item.image} onPress={onPress} select={select} />}
        />
    );
});

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    flatList: {
        alignItems: "center",
    },
});
