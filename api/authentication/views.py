from api.authentication.models import *
from common_modules.modules import success, failure, add_data

user_api = Blueprint("user", __name__, url_prefix='/api/user')


@user_api.route('/v1/signUp',methods=['POST'])
def sign_up():
    try:
        payload = request.get_json()
        if "first_name" not in payload or payload["first_name"] is None or payload["first_name"] == "":
            return failure("Please enter your name")

        if "phone_no" not in payload or payload["phone_no"] is None or payload["phone_no"] == "":
            return failure("Please enter your phone number")

        if "email" not in payload or payload["email"] is None or payload["email"] == "":
            return failure("Please enter your email address")

        if "password" not in payload or payload["password"] is None or payload["password"] == "":
            return failure("Please enter the password")

        user_exist = UserData.query.filter((UserData.email==payload["email"])|(UserData.phone_no==payload["phone_no"]))
        if user_exist:
            return failure("Email Id / Phone No. already exists!! Please login")

        user_data_obj = UserData()
        user_data_obj.first_name = payload["first_name"]
        user_data_obj.phone_no = payload["phone_no"]
        user_data_obj.email = payload["email"]

        password = generate_password_hash(payload["password"])
        user_data_obj.password = password

        if "last_name" in payload and (payload["last_name"] is not None or payload["last_name"] != ""):
            user_data_obj.last_name = payload["last_name"]

        if add_data(user_data_obj):
            return success('success', 'SignUp Done Successfully')
        return failure("Unable To SignUp")

    except Exception as err:
        print(traceback.print_exc())
        return failure(str(err))


@user_api.route('/v1/login',methods=['POST'])
def login():
    try:
        payload = request.get_json()

        if "email" in payload and (payload["email"] is not None or payload["email"] != ""):
            user_input = payload["email"]
        elif "phone_no" in payload and (payload["phone_no"] is not None or payload["phone_no"] != ""):
            user_input = payload["phone_no"]
        else:
            return failure("Please enter email id or phone no")

        if "password" not in payload or payload["password"] is None or payload["password"] == "":
            return failure("Please enter the password")

        user_obj_exist = UserData.query.filter(or_(UserData.email==user_input,UserData.phone_no == user_input)).first()
        if not user_obj_exist:
            return failure("User not found!! Please sign Up before Login")

        password = payload["password"]
        if check_password_hash(user_obj_exist.password,password):
            return success("Successfully Logged In!!!", user_obj_exist.id)

        return failure('Wrong Password!!! Please Enter the correct password')
    except Exception as err:
        print(traceback.print_exc())
        return failure(str(err))
