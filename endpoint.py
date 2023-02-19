from flask import Flask, jsonify

app = Flask(__name__)

people_data = [
    {
    "id":"1",
    "first_name":"Amanda",
    "last_name":"Leech",
    "eye_color":"Hazel",
    "hair_color":"Brown"
    },
    {
    "id":"2",
    "first_name":"Jasmine",
    "last_name":"Leech",
    "eye_color":"Brown",
    "hair_color":"Brown"
    },
    {
    "id":"3",
    "first_name":"Hailey",
    "last_name":"Leech",
    "eye_color":"Blue",
    "hair_color":"Brown"
    },
    {
    "id":"4",
    "first_name":"Amelia",
    "last_name":"Leech",
    "eye_color":"Brown",
    "hair_color":"Blonde"
    },
    {
    "id":"5",
    "first_name":"Bobby",
    "last_name":"Brown",
    "eye_color":"Brown",
    "hair_color":"Brown"
    },
    {
    "id":"6",
    "first_name":"Aspen",
    "last_name":"Leech",
    "eye_color":"Blue",
    "hair_color":"Blonde"
    }
]

@app.route('/')
def say_hello():
    return('Hello World!')


@app.route('/thisisapost', methods=['GET','POST','DELETE'])
def this_is_a_post():
    request_method = request.method
    request_user_agent = request.user_agent
    return "thanks for returning POST<br>Method:{request_method}<br>{request_user_agent}", 200

@app.route('/people')
def people():
    return(people_data)

@app.route('/people/<id>', methods=['GET'])
def get_by_id(id):
    for char in people_data:
        if char['id'] == id:
            return(jsonify(char)), 200
    return"Character not found", 404

@app.route('/people/<id>/<field>', methods=['GET'])
def get_field_by_id(id, field):
    try:
        for char in people_data:
            if char['id'] == id:
                if field in char.keys():
                    return(jsonify(char[field])), 200 # ok
                else:
                    return "Field not found in character", 404 # not found
        return "Character not found", 404
    except:
        return "There was an error finding your data", 400 # bad request

if __name__ =='__main__':
    app.run(host='0.0.0.0', port=8086)

