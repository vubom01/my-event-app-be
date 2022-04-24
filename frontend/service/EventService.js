import axios from "axios";
import APP from "../config/app";
const API = `${APP.BASE_API}events`;
import queryString from "query-string";
import http from "./http";

const getEvents = async (token, params = null) => {
    try {
        let config = {
            headers: {
                authorization: `Bearer ${token}`,
            },
        };
        let url = API;
        if (params) {
            url += "?" + queryString.stringify(params);
        }
        const response = await axios.get(url, config);
        return response.data.data.items;
    } catch (err) {
        console.log("error", err);
        return [];
    }
};

const getById = async (token, id) => {
    try {
        let config = {
            headers: {
                authorization: `Bearer ${token}`,
            },
        };
        const response = await axios.get(API + `/${id}`, config);
        return response.data.data;
    } catch (err) {
        console.log("error in get by id", err);
        return [];
    }
};

const likeOrDislikeEvent = async (token, id, type = "like") => {
    try {
        let config = {
            method: type == "like" ? "post" : "delete",
            url: `${API}/${id}/like`,
            headers: {
                Authorization: `Bearer ${token}`,
                "Content-Type": "application/json",
            },
        };
        await axios(config);
        return true;
    } catch (err) {
        console.log("error in likeOrDislikeEvent", err);
        return false;
    }
};

const getHealcheck = async () => {
    return await http.get("/healthcheck");
};

export default { getEvents, getById, likeOrDislikeEvent, getHealcheck, http };
