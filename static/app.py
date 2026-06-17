# 📁 项目结构
# chatroom/
# ├── app.py
# ├── templates/
# │   └── index.html
# └── static/
#     └── style.css

# ✅ 第一步：app.py（Flask 主程序）
from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print('Message:', msg)
    send(msg, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True, allow_unsafe_werkzeug=True)

# ✅ 第二步：templates/index.html
# 创建 templates/index.html 文件，内容如下：

"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Flask 聊天室</title>
  <link rel="stylesheet" href="/static/style.css">
  <script src="https://cdn.socket.io/4.7.2/socket.io.min.js"></script>
</head>
<body>
  <div class="container">
    <h1>简易聊天室</h1>
    <ul id="messages"></ul>
    <input id="messageInput" placeholder="输入消息...">
    <button onclick="sendMessage()">发送</button>
  </div>

  <script>
    const socket = io();
    const input = document.getElementById('messageInput');
    const messages = document.getElementById('messages');

    socket.on('message', function(msg) {
      const item = document.createElement('li');
      item.textContent = msg;
      messages.appendChild(item);
      window.scrollTo(0, document.body.scrollHeight);
    });

    function sendMessage() {
      const msg = input.value;
      if (msg.trim() !== '') {
        socket.send(msg);
        input.value = '';
      }
    }

    input.addEventListener('keydown', function(e) {
      if (e.key === 'Enter') sendMessage();
    });
  </script>
</body>
</html>
"""

# ✅ 第三步：static/style.css
# 创建 static/style.css 文件，内容如下：

"""
body {
  font-family: sans-serif;
  background: linear-gradient(to right, #f8fafc, #e0f2fe);
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  margin: 0;
}
.container {
  background: white;
  padding: 2rem;
  border-radius: 1rem;
  box-shadow: 0 0 10px rgba(0,0,0,0.1);
  width: 400px;
}
h1 {
  text-align: center;
}
ul {
  list-style: none;
  padding: 0;
  max-height: 300px;
  overflow-y: auto;
  margin-bottom: 1rem;
  border: 1px solid #ddd;
  border-radius: 0.5rem;
}
li {
  padding: 0.5rem;
  border-bottom: 1px solid #eee;
}
input {
  width: 75%;
  padding: 0.5rem;
}
button {
  width: 20%;
  padding: 0.5rem;
  margin-left: 5%;
  background-color: #3b82f6;
  color: white;
  border: none;
  border-radius: 0.5rem;
  cursor: pointer;
}
"""


# - 发送图片
# ✅ 安装依赖
# 在终端中运行以下命令：

# pip install flask flask-socketio

# ✅ 运行方式
# 在 PyCharm 或命令行中运行：
# python app.py
# 然后打开浏览器访问：http://127.0.0.1:5000

# 🎉 恭喜你完成了一个可以跑起来的实时聊天室！
# 你可以继续扩展功能，比如：
# - 用户名输入
# - 聊天记录保存
# - 发送图片
# - 聊天室分组
# 想做哪个，我可以继续带你升级。
