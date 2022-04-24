import { View, Text, StyleSheet, TextInput, ScrollView, FlatList, StatusBar } from "react-native";
import React, { useState, useEffect, useCallback } from "react";
import { useSelector, useDispatch } from "react-redux";
import DateTimePicker from "@react-native-community/datetimepicker";
import * as ImagePicker from "expo-image-picker";

import EventPostBtn from "../../components/EventItem/EventPostBtn";
import { BORDER_COLOR } from "../../components/common/CommonStyle";
import CustomButton from "../../components/ButtonComponent/CustomButton";
import SlideModal from "../../components/modal/SlideModal";
import CustomSwitch from "../../components/switch/Switch";
import CustomDateTimePicker from "../../components/DateTimePicker/CustomDateTimePicker";
import { CategoryList, ImagePost } from "./component";
import { categories } from "./data/category";
import { background, color } from "../../theme";
import { addEvent, editEvent } from "../../redux/actions";

const EventCreate = ({ route, navigation }) => {
    const [modalVisible, setModalVisible] = useState(false);
    const [modalImageVisible, setModalImageVisible] = useState(false);
    const [isToggleNav, setToggleNav] = useState(false);
    const [title, setTitle] = useState("");
    const [description, setDescription] = useState("");
    const [isEnabled, setIsEnabled] = useState(false);
    const [selectCategory, setSelectCategory] = useState({
        id: 1,
        name: categories[0].name,
    });
    const [imageList, setImageList] = useState([]);
    const [location, setLocation] = useState({
        name: "Chọn địa điểm",
        lat: 0,
        long: 0,
    });
    const [date, setDate] = useState({
        start: new Date(),
        end: new Date(),
    });
    const [mode, setMode] = useState("date");
    const [show, setShow] = useState(0);
    const eventId = route.params?.eventId;

    const [loading, setLoading] = useState(false);
    const onFocus = () => {
        setToggleNav(true);
    };
    const onBlur = () => {
        setToggleNav(false);
    };

    const dispatch = useDispatch();
    const { app, events } = useSelector((state) => state.authReducers);

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
        if (route.params?.location) {
            let { name, lat, long } = route.params?.location;
            setLocation({ lat, name, long });
        }
    }, [route.params?.location]);

    useEffect(() => {
        if (eventId) {
            const index = events.findIndex((event) => event.id === route.params.eventId);
            if (index > -1) {
                navigation.setOptions({ title: "Chỉnh sửa sự kiện" });
                const { description, event_name, end_at, start_at, lat, long, images, status, location_name, topic } = events[index];
                setSelectCategory({ ...selectCategory, name: topic });
                setDescription(description);
                setTitle(event_name);
                setDate({
                    start: start_at,
                    end: end_at,
                });
                setIsEnabled(status);
                setImageList(images);
                setLocation({
                    lat,
                    long,
                    name: location_name,
                });
            }
        }
    }, [eventId]);

    const goSelectMap = () => {
        navigation.navigate("MapScreen");
    };

    const toggleSwitch = () => setIsEnabled((previousState) => !previousState);

    const handlecheckCategory = useCallback(
        (id) => {
            let index = categories.findIndex((category) => category.id === id);
            if (index !== -1) {
                setSelectCategory({
                    id: id,
                    name: categories[index].name,
                });
            }
        },
        [selectCategory]
    );
    const pickImage = async () => {
        let result = await ImagePicker.launchImageLibraryAsync({
            mediaTypes: ImagePicker.MediaTypeOptions.All,
            allowsEditing: true,
            quality: 1,
        });

        if (!result.cancelled) {
            setImageList([...imageList, result.uri]);
        }
    };

    const onChange = (event, selectedDate) => {
        let value = { ...date };
        if (show === 1) {
            value.start = selectedDate;
        } else {
            value.end = selectedDate;
        }
        setShow(0);
        setDate(value);
    };

    const showMode = (currentMode, type) => {
        setShow(type === "start" ? 1 : 2);
        setMode(currentMode);
    };

    const showDatepicker = useCallback(
        (type) => {
            showMode("date", type);
        },
        [show]
    );

    const showTimepicker = useCallback(
        (type) => {
            showMode("time", type);
        },
        [show]
    );

    const handleCategorySelect = () => {
        setModalVisible(false);
    };

    const handleImageDelete = useCallback(
        (index) => {
            let list = imageList.filter((image, ind) => ind !== index);
            setImageList(list);
        },
        [imageList]
    );
    const handlePressEdit = () => {
        setLoading(true);
        setTimeout(() => {
            let formData = {
                id: eventId,
                topic: selectCategory.name,
                event_name: title,
                start_at: date.start,
                end_at: date.end,
                description,
                lat: 0,
                long: 0,
                images: [...imageList],
                location_name: location.name,
                status: isEnabled,
            };

            dispatch(editEvent(formData));
            setLoading(false);
            navigation.navigate("EventCreateMe");
        }, 1000);
    };
    const handlePressPost = () => {
        setLoading(true);
        setTimeout(() => {
            let formData = {
                topic: selectCategory.name,
                event_name: title,
                start_at: date.start,
                end_at: date.end,
                description,
                lat: 0,
                long: 0,
                images: [...imageList],
                location_name: location.name,
                status: isEnabled,
            };

            dispatch(addEvent(formData));
            setLoading(false);
            navigation.navigate("EventCreateMe");
        }, 1000);
    };
    return (
        <View style={styles.container}>
            <StatusBar />
            <SlideModal setModalVisible={setModalVisible} modalVisible={modalVisible}>
                <View>
                    <Text style={styles.modalText}>Chọn thể loại</Text>
                    <CategoryList data={categories} onPress={handlecheckCategory} select={selectCategory.id} />
                    <View style={styles.categoryWrap}>
                        <View style={styles.category}>
                            <CustomButton text="Chọn thể loại" type="category" onPress={handleCategorySelect} />
                        </View>
                    </View>
                </View>
            </SlideModal>

            <ScrollView showsVerticalScrollIndicator={false}>
                <View style={styles.inputTitleContainer}>
                    <View style={styles.inputWrap}>
                        <TextInput style={styles.input} value={title} onChangeText={setTitle} onFocus={onFocus} onBlur={onBlur} placeholder="Tiêu đề"></TextInput>
                    </View>
                    <CustomSwitch isEnabled={isEnabled} toggleSwitch={toggleSwitch} />
                </View>
                <View style={styles.inputContainer}>
                    <TextInput style={styles.descriptionInput} onFocus={onFocus} onBlur={onBlur} value={description} onChangeText={setDescription} multiline placeholder="Mô tả"></TextInput>
                </View>
                <EventPostBtn title="Thể loại" text={selectCategory.name} iconName="notebook-outline" bgColor={background.white} onPress={() => setModalVisible(true)} />
                <EventPostBtn title="Địa điểm" text={location.name} iconName="map-marker" bgColor={background.white} onPress={goSelectMap} />
                <EventPostBtn title="Ảnh event" text={`${imageList.length} ảnh`} iconName="group" bgColor={background.white} onPress={() => setModalImageVisible(true)} />
                <CustomDateTimePicker title={"Bắt đầu"} onPressTime={() => showTimepicker("start")} onPressDate={() => showDatepicker("start")} time={date.start} date={date.start} />
                <CustomDateTimePicker title={"Kết thúc"} onPressTime={() => showTimepicker("end")} onPressDate={() => showDatepicker("end")} time={date.end} date={date.end} />

                <View style={{ marginTop: 15, marginBottom: 5 }}>
                    {app.router !== "edit" ? (
                        <CustomButton text="Đăng bài viết" bgColor={background.random} ftColor={color.white} onPress={handlePressPost} loading={loading} />
                    ) : (
                        <CustomButton text="Chỉnh sửa bài viết" bgColor={background.random} ftColor={color.white} onPress={handlePressEdit} loading={loading} />
                    )}
                </View>
            </ScrollView>
            <SlideModal setModalVisible={setModalImageVisible} modalVisible={modalImageVisible}>
                <View>
                    <Text style={styles.title}>Các hình ảnh sự kiện ({imageList.length})</Text>
                    <FlatList
                        data={imageList}
                        contentContainerStyle={styles.flatList}
                        keyExtractor={(item, index) => index}
                        showsVerticalScrollIndicator={false}
                        renderItem={({ item, index }) => <ImagePost uri={item} index={index} onPressDelete={handleImageDelete} />}
                        ListFooterComponent={<CustomButton text="Chọn ảnh" bgColor={background.gray} ftColor={color.white} onPress={pickImage} />}
                    />
                </View>
            </SlideModal>
            {show !== 0 && <DateTimePicker testID="dateTimePicker" display="spinner" value={show === 1 ? date.start : date.end} mode={mode} is24Hour={true} onChange={onChange} />}
        </View>
    );
};

export default EventCreate;

const styles = StyleSheet.create({
    flatList: {
        paddingBottom: 100,
        alignItems: "center",
    },
    buttonModal: {},
    container: {
        padding: 10,
    },
    image: {
        flex: 1,
        justifyContent: "center",
        zIndex: 1000,
    },
    icon: {},
    titleContainer: {
        flexDirection: "row",
        alignItems: "center",
        marginBottom: 5,
    },
    inputTitle: {
        borderWidth: 1,
        flexDirection: "row",
    },
    title: {
        fontSize: 16,
        fontWeight: "bold",
        marginLeft: 5,
        color: color.blackText,
    },
    inputContainer: {
        width: "100%",
        height: 150,
        borderWidth: 1,
        marginTop: 10,
        paddingHorizontal: 10,
        paddingVertical: 5,
        borderRadius: 15,
    },
    inputTitleContainer: {
        marginTop: 10,
        flexDirection: "row",
        paddingHorizontal: 10,
        justifyContent: "center",
        alignItems: "center",
    },
    inputWrap: {
        height: 50,
        borderWidth: 1,
        flexDirection: "row",
        borderRadius: 15,
        justifyContent: "center",
        alignItems: "center",
    },
    input: {
        width: "90%",
    },
    descriptionInput: {
        width: "100%",
    },
    scrollView: {
        height: "3000%",
    },
    button: {
        borderRadius: 20,
        padding: 10,
        elevation: 2,
    },
    buttonOpen: {
        backgroundColor: "#F194FF",
    },
    buttonClose: {
        backgroundColor: "#2196F3",
    },
    textStyle: {
        color: "white",
        fontWeight: "bold",
        textAlign: "center",
    },
    modalText: {
        marginBottom: 15,
        fontWeight: "bold",
        fontSize: 18,
        textAlign: "center",
    },
    category: {
        width: "50%",
    },
    categoryWrap: {
        alignItems: "center",
    },
});
