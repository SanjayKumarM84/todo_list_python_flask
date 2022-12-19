from api.todolist.models import *
from api.authentication.models import *
from common_modules.modules import success, failure, add_data


todolist_api = Blueprint("todolist",__name__,url_prefix="/api/todolist")


@todolist_api.route("/v1/create",methods=["POST"])
def create_todolist():
    try:
        payload = request.get_json()

        user_id = request.headers["user_id"]
        if user_id is None or user_id == "":
            return failure("User Id Not Passed")

        user_exist_obj = UserData.query.filter_by(id=user_id).first()
        if not user_exist_obj:
            return failure("User Not Found!!!")

        days = ""
        if "days" in payload:
            days = payload["days"]

        date = ""
        if "date" in payload:
            date = payload["date"]

        if days == "" and date == "":
            return failure("Enter atleast day or date to save your todolist")

        description = payload["description"]

        todolist_obj = TodoList()
        todolist_obj.description = description
        todolist_obj.user_id = user_id

        if days != "":
            todolist_obj.days = days
        if date != "":
            todolist_obj.date = date

        if add_data(todolist_obj):
            return success("success","TodoList Created Successfully")

        return failure("Something Went Wrong!!")
    except Exception as err:
        print(traceback.print_exc())
        return failure(str(err))


@todolist_api.route("/v1/getTodolist",methods=['GET'])
def get_todolist():
    try:
        import datetime
        user_id = request.headers["user_id"]

        if "day" in request.args:
            today = request.args.get("day")
            today_date = ""
        elif "date" in request.args:
            today_date = str(request.args.get("date"))
            today = datetime.datetime.strptime(today_date,"%Y-%m-%d").strftime("%A")
        else:
            date = datetime.datetime.now()
            today_date = date.strftime("%Y-%m-%d")
            today = date.strftime("%A")

        user_todolist = TodoList.query.filter_by(user_id=user_id).all()
        if not user_todolist:
            return failure("User doesn't have any todolists")
        
        final_dict = dict()
        result = list()
        for each in user_todolist:
            if each.days is not None and today in each.days:
                todolist_dict = {}
                todolist_dict["id"] = each.id
                todolist_dict["todolist"] = each.description
                todolist_dict["today"] = today
                todolist_dict["days"] = each.days
                result.append(todolist_dict)
            elif each.date is not None and each.date == today_date:
                day = datetime.datetime.strptime(each.date,"%Y-%m-%d").strftime("%A")
                if day == today:
                    todolist_dict = {}
                    todolist_dict["id"] = each.id
                    todolist_dict["todolist"] = each.description
                    todolist_dict["today"] = day
                    todolist_dict["only_on"] = each.date
                    result.append(todolist_dict)
                    final_dict["todolist"] = each.description
                else:
                    continue
            else:
                continue

        if len(result) > 0:
            final_dict["todolist"] = result

        return success("success",final_dict)
    except Exception as err:
        print(traceback.print_exc())
        return failure(str(err))
