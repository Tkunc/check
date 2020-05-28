# py_ver == "3.6.9"
import flask


app = flask.Flask(__name__)


import json
import time
import cgi


@app.route('/feedback_form')
def introduction():
    feedback = ''
    with open('feedback.json', 'r') as feedback_file:
        feedback_dict = json.loads(feedback_file.read())
        for key, value in feedback_dict.items():
            feedback += "<p><i>Анононим, %s</i>: %s</p>" % (cgi.escape(key), cgi.escape(value))
    return """<html>
                <title>Обратная связь</title>
                <body>
                %s
                    <form action="/save_feedback" method="post">
                        Поделитесь своим мнением: <input name="feedback" type="text" />
                        <input name="submit" type="submit" value="Отправить">
                    </form>
                </body>
            </html>
""" % cgi.escape(feedback)


@app.route('/save_feedback', methods=["GET", "POST"])
def index_page():
    if flask.request.method == 'POST':
        feedback = cgi.escape(flask.request.form.get('feedback'))
        feedback_dict = {}
        path = 'feedback.json'
        if os.path.exists(path):
            with open(path, 'r') as feedback_file:
                feedback_dict.update(json.load(feedback_file))
        feedback_dict[time.time()] = feedback
        with open(path, 'w') as feedback_file:
            json.dump(feedback_dict, feedback_file)
    return flask.redirect('/feedback_form')

import joblib, pickle, base64, hashlib


@app.route('/secret')
def get_msg():
    if flask.request.data:
        Dat=base64.b64decode(flask.request.data)
        NewStr = data.decode('utf-8')
        msg = json.dumps(new_str)
        if joblib.hash(msg) == hashlib.sha256(msg.encode('utf8')).hexdigest():
            with open('messages', 'a') as msg_log:
                msg_log.write(msg)

@app.after_request

def add_header(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    response.headers['Content-Security-Policy'] = "default-src 'self'"

return response
if __name__ == '__main__':
    app.run()
