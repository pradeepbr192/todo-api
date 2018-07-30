from flask import Flask,jsonify

app = Flask(__name__)

tasks = [
    {
        'id':1,
        'title': 'this is simple description',
        'Description': 'this is an api to call the function'}
,    {
        'id': 2,
        'title': 'this is another simple description',
        'Description': "this is another api to call the function"

    }
]

@app.route('/todo/api/1.0/tasks', methods=['GET'])
def gettasks():
    return jsonify({'tasks': tasks})


if __name__ == '__main__':
    app.run(debug=True)
