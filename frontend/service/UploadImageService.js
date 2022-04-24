import axios from "axios";
import APP from "../config/app";

const API = APP.CLOUDINARY_API;

const uploadImage = async (file) => {
    try {
        let config = {
            headers: {
                "content-type": "application/json",
            },
        };
        const response = await axios.post(API, file, config);
        return response.data.secure_url;
    } catch (e) {
        return null;
    }
};

export default { uploadImage };
