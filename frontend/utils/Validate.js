export const validateUser = (user) => {
    if (
        String(user)
            .toLowerCase()
            .match(/^(?=[a-zA-Z0-9._]{3,20}$)(?!.*[_.]{2})[^_.].*[^_.]$/)
    ) {
        return { status: false, msg: "" };
    } else {
        return { status: true, msg: "Tên phải chứa từ 3-20 kí tự và không có kí tự đặc biệt" };
    }
};
export const validateEmail = (email) => {
    if (
        String(email)
            .toLowerCase()
            .match(/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)
    ) {
        return { status: false, msg: "" };
    } else {
        return { status: true, msg: "Email phải đúng định dạng" };
    }
};
export const validatePassword = (password) => {
    if (
        String(password)
            .toLowerCase()
            .match(/^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/)
    ) {
        return { status: false, msg: "" };
    } else {
        return { status: true, msg: "Mật khẩu ít nhất 8 kí tự, ít nhất 1 kí tự số" };
    }
};
