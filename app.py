from flask import Flask
import config
from exts import db
from models import UserModel
from blueprints.qa import qa_blueprint
from blueprints.auth import auth_blueprint
from flask_migrate import Migrate
from flask import Flask, jsonify, request
import json
app = Flask(__name__)

# 绑定配置文件
app.config.from_object(config)

# 把db与app绑定
db.init_app(app)

# 上传数据库
migrate = Migrate(app, db)




# 注册蓝图
app.register_blueprint(qa_blueprint)
app.register_blueprint(auth_blueprint)


@app.route("/login",methods=['post'])
def query_user():
    un = request.json.get("username").strip()
    pd = request.json.get("password").strip()
    user = UserModel.query.filter_by(username=un,password=pd).first()
    if user:
        data = {
            "userid":user.id,
            "username":user.username,
            "phone":user.phone,
            "token":user.token
        }
        res = {
            "code":200,
            "msg":"登录成功",
            "data":data
        }
    else:
        res = {
            "code": 201,
            "msg": "用户名或密码错误",
        }
    return jsonify(res)





if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.run(debug=True)

