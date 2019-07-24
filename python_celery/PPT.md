
## 1 celery的介绍

Celery 是什么？

Celery 是一个简单、灵活且可靠的，处理大量消息的分布式系统

专注于实时处理的异步任务队列同时也支持任务调度



![image-20190721204324700](http://puzrnb9d3.bkt.clouddn.com/2019-07-21-124337.png)



## 2 celery的安装

#### 2.1 virtualenv

```shell
pip install virtualenv
        virtualenv env

source env/bin/activate
deactivate

```

#### 2.2 virtualenvwrapper

```shell
pip install virtualenvwrapper
ls /usr/local/bin/virtualenvwrapper.sh
source /usr/local/bin/virtualenvwrapper.sh

mkvirtualenv env

# show env list
workon

workon env

# quit env
deactivate

```

#### 2.3 pyenv


```shell
brew install pyenv

https://github.com/pyenv

echo 'eval "$(pyenv init -)"' >> ~/.zshrc


# 当前系统安装的版本
pyenv versions


# 查看可以安装的python版本
pyenv list -l


# 安装和卸载
pyenv install 3.6.4
pyenv uninstall 3.6.4


# 使用指定版本python
# shell > local > global
pyenv shell 3.6.4


# 查看安装的插件
ls -la ~/.pyenv/plugins


https://github.com/pyenv/pyenv-virtualenv
git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc

brew install pyenv-virtualenv

# 查看安装的虚拟环境
pyenv virtualenvs


# 安装指定python版本的虚拟环境
pyenv virtualenv 2.7.4 env


# 激活虚拟环境
pyenv activate env


```

### 2.4 celery

```shell
pip install celery[redis]


pip install celery
pip install redis

```


### 2.5 redis

```shell
https://redis.io/download

wget http://download.redis.io/releases/redis-5.0.5.tar.gz
tar xzf redis-5.0.5.tar.gz
cd redis-5.0.5
make


src/redis-server
src/redis-cli

```


## 3 基本使用


```shell
Package    Version
---------- -------
amqp       2.5.0
billiard   3.6.0.0
celery     4.3.0
kombu      4.6.3
pip        19.2.1
pytz       2019.1
redis      3.2.1
setuptools 41.0.1
vine       1.3.0
wheel      0.33.4
```

```
src/redis-server
```

```shell
(env) ➜  demo_1 git:(master) ✗ python app.py
start 2019-07-25 00:12:25.711772
08645e77-7978-4cdf-a13e-eee7f323a3a5
end 2019-07-25 00:12:25.755517

```

```shell
(env) ➜  demo_1 git:(master) ✗ celery worker -A task -l INFO


celery@bogon v4.3.0 (rhubarb)

Darwin-17.5.0-x86_64-i386-64bit 2019-07-25 00:12:21

[config]
.> app:         my_task:0x106dc6810
.> transport:   redis://localhost:6379/1
.> results:     redis://localhost:6379/2
.> concurrency: 4 (prefork)
.> task events: OFF (enable -E to monitor tasks in this worker)

[queues]
.> celery           exchange=celery(direct) key=celery


[tasks]
  . task.add

[2019-07-25 00:12:21,145: INFO/MainProcess] Connected to redis://localhost:6379/1
[2019-07-25 00:12:21,154: INFO/MainProcess] mingle: searching for neighbors
[2019-07-25 00:12:22,169: INFO/MainProcess] mingle: all alone
[2019-07-25 00:12:22,178: INFO/MainProcess] celery@bogon ready.
[2019-07-25 00:12:25,756: INFO/MainProcess] Received task: task.add[08645e77-7978-4cdf-a13e-eee7f323a3a5]
[2019-07-25 00:12:35,771: INFO/ForkPoolWorker-3] Task task.add[08645e77-7978-4cdf-a13e-eee7f323a3a5] succeeded in 10.013767232s: 5

```