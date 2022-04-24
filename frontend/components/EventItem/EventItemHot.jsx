import { View, Text, StyleSheet, Image, TouchableOpacity } from "react-native";
import React, { useEffect, useState } from "react";
import MaterialCommunityIcons from "react-native-vector-icons/MaterialCommunityIcons";
import CommonStyle, { BORDER_COLOR, MAIN_COLOR } from "../common/CommonStyle";
import { toEventResource } from "../../resources/events/EventResource";
import EventService from "../../service/EventService";
import { useDispatch, useSelector } from "react-redux";
import { setLogin } from "../../redux/actions/auth_actions";
import { addItem, removeItem } from "../../redux/actions/favorite_actions";
// import AsyncStorage from "@react-native-async-storage/async-storage";
const EventItemHot = ({ item, onPress, onFresh }) => {
  const [event, setEvent] = useState(item);
  const auth = useSelector((state) => state.authReducers.auth);
  const favorite = useSelector((state) => state.authReducers.favorite);
  const dispatch = useDispatch();

  const [liked, setLiked] = useState(false);
  useEffect(()=> {
    const getUpdatedEvent = async () => {
      const record = await EventService.getById(auth.token, item.id);
      setEvent(await toEventResource(record, auth.token));
    }
    getUpdatedEvent();
  }, []);
  useEffect(() => {
    const getLikedStatus = async () => {
      const record = await EventService.getEvents(auth.token, { type: "like" });
      const isLiked = record.some((item) => item.id === event.id);
      setLiked(isLiked);
    };
    getLikedStatus();
  }, [liked, onFresh, favorite]);
  const onPressLiked = async () => {
    const likeOrDislike = await EventService.likeOrDislikeEvent(
      auth.token,
      event.id,
      liked ? "dislike" : "like"
    );
    if (likeOrDislike) {
      alert(
        liked
          ? "Đã xóa khỏi danh sách yêu thích"
          : "Đã thêm vào danh sách yêu thích"
      );
      if (liked) {
        dispatch(removeItem(event));
      } else {
        dispatch(addItem(event));
      }
      setLiked(!liked);
    } else {
      alert("Vui lòng tải lại trang");
    }
  };

  return (
    <TouchableOpacity onPress={onPress}>
      <View style={styles.container}>
        <Image
          style={styles.image}
          source={{
            uri:
              event.images && event.images.length > 0
                ? event.images[0]
                : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS42dec7jSJc9r9eJNqo-6s7S-JMANOe5_1uNd3ca6ZHObtoOGuf5ejxVzhODUTiIiA2lI&usqp=CAU",
          }}
        />
        <View style={styles.contentContainer}>
          <View style={styles.contentWrap}>
            <Text style={styles.title}>{event.event_name}</Text>
          </View>
          <View style={styles.contentWrap}>
            <MaterialCommunityIcons
              size={30}
              style={[styles.icon]}
              name="party-popper"
              color="orange"
              type="font-awesome"
            />
            <Text style={[styles.text]}>{event.event_name}</Text>
          </View>
          <View style={styles.contentWrap}>
            <MaterialCommunityIcons
              size={30}
              style={[styles.icon]}
              name="map-marker-outline"
              color="red"
              type="font-awesome"
            />
            <Text style={[styles.text]}>{event.location}</Text>
          </View>
        </View>
        <TouchableOpacity
          style={styles.heartContainer}
          onPress={() => onPressLiked()}
        >
          <View>
            <MaterialCommunityIcons
              style={[styles.heart]}
              size={30}
              name="heart"
              color={liked ? "red" : "grey"}
              type="font-awesome"
            />
          </View>
        </TouchableOpacity>
      </View>
    </TouchableOpacity>
  );
};

export default EventItemHot;

const styles = StyleSheet.create({
  container: {
    height: 100,
    width: "100%",
    borderWidth: 1,
    borderColor: BORDER_COLOR,
    borderRadius: 15,
    overflow: "hidden",
    marginBottom: 15,
    flexDirection: "row",
    justifyContent: "space-between",
  },
  image: {
    width: "40%",
    height: 100,
    borderRadius: 10,
    resizeMode: "contain",
    overflow: "hidden",
    transform: [{ translateX: -10 }],
  },
  contentWrap: {
    flexDirection: "row",
    paddingHorizontal: 10,
    alignItems: "center",
  },
  title: {
    fontSize: 20,
    fontWeight: "700",
  },
  contentContainer: {
    flex: 2,
  },
  heartContainer: {
    flex: 1,
    justifyContent: "center",
    alignItems: "center",
  },
  heart: {
    // width: 30,
    // height: 20,
  },
  text: {},
  icon: {
    marginRight: 10,
  },
});
