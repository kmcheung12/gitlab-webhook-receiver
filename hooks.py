from bottle import route, run, request

def handle_shit():
    print request.json
    return "Handling shit..."

@route('/hooks', method='POST')
def hooks():
    handle_shit()

run(host='0.0.0.0', port=8080, debug=True)
