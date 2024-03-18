#!/usr/env python3
# -*- coding: UTF-8 -*-

from flask import Flask, request, send_file, make_response
from flask_cors import CORS
import json
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "https://agents.baidu.com"}})

movie_recommendations = []
movie_list = []
watch_list = []

def make_json_response(data, status_code=200):
    response = make_response(json.dumps(data), status_code)
    response.headers["Content-Type"] = "application/json"
    return response


@app.route("/like_movie", methods=['POST'])
async def like_movie():
    """
        标记喜欢的电影
    """
    movie = request.json.get('movie', "")
    movie_lists.append(movie)
    return make_json_response({"message": "标记成功"})


@app.route("/dislike_movie", methods=['POST'])
async def dislike_movie():
    """
        标记不喜欢的电影
    """
    movie = request.json.get('movie', "")
    if movie in movie_list:
        movie_list.remove(movie)
    return make_json_response({"message": "标记成功"})


@app.route("/get_movie_recommendations")
async def get_movie_recommendations():
    """
        获取电影推荐
    """
    return make_json_response({"movie_recommendations": movie_recommendations})


@app.route("/get_movie_list")
async def get_movie_list():
    """
        获取电影收藏夹
    """
    return make_json_response({"movie_list": movie_list})


@app.route("/add_to_watchlist", methods=['POST'])
async def add_to_watchlist():
    """
        将电影加入观看列表
    """
    movie = request.json.get('movie', "")
    watch_list.append(movie)
    return make_json_response({"message": "加入成功"})


@app.route("/remove_from_watchlist", methods=['DELETE'])
async def delete_word():
    """
        从观看列表中移除电影
    """
    movie = request.json.get('movie', "")
    if movie in watch_list:
        watch_list.remove(movie)
    return make_json_response({"message": "移除成功"})


@app.route("/logo.png")
async def plugin_logo():
    """
        注册用的：返回插件的 logo，要求 48 x 48 大小的 png 文件.
        注意：API路由是固定的，事先约定的。
    """
    return send_file('logo.png', mimetype='image/png')


@app.route("/ai-plugin.json")
async def plugin_manifest():
    """
        注册用的：返回插件的描述文件，描述了插件是什么等信息。
        注意：API 路由是固定的，事先约定的。
    """
    host = request.host_url
    with open("/ai-plugin.json", encoding="utf-8") as f:
        text = f.read().replace("PLUGIN_HOST", host)
        return text, 200, {"Content-Type": "application/json"}


@app.route("/openapi.yaml")
async def openapi_spec():
    """
        注册用的：返回插件所依赖的插件服务的API接口描述，参照 openapi 规范编写。
        注意：API 路由是固定的，事先约定的。
    """
    with open("/openapi.yaml", encoding="utf-8") as f:
        text = f.read()
        return text, 200, {"Content-Type": "text/yaml"}

@app.route("/example.yaml")
async def exampleSpec():
    host = request.host_url
    with open("example.yaml") as f:
        text = f.read().replace("PLUGIN_HOST", host)
        return text, 200, {"Content-Type": "text/yaml"}



@app.route('/')
def index():
    return 'welcome to my webpage!'

if __name__ == '__main__':
    app.run(debug=True, host='111.67.192.242', port=8089)
