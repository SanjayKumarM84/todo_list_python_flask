import uuid
from init import jsonify, db


def uuid_func():
    return str(uuid.uuid4()).replace('-','')


def success(message,data):
    response = dict()
    response['message'] = message
    response['data'] = data
    return jsonify(response)


def failure(data):
    error_response = dict()
    error_response['message'] = 'error'
    error_response['data'] = data
    return jsonify(error_response)


def add_data(obj):
    try:
        db.session.add(obj)
        db.session.commit()
        return True
    except Exception as err:
        print(str(err))
        return False
