import { View, Text, Image, StyleSheet, useWindowDimensions, ScrollView } from "react-native";
import React, { useState } from "react";
import { useNavigation } from "@react-navigation/native";
import CustomInput from "../../components/InputComponent/CustomInput";
import CustomButton from "../../components/ButtonComponent/CustomButton";
import AuthService from "../../service/AuthService";
import { validateUser, validateEmail, validatePassword } from "../../utils/Validate";

const Signup = () => {
    const { height } = useWindowDimensions();
    const navigation = useNavigation();

    const [user, setUser] = useState({
        username: "",
        email: "",
        password: "",
        repeatPw: "",
    });

    const [loading, setLoading] = useState(false);
    const [error, setError] = useState({
        status: false,
        msg: "",
    });
    const [signUpMsg, setSignUpMsg] = useState("");

    const onSignInPressed = () => {
        navigation.navigate("Signin");
    };

    const onSignUpPressed = () => {
        if (validateUser(user.username).status) {
            setError(validateUser(user.username));
        } else if (validateEmail(user.email).status) {
            setError(validateEmail(user.email));
        } else if (validatePassword(user.password).status) {
            setError(validatePassword(user.password));
        } else if (user.password !== user.repeatPw) {
            setError({ status: true, msg: "Mật khẩu không khớp" });
        } else {
            setLoading(true);
            setError({ status: false, msg: "" });
            AuthService.signUp(user)
                .then((res) => {
                    setSignUpMsg("Bạn đã đăng kí tài khoản thành công!");
                    setTimeout(() => {
                        setLoading(false);
                        navigation.navigate("Signin");
                    }, 1000);
                })
                .catch((err) => {
                    setLoading(false);
                    console.log("err", err.response.data.message);
                    setError({ status: true, msg: "Tài khoản đã có người sử dụng" });
                });
        }
    };

    return (
        <ScrollView showsVerticalScrollIndicator={false}>
            <View style={styles.root}>
                <View>
                    <Image
                        style={[styles.logo, { height: height * 0.4 }, { marginBottom: 5 }]}
                        source={{
                            uri: "https://intphcm.com/data/upload/logo-the-thao-dep.jpg",
                        }}
                    />
                    <Text style={styles.title}>TẠO TÀI KHOẢN MỚI</Text>
                    <CustomInput
                        placeholder="Tên người dùng"
                        value={user.username}
                        setValue={(value) => {
                            setUser({ ...user, username: value });
                        }}
                        icon={{ name: "user", type: "font-awesome" }}
                    />
                    <CustomInput
                        placeholder="Email"
                        value={user.email}
                        setValue={(value) => {
                            setUser({ ...user, email: value });
                        }}
                        icon={{ name: "email" }}
                    />

                    <CustomInput
                        placeholder="Mật khẩu"
                        value={user.password}
                        setValue={(value) => {
                            setUser({ ...user, password: value });
                        }}
                        secureTextEntry={true}
                        icon={{ name: "lock" }}
                    />
                    <CustomInput
                        placeholder="Nhập lại mật khẩu"
                        value={user.repeatPw}
                        setValue={(value) => {
                            setUser({ ...user, repeatPw: value });
                        }}
                        secureTextEntry={true}
                        icon={{ name: "lock" }}
                    />
                    {error.status && <Text style={{ color: "red", padding: 10 }}>{error.msg}</Text>}
                    {!error.status && signUpMsg > 1 && <Text style={{ color: "green", padding: 10 }}>{signUpMsg}</Text>}
                    <CustomButton text="Đăng ký tài khoản" onPress={onSignUpPressed} loading={loading} />
                    <CustomButton text="Đã có tài khoản? Đăng nhập ngay" bgColor="transparent" onPress={onSignInPressed} type="tertiary" />
                </View>
            </View>
        </ScrollView>
    );
};

export default Signup;
const styles = StyleSheet.create({
    root: {
        alignItems: "center",
        justifyContent: "center",
        padding: 20,
        height: "100%",
    },
    title: {
        fontSize: 24,
        fontWeight: "bold",
        color: "#051C60",
        margin: 10,
        textAlign: "center",
    },
    logo: {},
});
