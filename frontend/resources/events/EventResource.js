import { secondToHms } from "../../helpers/helpers";
import UserService from "../../service/UserService";

export const toEventResource = async (resource, token = null) => {
    const host = token ? await UserService.getUserById(token, resource.host_id) : {};
    return {
        description: resource.description,
        end_at: resource.end_at.split("T")[0] == resource.start_at.split("T")[0] ? resource.end_at.split("T")[1] : resource.end_at,
        event_name: resource.event_name,
        host_id: resource.host_id,
        id: resource.id,
        images: resource.images,
        location: "Not handled",
        start_at: resource.end_at.split("T")[0] == resource.start_at.split("T")[0] ? resource.start_at.split("T")[1] : resource.start_at,
        status: resource.status,
        topic: resource.topic,
        duration: secondToHms((new Date(resource.end_at) - new Date(resource.start_at)) / 1000),
        host,
        start_date: resource.start_at,
    };
};

export const toEventCollection = async (resource, token) => {
    return await Promise.all(resource.map(async (item) => await toEventResource(item, token)));
};
