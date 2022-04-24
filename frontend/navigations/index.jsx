import { StyleSheet, Text, View, Button } from "react-native";
import React, { useEffect, useState } from "react";

import { useSelector, useDispatch } from "react-redux";
import AuthStack from "./AuthStack";
import AppStack from "./AppStack";
import { NavigationContainer } from "@react-navigation/native";
import { SafeAreaProvider } from "react-native-safe-area-context";
import { getFBLoginUser, getLoginUser } from "../redux/actions/auth_actions";

export default function Nav() {
    const [authLogin, setAuthLogin] = useState(false);
    const auth = useSelector((state) => state.authReducers.auth);
    const dispatch = useDispatch();

    useEffect(() => {
        if (auth.token) {
            setAuthLogin(true);
        } else {
            setAuthLogin(false);
        }
    }, [auth.token]);

    useEffect(() => {
        dispatch(getLoginUser());
    }, []);

    return (
        <NavigationContainer>
            <SafeAreaProvider>{!authLogin ? <AuthStack /> : <AppStack />}</SafeAreaProvider>
        </NavigationContainer>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: "#fff",
        alignItems: "center",
        justifyContent: "center",
    },
});
