from flask import jsonify
    
def json(msg, data, status):
    return jsonify({
        "status": status,
        "msg": msg,
        "data": data
        }), status 