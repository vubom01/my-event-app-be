import { SafeAreaView, View, Text } from "react-native";
import React, { useEffect } from "react";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import Signin from "../screens/AuthTab/Signin";
import Signup from "../screens/AuthTab/Signup";

const Stack = createNativeStackNavigator();

const Navigation = () => {
    return (
        <Stack.Navigator>
            <Stack.Screen name="Signin" component={Signin} options={{ headerShown: false }} />
            <Stack.Screen name="Signup" component={Signup} options={{ headerShown: false }} />
        </Stack.Navigator>
    );
};

export default Navigation;
