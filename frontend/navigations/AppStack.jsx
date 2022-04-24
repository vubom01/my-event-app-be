import { SafeAreaView, View, Text } from "react-native";
import React from "react";
import { NavigationContainer } from "@react-navigation/native";
import { createNativeStackNavigator } from "@react-navigation/native-stack";
import { SafeAreaProvider } from "react-native-safe-area-context";

import EventList from "../screens/EventTab/EventList";
import Home from "../screens/Home";
import Tabs from "./Tabs";
import Profile from "../screens/MeTab/Profile";
import { PasswordChange } from "../screens/MeTab/PasswordChange";
import { InfoChange } from "../screens/MeTab/InfoChange";
import { Friend } from "../screens/MeTab/Friend";
import MapScreen from "../screens/MapScreen/MapScreen";
import { DetailEvent } from "../screens/Event/DetailEvent";
import EventCreateMe from "../screens/EventTab/EventCreateMe";
import EventCreate from "../screens/EventTab/EventCreate";
import EventInfo from "../screens/EventTab/EventInfo";
import { color, background } from "../theme";

const Stack = createNativeStackNavigator();
const Navigation = () => {
    const option = (title) => ({
        title: title,
        headerStyle: {
            backgroundColor: background.gray,
        },
        headerTintColor: color.white,
    });
    return (
        <Stack.Navigator>
            <Stack.Screen name="Tabs" component={Tabs} options={{ headerShown: false }} />
            <Stack.Screen name="EventList" component={EventList} options={{ headerShown: false }} />
            <Stack.Screen
                name="Friend"
                component={Friend}
                options={{
                    title: "Bạn bè",
                    headerStyle: {
                        backgroundColor: "transparent",
                        elevator: 0,
                    },
                }}
            />
            
            <Stack.Screen name="DetailEvent" component={DetailEvent} />
            <Stack.Screen name="Profile" component={Profile} options={option("Thông tin cá nhân")} />
            <Stack.Screen name="Change Password" component={PasswordChange} options={option("Thay đổi mật khẩu")} />
            <Stack.Screen name="Change Information" component={InfoChange} options={option("Thay đổi thông tin")} />
            <Stack.Screen name="MapScreen" component={MapScreen} options={option("Bản đồ")} />
            <Stack.Screen name="EventCreateMe" component={EventCreateMe} options={option("Danh sách sự kiện")} />
            <Stack.Screen name="EventCreate" component={EventCreate} options={option("Sự kiện mới")} />
            {/* <Stack.Screen name="Friend" component={Friend} options={option("Bạn bè")} /> */}
            <Stack.Screen name="EventInfo" component={EventInfo} options={option("Thông tin sự kiện")} />
        </Stack.Navigator>
    );
};

export default Navigation;
