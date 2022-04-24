import React, { useState, useEffect, useRef } from "react";
import { StyleSheet, View, Button, Platform, Text, TouchableOpacity, KeyboardAvoidingView, FlatList, StatusBar, Picker } from "react-native";
import SearchBar from "../../components/InputComponent/SearchBar";
import { BORDER_COLOR } from "../../components/common/CommonStyle";
import { Icon } from "react-native-elements";
import { background, color } from "../../theme";
import Swipeout from "react-native-swipeout";

import { EventCreateMeItem } from "../../components/EventItem/EventCreateMeItem";
import { useDispatch, useSelector } from "react-redux";
import CrudSwipeoutButton from "../../components/ButtonComponent/CrudSwipeoutButton";
import FadeModal from "../../components/modal/FadeModal";
import { deleteEvent, setRouter } from "../../redux/actions";
import EventService from "../../service/EventService";

const dataPicker = {
    all: "Tất cả",
    inActive: "Không hoạt động",
    active: "Hoạt động",
};
const EventCreateMe = ({ navigation }) => {
    const [visibleModalDelete, setVisibleModalDelete] = useState(false);
    const [selectedValue, setSelectedValue] = useState("Lọc");
    const [eventList, setEventList] = useState([]);
    const [keyword, setKeyword] = useState("");
    const eventId = useRef(0);
    const dispatch = useDispatch();
    const goCreateEvent = () => {
        dispatch(setRouter("create"));
        navigation.navigate("EventCreate");
    };
    const { events } = useSelector((state) => state.authReducers);

    const [isToggleNav, setToggleNav] = useState(false);
    useEffect(() => {
        if (isToggleNav) {
            navigation.setOptions({
                tabBarStyle: { display: "none" },
            });
        } else {
            navigation.setOptions({
                tabBarStyle: {
                    display: "flex",
                    position: "absolute",
                    bottom: 10,
                    left: 10,
                    right: 10,
                    elevation: 1,
                    backgroundColor: "#FFFFFF",
                    borderRadius: 10,
                    height: 70,
                    paddingBottom: 10,
                    paddingTop: 5,
                    borderWidth: 1,
                    borderColor: BORDER_COLOR,
                },
            });
        }
    }, [isToggleNav]);

    useEffect(() => {
        setEventList([...events]);
    }, []);

    useEffect(() => {
        (async () => {
            await EventService.getHealcheck().then((res) => {
                console.log("res", res);
            });
        })();
    }, []);

    const handleSearch = () => {
        let newList = events.filter((event) => event.event_name.includes(keyword));
        setEventList([...newList]);
    };
    const handleDeleteEvent = (id) => {
        eventId.current = id;
        setVisibleModalDelete(true);
    };
    const handleEditEvent = (id) => {
        dispatch(setRouter("edit"));
        navigation.navigate("EventCreate", { eventId: id });
    };

    const handleDeleteForce = () => {
        setVisibleModalDelete(false);
        dispatch(deleteEvent(eventId.current));
    };

    const onChangePicker = (itemValue, itemIndex) => {
        let activeEventList = [];
        if (itemValue === dataPicker.all) {
            activeEventList = [...events];
        } else {
            activeEventList = events.filter((event) => (itemValue === dataPicker.active ? event.status : !event.status));
        }
        setEventList([...activeEventList]);
        setSelectedValue(itemValue);
    };
    const swipeoutBtns = (id) => [
        {
            text: "Sửa",
            color: "black",
            backgroundColor: "transparent",
            component: <CrudSwipeoutButton icon="edit" onPress={() => handleEditEvent(id)} type="edit" />,
        },
        {
            text: "Xóa",
            backgroundColor: "transparent",
            component: <CrudSwipeoutButton icon="trash" onPress={() => handleDeleteEvent(id)} type="delete" />,
        },
    ];

    return (
        <View>
            <SearchBar placeholder="Tìm kiếm" setToggleNav={setToggleNav} value={keyword} setValue={setKeyword} onPress={handleSearch} />
            <KeyboardAvoidingView behavior={Platform.OS === "ios" ? "padding" : "height"} style={styles.container}>
                <View style={styles.wrap}>
                    <TouchableOpacity onPress={goCreateEvent}>
                        <View style={styles.plusWrap}>
                            <Icon name="plus" type="font-awesome" color={background.gray} />
                            <Text style={[styles.add, styles.title]}>Tạo mới</Text>
                        </View>
                    </TouchableOpacity>
                    <View style={styles.plusWrap}>
                        <Text style={[styles.filter, styles.title]}>{selectedValue}</Text>
                        {/* <Icon name="filter" type="font-awesome" color={background.gray} /> */}

                        <Picker style={[styles.picker]} selectedValue={selectedValue} style={{ width: 35 }} onValueChange={onChangePicker}>
                            <Picker.Item label={dataPicker.all} value={dataPicker.all} disabled={true} />
                            <Picker.Item label={dataPicker.active} value={dataPicker.active} />
                            <Picker.Item label={dataPicker.inActive} value={dataPicker.inActive} />
                        </Picker>
                    </View>
                </View>
                <View style={styles.main}>
                    {eventList.length > 0 ? (
                        <FlatList
                            data={eventList}
                            keyExtractor={(item, index) => index}
                            scrollEnabled={true}
                            renderItem={({ item, index }) => (
                                <Swipeout right={swipeoutBtns(item.id)} style={styles.btns}>
                                    <EventCreateMeItem name={item.event_name} status={item.status} />
                                </Swipeout>
                            )}
                            showsVerticalScrollIndicator={false}
                            ListFooterComponent={<View style={{ paddingBottom: 300 }}></View>}
                        />
                    ) : (
                        <View style={styles.noEvent}>
                            <Text style={styles.text}>Không có sự kiện nào!</Text>
                        </View>
                    )}
                </View>
            </KeyboardAvoidingView>

            <FadeModal modalVisible={visibleModalDelete} setModalVisible={setVisibleModalDelete}>
                <View style={styles.modalContainer}>
                    <Text>Bạn có muốn xóa sự kiện này</Text>
                    <TouchableOpacity onPress={handleDeleteForce}>
                        <View style={styles.confirmBtn}>
                            <Text style={{ color: color.blackText, fontSize: 18 }}>Có</Text>
                        </View>
                    </TouchableOpacity>
                </View>
            </FadeModal>
        </View>
    );
};

export default EventCreateMe;
const styles = StyleSheet.create({
    disablePicker: {
        display: "none",
    },
    picker: {
        borderRadius: 50,
    },
    swipeBtn: {
        width: "100%",
        height: "100%",
        alignItems: "center",
        justifyContent: "center",
    },
    container: {
        paddingHorizontal: 15,
    },
    confirmBtn: {
        backgroundColor: background.lightPink,
        color: color.white,
        paddingHorizontal: 20,
        paddingVertical: 10,
        marginTop: 20,
        marginBottom: 5,
        borderRadius: 10,
    },
    modalContainer: {
        width: 300,
        alignItems: "center",
    },
    noEvent: {
        paddingTop: 10,
        justifyContent: "center",
        alignItems: "center",
    },
    text: {
        fontSize: 14,
        fontWeight: "bold",
        color: color.blackText,
    },
    title: {
        fontSize: 16,
        fontWeight: "bold",
        color: color.blackText,
    },
    center: {
        flex: 1,
        alignItems: "center",
        justifyContent: "center",
        borderRadius: 10,
        overflow: "hidden",
    },
    delete: {
        marginHorizontal: 2,
        backgroundColor: background.brown,
    },
    edit: {
        marginHorizontal: 2,
        backgroundColor: background.gray,
    },
    plusWrap: {
        paddingTop: 5,
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "center",
    },
    wrap: {
        marginTop: 5,
        flexDirection: "row",
        alignItems: "center",
        justifyContent: "space-between",
    },
    add: {
        marginLeft: 7,
    },
    filter: {
        marginRight: 7,
    },
    main: {
        marginTop: 10,
    },
    btns: {
        height: 60,
        borderRadius: 10,
        height: 55,
        marginVertical: 5,
        backgroundColor: "transparent",
    },
});
