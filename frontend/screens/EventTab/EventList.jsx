import * as React from "react";
import MapView from "react-native-maps";
import { StyleSheet, Text, View, Dimensions, ActivityIndicator, KeyboardAvoidingView } from "react-native";
import { GooglePlacesAutocomplete } from "react-native-google-places-autocomplete";

const API_KEY_GOOGLE = "4201738803816157";
export default function EventList() {
    const [location, setLocation] = React.useState({
        latitude: -122,
        longitude: 37,
        latitudeDelta: 0.05,
        longitudeDelta: 0.05,
    });

    const [isLoading, setLoading] = React.useState(false);
    const onRegionChange = (region) => {
        // setLocation({ ...region });
        // setLocation
        // console.log(region);
        // console.log(region);
    };

    React.useEffect(() => {
        setLoading(true);
    }, []);

    if (isLoading) {
        return (
            <View style={styles.container}>
                <KeyboardAvoidingView behavior={Platform.OS === "ios" ? "padding" : "height"} style={styles.container}>
                    <View style="search">
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
                            onPress={(data, details = null) => {
                                console.log(details.geometry.location);
                            }}
                            nearbyPlacesAPI="GooglePlacesSearch"
                            debounce={400}
                            query={{
                                key: "AIzaSyC_8ZzcEbucSlkDlE7GTiLHNhFvfGHDMlQ",
                                language: "en",
                            }}
                        />
                    </View>

                    <MapView style={styles.map} onRegionChangeComplete={onRegionChange} region={location} enabled={false} />
                </KeyboardAvoidingView>
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
        // justifyContent: "center",
        marginTop: 20,
    },
    map: {
        width: Dimensions.get("window").width,
        height: Dimensions.get("window").height / 1.8,
    },
    search: {
        top: 0,
        width: "100%",
        height: 100,
        borderWidth: 10,
        // marginTop: 100,
        margin: 2,
    },
});
