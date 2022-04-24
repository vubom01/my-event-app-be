import axios from "axios";
// const FB_BASE_URL = "http://192.168.43.182:5002/";

import APP from "../config/app";
const getFbUser = async (token) => {
    return axios.get(`https://graph.facebook.com/me?access_token=${token}&fields=id,name,email,picture.height(500)`);
};
const test = async () => {
    return axios.get(`${APP.BASE_API}healthcheck`);
};
const signUp = async (user) => {
    return axios.post(`${APP.BASE_API}register`, user);
};
const signIn = async (user) => {
    return axios.post(`${APP.BASE_API}login`, user);
};

const getUserInfo = async (token) => {
    let config = {
        headers: {
            authorization: `bearer ${token}`,
        },
    };
    return await axios.get(`${APP.BASE_API}users/me`, config);
};

export default { getFbUser, test, signUp, signIn, getUserInfo };
