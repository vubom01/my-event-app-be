import React, { useState, useContext, useEffect } from "react";
import * as ImagePicker from "expo-image-picker";
import { View, Text, Image, TextInput, StyleSheet, Button } from "react-native";
import CustomInput from "../../components/InputComponent/CustomInput";
import CustomButton from "../../components/ButtonComponent/CustomButton";
import { useSelector } from "react-redux";
import getUser from "../../service/UserService";
import UserService from "../../service/UserService";
import { useNavigation } from "@react-navigation/native";
export const PasswordChange = () => {
  const auth = useSelector((state) => state.authReducers.auth);
  
  const navigation = useNavigation();
  const [showPw, setShowPw] = useState({
    name: "eye-slash",
    status: true,
  });
  const [showPwNew, setShowPwNew] = useState({
    name: "eye-slash",
    status: true,
  });
  const [showPwRetype, setShowPwRetype] = useState({
    name: "eye-slash",
    status: true,
  });
  const onEyePress = () => {
    if (!showPw.status) {
      setShowPw({
        name: "eye-slash",
        status: true,
      });
    } else {
      setShowPw({
        name: "eye",
        status: false,
      });
    }
  };
  const onEyePressNew = () => {
    if (!showPwNew.status) {
      setShowPwNew({
        name: "eye-slash",
        status: true,
      });
    } else {
      setShowPwNew({
        name: "eye",
        status: false,
      });
    }
  };
  const onEyePressRetype = () => {
    if (!showPwRetype.status) {
      setShowPwRetype({
        name: "eye-slash",
        status: true,
      });
    } else {
      setShowPwRetype({
        name: "eye",
        status: false,
      });
    }
  };
  const [oldPassword, setOldPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");
  const [retypeNewPassword, setRetypeNewPassword] = useState("");
  const [loading, setLoading] = useState({
    updated: false,
  });
  const onConfirmPress = async () => {
    let data = {};
    if (oldPassword !== "") {
      data.current_password = oldPassword;
    }
    if (newPassword !== "") {
      data.update_password = newPassword;
    }
    if (newPassword !== retypeNewPassword) {
      alert("Khong khop");
      return false;
    }

    setLoading({ ...loading, updated: true });
    UserService.updatePassword(auth.token, JSON.stringify(data))
      .then((result) => {
        setLoading({ ...loading, updated: false });
        alert("Updated successfully");
        navigation.navigate("Profile");
      })
      .catch((error) => {
        console.log(error);
        setLoading({ ...loading, login: false });
        alert("Wrong password");
      } );
  };
  return (
    <View style={styles.main}>
      <CustomInput
        titleInput="Old Password"
        setValue={(old) => setOldPassword(old)}
        secureTextEntry={showPw.status}
        icon={{ name: "lock" }}
        iconRight={{ name: showPw.name, type: "font-awesome" }}
        onPress={onEyePress} placeholder="Password"
      ></CustomInput>
      <CustomInput
        titleInput="New Password"
        setValue={(newPassword) => setNewPassword(newPassword)}
        secureTextEntry={showPwNew.status}
        icon={{ name: "lock" }}
        iconRight={{ name: showPwNew.name, type: "font-awesome" }}
        onPress={onEyePressNew} placeholder="Password"
      ></CustomInput>
      <CustomInput
        titleInput="Confirm New Password"
        setValue={(confirmNewPassword) =>
          setRetypeNewPassword(confirmNewPassword)
        }
        secureTextEntry={showPwRetype.status}
        icon={{ name: "lock" }}
        iconRight={{ name: showPwRetype.name, type: "font-awesome" }}
        onPress={onEyePressRetype} placeholder="Password"
      ></CustomInput>

      <View style={styles.confirmButton}>
        <CustomButton
          text="Confirm"
          onPress={onConfirmPress}
          loading={loading.updated}
        ></CustomButton>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  main: {
    marginTop: 10,
    marginLeft: 10,
  },
  confirmButton: {
    // paddingLeft:
    width: "93%",
  },
});
