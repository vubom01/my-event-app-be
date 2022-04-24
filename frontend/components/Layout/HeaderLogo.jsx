import { View, Text, Image, StyleSheet, useWindowDimensions } from "react-native";
import React from "react";
import { useSelector, useDispatch } from "react-redux";
import CommonStyle, { BORDER_COLOR } from "../common/CommonStyle";
import { useNavigation } from "@react-navigation/native";

const HeaderLogo = () => {
    const nav = useNavigation();
    const { height } = useWindowDimensions();
    const auth = useSelector((state) => state.authReducers.auth);
    return (
        <View style={styles.container}>
            <View style={styles.avatarContainer}>
                <Image
                    style={[styles.logo, { marginBottom: 5 }]}
                    source={{
                        uri: "https://scontent.fhan2-4.fna.fbcdn.net/v/t1.6435-1/49204546_581029609007102_1545982587820834816_n.jpg?stp=cp0_dst-jpg_p60x60&_nc_cat=104&ccb=1-5&_nc_sid=1eb0c7&_nc_ohc=mg15yCEA1BYAX-oYnpm&tn=wuNm7sLpi-3BCdM8&_nc_ht=scontent.fhan2-4.fna&oh=00_AT9Ov_C2UIjYv29N51l1DOYfex1E58lNDobUCrCY9zjJbA&oe=625A94D4",
                    }}
                />
                <Text style={styles.title}>SOCIENT</Text>
            </View>

            <View style={[styles.avatarContainer, styles.borderWidth]}
                    onPress={() => nav.navigate("Profile")}>
                <Image
                    style={[styles.avt, { marginBottom: 5 }]}
                    source={{
                        uri: auth.user?.avatar,
                    }}
                />
                <Text style={styles.name}>{auth.user?.username}</Text>
            </View>
        </View>
    );
};

export default HeaderLogo;
const styles = StyleSheet.create({
    container: {
        flexDirection: "row",
        justifyContent: "space-between",
        alignItems: "center",
        padding: 5,
        marginHorizontal: 5,
    },
    avt: {
        width: 40,
        height: 40,
        backgroundColor: "black",
        zIndex: 1000,
        transform: [{ translateX: -5 }],
        borderRadius: 50,
        overflow: "hidden",
    },
    logo: {
        width: 50,
        height: 50,
    },
    avatarContainer: {
        flexDirection: "row",
        alignItems: "center",

        height: 25,
        justifyContent: "space-between",
        shadowColor: "red",
    },
    borderWidth: {
        borderWidth: 1,
        borderColor: BORDER_COLOR,
        borderRadius: 400,
    },
    name: {
        fontSize: 16,
        paddingHorizontal: 5,
        paddingBottom: 2,
        marginRight: 5,
        alignSelf: "center",
    },
    title: {
        fontSize: 16,
        paddingHorizontal: 5,
        fontWeight: "700",
        color: "#5D5FEF",
    },
});
