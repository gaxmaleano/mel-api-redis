from flask import Flask
import os
import redis

app = Flask(__name__)

redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/redis')
def redis_test():
    redis_client.set('foo', 'bar')
    return redis_client.get('foo')

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')