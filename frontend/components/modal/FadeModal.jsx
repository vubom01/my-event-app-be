import { StyleSheet, Text, View, Modal, TouchableOpacity, Dimensions } from "react-native";
import React from "react";
import { Icon } from "react-native-elements";
import { color } from "../../theme";
import { background } from "../../theme";
const windowWidth = Dimensions.get("window").width;
const windowHeight = Dimensions.get("window").height;

const FadeModal = ({ modalVisible, setModalVisible, children }) => {
    const handleClose = () => {
        setModalVisible(false);
    };
    return (
        <View>
            <Modal
                animationType="fade"
                transparent={true}
                visible={modalVisible}
                statusBarTranslucent={false}
                onRequestClose={() => {
                    setModalVisible(!modalVisible);
                }}
            >
                <View style={styles.centeredView}>
                    <View style={styles.modalView}>
                        <TouchableOpacity onPress={handleClose}>
                            <Text style={styles.close}>
                                <Icon name="close" type="font-awesome" color={color.black} />
                            </Text>
                        </TouchableOpacity>
                        {children}
                    </View>
                </View>
            </Modal>
        </View>
    );
};

export default FadeModal;

const styles = StyleSheet.create({
    close: {
        textAlign: "right",
    },
    txt: {
        color: "black",
    },
    modalView: {
        backgroundColor: "white",
        borderRadius: 20,
        padding: 10,
        maxWidth: windowWidth * 0.9,
        maxHeight: windowHeight * 0.5,
        shadowColor: "#000",
        shadowOffset: {
            width: 0,
            height: 2,
        },
        shadowOpacity: 0.25,
        shadowRadius: 4,
        elevation: 5,
    },
    centeredView: {
        flex: 1,
        backgroundColor: background.blur,
        alignItems: "center",
        justifyContent: "center",
    },
});
