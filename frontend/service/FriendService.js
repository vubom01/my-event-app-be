import axios from "axios";
import APP from "../config/app";
const API = `${APP.BASE_API}friends`;

const getMyFriends = async (token, query = null) => {
  try {
    let config = {
      headers: {
        authorization: `Bearer ${token}`,
      },
    };
  
    const response = await axios.get(API, config);
    return response.data.data;
  } catch (err) {
    console.log(err);
    return [];
  }
};

export default {getMyFriends};
