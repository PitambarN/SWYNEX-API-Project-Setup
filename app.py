from flask import Flask,jsonify,request
from dotenv import load_dotenv
import os


app=Flask(__name__)
load_dotenv()
app.secret_key=os.getenv('SECRET_KEY')

@app.route('/health_check',methods=['GET'])
def health_check():
    # print(os.getcwd())
    return jsonify({
        "WELCOME TO MY":os.getenv('APP_NAME')
    })
if __name__ =='__main__':
    app.run(
        host='127.0.0.1',
        port=int(os.getenv("PORT",4070)),
        debug=os.getenv('DEBUG', 'False').lower() == 'true'
        )




