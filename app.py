from api.authentication.views import *
from api.todolist.views import *


app.register_blueprint(user_api)
app.register_blueprint(todolist_api)


@app.route('/home',methods=['GET'])
def home():
    try:
        return success('success','home page')
    except Exception as err:
        print(traceback.print_exc())
        return failure(str(err))

if __name__ == '__main__':
    app.run(debug=True)
