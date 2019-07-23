
## 1.1 celery的介绍

Celery 是什么？

Celery 是一个简单、灵活且可靠的，处理大量消息的分布式系统

专注于实时处理的异步任务队列同时也支持任务调度



![image-20190721204324700](http://puzrnb9d3.bkt.clouddn.com/2019-07-21-124337.png)



## 1.2 celery的安装

#### 1.2.1 virtualenv

```shell
pip install virtualenv
virtualenv env

source env/bin/activate
deactivate

```

#### 1.2.2 virtualenvwrapper

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

#### 1.2.3 pyenv


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

### 1.2.4 celery

```shell
pip install celery[redis]


pip install celery
pip install redis

```


### 1.2.5 redis

```shell
https://redis.io/download

wget http://download.redis.io/releases/redis-5.0.5.tar.gz
tar xzf redis-5.0.5.tar.gz
cd redis-5.0.5
make


```


