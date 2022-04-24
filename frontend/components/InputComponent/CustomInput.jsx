import {
  View,
  Text,
  TextInput,
  StyleSheet,
  width,
  Dimensions,
  TouchableOpacity,
} from "react-native";
import React from "react";
import { Icon } from "react-native-elements";
const windowWidth = Dimensions.get("window").width;

const CustomInput = ({ style, icon, value, setValue, onPress, iconRight, ...props }) => {
  let iconInput = !icon ? "" : <Icon {...icon} />;
  let icon2 =
    props.placeholder !== "Password" ? (
      ""
    ) : (
      <TouchableOpacity onPress={onPress}>
        <Icon {...iconRight} />
      </TouchableOpacity>
    );

  return (
    <View>
      {props.titleInput && (
        <Text style={styles.titleInput}>{props.titleInput}</Text>
      )}

      <View style={styles.container}>
        <Text>{iconInput}</Text>
        <TextInput
          style={styles.input}
          value={value}
          onChangeText={setValue}
          name={props.name}
          {...props}
        />

        <Text style={styles.iconEye}>{icon2}</Text>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  input: {
    marginLeft: 10,
    width: "100%",
    height: "100%",
  },
  titleInput: {
    color: "grey",
    fontSize: 15,
    fontWeight: "bold",
  },
  container: {
    backgroundColor: "#FFFFFF",
    width: windowWidth * 0.9,
    borderWidth: 1,
    borderColor: "black",
    borderRadius: 5,
    paddingHorizontal: 10,
    paddingVertical: 10,
    marginVertical: 5,
    flexDirection: "row",
    justifyContent: "flex-start",
    alignItems: "center",
  },
  iconEye: {
    position: "absolute",
    right: 10,
  },
});

export default CustomInput;
