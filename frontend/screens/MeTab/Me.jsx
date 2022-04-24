import {
  View,
  Text,
  Image,
  StyleSheet,
  TouchableOpacity,
  Button,
  SafeAreaView,
  ScrollView,
  StatusBar,
} from "react-native";
import { useSelector, useDispatch } from "react-redux";
import React, { useEffect } from "react";
import Icon from "react-native-vector-icons/FontAwesome";

import CustomTextBox from "../../components/InputComponent/CustomTextBox";
import { getLoginUser, setLogout } from "../../redux/actions/auth_actions";
import { useNavigation } from "@react-navigation/native";
import Profile from "./Profile";

const Me = () => {
  const dispatch = useDispatch();
  const onSignOut = () => {
    dispatch(setLogout());
  };
  const navigation = useNavigation();

  const auth = useSelector((state) => state.authReducers.auth);
  const onProfilePress = () => {
    navigation.navigate("Profile");
  };
  const onFriendPress = () => {
    navigation.navigate("Friend");
  };
  return (
    <View>
      <ScrollView
        style={styles.scrollView}
        showsVerticalScrollIndicator={false}
      >
        <View style={styles.nav}>
          <View style={styles.top}>
            <Image
              style={styles.avatar}
              source={{
                uri: auth.user?.avatar,
              }}
            />
            {/* <TouchableOpacity>
              <Icon style={styles.camera} name="camera"/>
            </TouchableOpacity> */}
          </View>
          <View style={styles.main}>
            <TouchableOpacity style={styles.content} onPress={onProfilePress}>
              <CustomTextBox text={"See my profile"} />
            </TouchableOpacity>
            <TouchableOpacity style={styles.content}>
              <CustomTextBox text={"Check my calendar"} />
            </TouchableOpacity>
            <TouchableOpacity style={styles.content} onPress={onFriendPress}>
              <CustomTextBox text={"Friends"} />
            </TouchableOpacity>
          </View>
          <View style={styles.buttonBox}>
            <Button
              onPress={onSignOut}
              title="Sign Out"
              style={styles.buttonSignout}
            />
          </View>
          <View style={{ marginBottom: 150 }}></View>
        </View>
      </ScrollView>
    </View>
  );
};
const styles = StyleSheet.create({
  nav: {
    marginTop: 20,
  },
  top: {
    justifyContent: "center",
    alignItems: "center",
    height: 200,
    width: 200,
    marginLeft: 80,
    textAlign: "center",
    marginBottom: 20,
  },
  avatar: {
    borderRadius: 100,
    marginTop: 20,
    maxWidth: "100%",
    maxHeight: "100%",
    width: 250,
    height: 250,
  },
  camera: {
    color: "black",
    fontSize: 20,
  },
  main: {
    backgroundColor: "#C4C4C4",
    marginLeft: 15,
    marginRight: 15,
    marginBottom: 30,
    borderRadius: 20,
  },
  content: {
    marginHorizontal: 10,
  },
  buttonBox: {
    marginHorizontal: 20,
  },
  buttonSignout: {
    paddingVertical: 15,
  },
  container: {
    flex: 1,
    paddingTop: StatusBar.currentHeight,
  },
  scrollView: {
    paddingVertical: 20,
    flexGrow: 0,
    height: "100%",
  },
});
export default Me;
