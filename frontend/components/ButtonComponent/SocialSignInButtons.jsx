/* eslint-disable prettier/prettier */
import { View, Text, TouchableOpacity } from "react-native";
import React, { useEffect } from "react";
import { facebookLogin, setLogin, getLoginUser } from "../../redux/actions/auth_actions";
import { useSelector, useDispatch } from "react-redux";
import CustomButton from "./CustomButton";
import { color, background } from "../../theme";
const SocialSignInButtons = ({ loading, setLoading }) => {
    const dispatch = useDispatch();
    const auth = useSelector((state) => state.authReducers.auth);

    const doLoginFB = async () => {
        setLoading({ ...loading, fbLogin: true });
        await dispatch(facebookLogin());
        setLoading({ ...loading, fbLogin: false });
    };

    return (
        <View style={{ marginTop: 20 }}>
            <CustomButton
                loading={loading.ggLogin}
                icon={{ name: "google", type: "font-awesome", color: color.white, style: { backgroundColor: background.lightGoogle, padding: 5, borderRadius: 5 } }}
                text="Đăng nhập với tài khoản google"
                ftColor={color.white}
                bgColor={background.red}
            />
            <CustomButton
                loading={loading.fbLogin}
                onPress={doLoginFB}
                icon={{ name: "facebook", type: "font-awesome", color: color.blue, style: { backgroundColor: background.lightGoogle, padding: 5, paddingLeft: 8, paddingRight: 8, borderRadius: 5 } }}
                text="Đăng nhập với tài khoản facebook"
                ftColor={color.blueDark}
                bgColor={background.lightWhite}
            />
        </View>
    );
};

export default SocialSignInButtons;
