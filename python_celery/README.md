
## 1 工具安装

### 1.1 itext

```
xrhd
https://pan.baidu.com/s/1LFZ64mHu_zPv4mg7GCECng#xrhd

sudo spctl --master-disable

https://apps.apple.com/cn/app/itext-ocr-%E8%AF%86%E5%88%AB-%E7%BF%BB%E8%AF%91%E5%9B%BE%E7%89%87%E4%B8%AD%E7%9A%84%E6%96%87%E5%AD%97/id1314980676?mt=12
```

快捷键 `COMMOND + SHIFT + 1`


### 1.2 typora

```
https://www.typora.io/
```


### 1.3 ipic

```
https://toolinbox.net/iPic/

https://apps.apple.com/cn/app/id1101244278?mt=12
```

需要高级版才能开放别的图床， 废弃使用


### 1.4 picgo

```
https://github.com/Molunerfinn/PicGo


```



### 1.4 qiniu


使用七牛的对象存储作为图床
```
https://portal.qiniu.com/bucket

```


## 2 git无法提交

macOS 10.13.4 git无法提交

```
https://help.github.com/en/articles/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent

# clone by ssh

eval "$(ssh-agent -s)"


Host *
  AddKeysToAgent yes
  UseKeychain yes
  IdentityFile ~/.ssh/id_rsa

ssh-add -K ~/.ssh/id_rsa

```
