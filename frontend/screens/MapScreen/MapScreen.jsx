import React, { useEffect, useState } from "react";
import MapView, { Marker, AnimatedRegion, MarkerAnimated, Animated } from "react-native-maps";
import { StyleSheet, Text, View, Dimensions, ActivityIndicator, KeyboardAvoidingView, TouchableOpacity } from "react-native";
import { GooglePlacesAutocomplete } from "react-native-google-places-autocomplete";
import CustomButton from "../../components/ButtonComponent/CustomButton";
import { color, background } from "../../theme";
import * as Location from "expo-location";

const data = [
    {
        latitude: -125,
        longitude: 30,
        latitudeDelta: 0.25,
        longitudeDelta: 0.25,
        name: "quan",
        description: "abc",
    },
    {
        latitude: -126,
        longitude: 31,
        latitudeDelta: 0.25,
        longitudeDelta: 0.25,
        name: "adsf",
        description: "azcv",
    },
    {
        latitude: -128,
        longitude: 38,
        latitudeDelta: 0.25,
        longitudeDelta: 0.25,
        name: "ac",
        description: "adf",
    },
    {
        latitude: -130,
        longitude: 36,
        latitudeDelta: 0.25,
        longitudeDelta: 0.25,
        name: "aaa",
        description: "bbb",
    },
];
export default function MapScreen({ navigation }) {
    const [location, setLocation] = useState({
        latitude: -122,
        longitude: 37,
        latitudeDelta: 0.25,
        longitudeDelta: 0.25,
        name: "Đống Đa",
    });

    useEffect(() => {
        setLoading(true);

        (async () => {
            let { status } = await Location.requestForegroundPermissionsAsync();
            if (status !== "granted") {
                return;
            }
            let location = await Location.getCurrentPositionAsync({});
            // setLocation({ locatio});
        })();
    }, []);

    const [isLoading, setLoading] = React.useState(false);

    const onRegionChange = (region) => {
        // console.log(region);
    };
    const handlePressSearch = (data, details = null) => {
        let { lat, lng } = details.geometry.location;
        let { name } = details;
        setLocation({
            ...location,
            latitude: lat,
            longitude: lng,
            name,
        });
    };

    const handlePressSelect = () => {
        let locationParams = {
            lat: location.latitude,
            long: location.longitude,
            name: location.name,
        };
        navigation.navigate("EventCreate", { location: locationParams });
    };

    if (isLoading) {
        return (
            <View style={styles.container}>
                <KeyboardAvoidingView behavior={Platform.OS === "ios" ? "padding" : "height"}>
                    <GooglePlacesAutocomplete
                        placeholder="Search"
                        styles={{
                            container: {
                                flex: 0,
                            },
                            textInput: {
                                fontSize: 10,
                                color: "black",
                                borderWidth: 1,
                                margin: 0,
                            },
                        }}
                        enablePoweredByContainer={false}
                        minLength={2}
                        fetchDetails={true}
                        returnKeyType={"search"}
                        onPress={handlePressSearch}
                        nearbyPlacesAPI="GooglePlacesSearch"
                        debounce={400}
                        query={{
                            key: "AIzaSyC_8ZzcEbucSlkDlE7GTiLHNhFvfGHDMlQ",
                            language: "en",
                        }}
                    />

                    <View style={styles.paddingVer}></View>
                    <View style={styles.mapWrap}>
                        <MapView style={styles.map} onRegionChangeComplete={onRegionChange} region={location} enabled={false}>
                            {data.map((location, index) => {
                                return (
                                    <Marker
                                        draggable
                                        key={index}
                                        coordinate={{
                                            latitude: location.latitude,
                                            longitude: location.longitude,
                                        }}
                                        title={location.name}
                                        description={location.description}
                                        onDragStart={(e) => {
                                            console.log("dragEnd", e.nativeEvent.coordinate);
                                        }}
                                        onDragEnd={(e) => {
                                            console.log(e.nativeEvent.coordinate);
                                        }}
                                    />
                                );
                            })}
                            <Marker
                                draggable
                                coordinate={{
                                    latitude: location.latitude,
                                    longitude: location.longitude,
                                }}
                                title="Vị trí của bạn"
                                description="giữ vào đây để kéo"
                                onDragStart={(e) => {
                                    console.log("dragEnd", e.nativeEvent.coordinate);
                                }}
                                onDragEnd={(e) => {
                                    console.log(e.nativeEvent.coordinate);
                                }}
                            />
                        </MapView>
                    </View>
                    <View style={styles.nameWrap}>
                        <Text style={styles.title}>{location.name}</Text>
                    </View>
                </KeyboardAvoidingView>

                <View style={styles.padding}>
                    <CustomButton text="chọn địa điểm" bgColor={background.random} onPress={handlePressSelect} />
                </View>
            </View>
        );
    } else {
        return (
            <View style={styles.container}>
                <Text>Loading...</Text>
                <ActivityIndicator size="large" />
            </View>
        );
    }
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        paddingTop: 10,
        paddingHorizontal: 5,
    },
    map: {
        height: Dimensions.get("window").height * 0.57,
    },
    nameWrap: {
        alignItems: "center",
        paddingVertical: 15,
    },
    mapWrap: {
        borderColor: background.gray,
        borderWidth: 1,
        borderRadius: 8,
        overflow: "hidden",
    },
    title: {
        fontSize: 18,
        fontWeight: "bold",
        color: color.blackText,
    },
    search: {
        top: 0,
        width: "100%",
        height: 100,
        borderWidth: 10,
        margin: 2,
    },
    padding: {
        paddingHorizontal: 10,
    },
    paddingVer: {
        paddingVertical: 10,
    },
});
