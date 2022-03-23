class ErrorCode(object):
    ERROR_001_REQUIRED_FIELD_NOT_NULL = '001'
    ERROR_002_PAGE_SIZE_LARGE_THAN_0 = '002'
    ERROR_003_PAGE_LARGE_THAN_0 = '003'
    ERROR_004_PASSWORD_IS_WRONG = '004'


class ErrorMessage(object):
    MESSAGE_001_REQUIRED_FIELD_NOT_NULL = 'Các trường thông tin bắt buộc không được bỏ trống'
    MESSAGE_002_PAGE_SIZE_LARGE_THAN_0 = 'Số lượng phần tử trong trang tìm kiếm phải lớn hơn 0'
    MESSAGE_003_PAGE_LARGE_THAN_0 = 'Số thứ tự của trang hiện tại phải lớn hơn hoặc bằng 0'
    MESSAGE_004_PASSWORD_IS_WRONG = 'Mật khẩu không chính xác'


error_code = ErrorCode()
message = ErrorMessage()
