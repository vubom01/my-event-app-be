import React, { useState, useEffect } from "react";
import {
  StyleSheet,
  View,
  ScrollView,
  FlatList,
  SafeAreaView,
} from "react-native";
import { useSelector } from "react-redux";
import { FriendItem } from "../../components/FriendItem";
import SearchBar from "../../components/InputComponent/SearchBar";
import FriendService from "../../service/FriendService";
export const Friend = () => {
  const [isToggleNav, setToggleNav] = useState(false);
  const [searchEvent, setSearchEvent] = useState("");

  const auth = useSelector((state) => state.authReducers.auth);
  const [friends, setFriends] = useState([]);
  useEffect(async () => {
    const record = await FriendService.getMyFriends(auth.token);
    setFriends(record.items);
  }, []);
  return (
    <SafeAreaView>
      <View style={styles.main}>
        <View style={styles.header}>
          <View style={styles.header}>
            <SearchBar
              placeholder="Tìm kiếm"
              setToggleNav={setToggleNav}
              setValue={setSearchEvent}
              value={searchEvent}
            />
          </View>
        </View>
        <ScrollView>
          {friends && friends.length > 0 && friends.map((friend) => (
            <View style={styles.item} key={friend.id}>
              <FriendItem
                name={`${friend.first_name + " " + friend.last_name}`}
                avatar={friend.avatar}
              ></FriendItem>
            </View>
          ))}
          <View style={{ marginBottom: 100 }}></View>
        </ScrollView>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  main: {
    alignItems: "center",
  },
  header: {
    marginTop: 10,
    marginBottom: 5,
  },
  item: {
    marginRight: 200,
  },
});
