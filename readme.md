
# 使用说明

在MySQL中导入数据库:

    mysql -h127.0.0.1 -u user -p -D flask_navi -P 3306 < schema.sql

修改secure.py，配置访问数据库的用户名、密码和端口号。

## 部署

推荐使用virtualenv创建隔离环境。
```
pip3 install virtualenv
virtualenv flask-navi/
source flask-navi/bin/activate
pip3 install -r requirements.txt
```


# TODO

* 密码加密
* 用户注册
* 后台页面设计
* 获取站点图标

# 感谢

本项目借鉴并参考了以下项目：

* https://github.com/WebStackPage/WebStackPage.github.io
* https://123.haoip.cn/


熊猫图标作者：http://www.turbomilk.com/