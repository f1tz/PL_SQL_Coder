```
用于加解密 PL/SQL Developer 工具保存的数据库连接密码
```
# 工具如何使用

`PL_SQL_decrypt.py` 用于解密，密文`一行一个`放在`encrypted.txt`里，然后运行`PL_SQL_decrypt.py` 进行解密。

`PL_SQL_encrypt.py` 用于加密，感觉渗透用的不多，如有需要修改源码进行加密。

# 基础信息
## 确认目标是否配置了记录密码
打开 `工具->首选项->登录历史` 选项，确认是否勾选了 `存储历史及带密码存储`，窗口下方的 `历史就保存了目标的连接记录`

## 密码配置文件位置
PL/SQL将登录信息及密码存储在 `user.prefs` 下。该文件一般存储在如下位置：

```
其中USERNAME是你的用户名

C:\Users\USERNAME\AppData\Roaming\PLSQL Developer\Preferences\USERNAME\
C:\Program Files\PLSQL Developer\Preferences\USERNAME\
C:\Program Files (x86)\PLSQL Developer\Preferences\USERNAME\
```

绿色版的PL/SQL，存储位置为：`C:\Users\USERNAME\AppData\Roaming\PLSQL Developer\Preferences\USERNAME\ `
打开`user.prefs` 文件，其中标题 `[LogonHistory]`下面存在多行数字字符串，每一行即为一个登录信息，这些信息是加密的，其明文格式如下：

`<username>/<password>@<server>`

##算法
主要由位移和xor组成 。生成的密文看起来像这样：

`273645624572423045763066456443024120413041724566408044424900419043284194407643904160`

第一组四位数（2736）是密钥值-他是有系统运行时随机生成的四位数（大于2000，小于3000），后面每一位字符根据下面算法进行运算得到4位数字，直至加密完毕。

## 参考
https://www.jianshu.com/p/d0a741c9439a
https://adamcaudill.com/2016/02/02/plsql-developer-nonexistent-encryption/