import moment from "moment";
import "moment/locale/vi";
import React, { useEffect, useState } from "react";
import {
  View,
  StyleSheet,
  Text,
  Image,
  ScrollView,
  TouchableOpacity,
  Button,
  ActivityIndicator,
} from "react-native";
import { useDispatch, useSelector } from "react-redux";
import CustomButton from "../../components/ButtonComponent/CustomButton";
import { ImageButton } from "../../components/ButtonComponent/ImageButton";
import { SmallButton } from "../../components/ButtonComponent/SmallButton";
import { BORDER_COLOR, MAIN_COLOR } from "../../components/common/CommonStyle";
import { EventInfo } from "../../components/EventItem/EventInfo";
import { SimpleLoading } from "../../components/LoadingComponent/simpleLoading";
import { MONTH } from "../../config/date";
import { wait } from "../../helpers/helpers";
import { addItem, removeItem } from "../../redux/actions/favorite_actions";
import { toEventResource } from "../../resources/events/EventResource";
import EventService from "../../service/EventService";

moment.locale("vi");
export const DetailEvent = (navigation) => {
  const auth = useSelector((state) => state.authReducers.auth);
  const dispatch = useDispatch();

  const itemId = navigation.route.params.id;
  const [event, setEvent] = useState({});
  const [liked, setLiked] = useState(false);
  const [isLoading, setLoading] = useState(true);
  const [ready, setReady] = useState(false);
  useEffect(() => {
    const getEvent = async () => {
      const record = await EventService.getById(auth.token, itemId);
      setEvent(await toEventResource(record, auth.token));
      setLoading(false);
    };
    getEvent();
  }, []);

  useEffect(() => {
    const isLiked = async () => {
      const likedRecord = await EventService.getEvents(auth.token, {
        type: "like",
      });
      const checkLiked = likedRecord.some((item) => item.id === event.id);
      setLiked(checkLiked);
      wait(1000).then(() => setReady(true));
    };
    isLiked();
  }, [event]);

  const onJoinPress = () => {
    alert("Joined successfully");
  };
  const onLikePress = async () => {
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

  const onRatePress = () => {
    alert("on rate");
  };
  const onSharePress = () => {
    alert("on share");
  };
  const onEditPress = () => {
    alert("on edit");
  };
  return isLoading || !ready ? (
    <SimpleLoading></SimpleLoading>
  ) : (
    Object.keys(event).length > 0 && (
      <View style={styles.container}>
        <ScrollView style={styles.scrollView}>
          <View style={styles.bannerContainer}>
            <Image
              style={styles.banner}
              source={{
                uri:
                  event.images && event.images.length > 0
                    ? event.images[0]
                    : "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS42dec7jSJc9r9eJNqo-6s7S-JMANOe5_1uNd3ca6ZHObtoOGuf5ejxVzhODUTiIiA2lI&usqp=CAU",
              }}
            />
          </View>
          <View style={styles.body}>
            <View style={styles.introContainer}>
              <View>
                <Text style={styles.introTime}>
                  {/* {event.start_at + " - " + event.end_at} */}
                  {event.start_date
                    ? moment(event.start_date).calendar().includes("/")
                      ? moment(event.start_date).format("Do MMMM, h:mm")
                      : moment(event.start_date).calendar()
                    : ""}
                </Text>
                <Text style={styles.introTitle}>{event.event_name}</Text>
                <Text style={styles.introLocation}>{event.location}</Text>
              </View>

              <View style={styles.dateContainer}>
                <Text style={styles.dateText}>
                  {event.start_date?.split("T")[0].split("-")[2]}
                </Text>
                <Text style={styles.monthText}>
                  {MONTH[event.start_date?.split("T")[0].split("-")[1]]}
                </Text>
              </View>
            </View>
            <View style={styles.main}>
              <Text style={styles.titleMain}>Chi tiết sự kiện</Text>

              {/* <EventInfo info={data.host} source={require('../../assets/sand-clock.png')}></EventInfo>| */}
              {event.duration ? (
                <EventInfo
                  info={event.duration}
                  source={require("../../assets/sand-clock.png")}
                ></EventInfo>
              ) : <Text style={{ height: 0 }}></Text>}
              <EventInfo
                info={event.host?.first_name + " " + event.host?.last_name}
                source={require("../../assets/flag.png")}
                type="host"
              ></EventInfo>

              <EventInfo
                info={event.location}
                source={require("../../assets/pin.png")}
              ></EventInfo>

              <EventInfo
                info={event.description}
                source={require("../../assets/info.png")}
              ></EventInfo>
              <View style={{ flexDirection: "row" }}>
                <SmallButton title={event.topic}></SmallButton>
              </View>
            </View>
          </View>
          <View style={{ marginTop: 100 }}></View>
        </ScrollView>

        <View style={styles.actionContainer}>
          <View style={styles.actions}>
            <View style={styles.going}>
              <Text style={styles.optionText}>Tham gia</Text>
            </View>
            <TouchableOpacity
              style={{
                ...styles.liked,
                ...{ backgroundColor: liked ? MAIN_COLOR : "grey" },
              }}
              onPress={onLikePress}
            >
              <Text style={styles.optionText}>Quan tâm</Text>
            </TouchableOpacity>
            <View style={styles.other}>
              <Text style={styles.optionText}>...</Text>
            </View>
          </View>
        </View>
      </View>
    )
  );
};
const styles = StyleSheet.create({
  container: { flex: 1, alignItems: "center" },
  body: {},
  bannerContainer: {
    justifyContent: "space-between",
  },
  banner: {
    height: 137,
    width: 405,
    maxWidth: "95%",
    marginHorizontal: 10,
    marginVertical: 20,
    borderRadius: 20,
  },
  titleContainer: {
    backgroundColor: "#6B42DD",
    height: 100,
    borderColor: "white",
    borderWidth: 2,
    borderRadius: 10,
    marginHorizontal: 10,
    marginTop: 5,
    paddingVertical: 20,
  },
  title: {
    fontSize: 25,
    textAlign: "center",
    color: "white",
    fontWeight: "600",
  },
  time: {
    textAlign: "center",
    color: "white",
  },
  main: {
    backgroundColor: "white",
    borderColor: "white",
    borderWidth: 2,
    borderRadius: 10,
    marginHorizontal: 10,
    marginTop: 5,
    paddingVertical: 20,
  },
  titleMain: {
    fontSize: 20,
    fontWeight: "bold",
    textAlign: "center",
    color: "black",
  },
  actionContainer: {
    // maxHeight: 50,
    // marginTop: 50,
    flex: 0.2,
    position: "absolute",
    bottom: 10,
    justifyContent: "center",
    borderRadius: 10,
    backgroundColor: "#FFFFFF",
    width: "95%",
    shadowColor: "grey",
    borderColor: "grey",
  },
  actions: {
    flexDirection: "row",
    justifyContent: "center",
    height: 50,
    flex: 1,
  },
  introContainer: {
    marginHorizontal: 20,
    // marginTop: 10
  },
  introTime: {
    color: "#5A5C60",
    fontSize: 15,
  },
  introTitle: {
    fontSize: 22,
    fontWeight: "bold",
  },
  introLocation: {
    color: "#5A5C60",
    fontSize: 15,
  },
  dateContainer: {
    position: "absolute",
    borderRadius: 10,
    width: 80,
    height: 80,
    justifyContent: "center",
    alignItems: "center",
    top: 0,
    right: 0,
    borderWidth: 1,
    backgroundColor: MAIN_COLOR,
    borderColor: BORDER_COLOR,
    elevation: 10,
    marginBottom: 10,
  },
  dateText: {
    fontSize: 27,
    fontWeight: "bold",
    color: "#FFFFFF",
  },
  monthText: {
    fontSize: 16,
    color: "#FFFFFF",
  },
  going: {
    backgroundColor: MAIN_COLOR,
    flex: 0.3,
    justifyContent: "center",
    borderRadius: 10,
    height: 40,
  },
  liked: {
    backgroundColor: "grey",
    marginLeft: 10,
    flex: 0.5,
    justifyContent: "center",
    borderRadius: 10,
    height: 40,
  },
  other: {
    backgroundColor: MAIN_COLOR,
    marginLeft: 10,
    flex: 0.2,
    justifyContent: "center",
    borderRadius: 10,
    height: 40,
  },
  optionText: {
    textAlign: "center",
    fontWeight: "bold",
    color: "#FFFFFF",
  },
});
