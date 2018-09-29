# 序
influxdb+grafana 监控CPU使用情况

见[博客](https://les1ie.com/2018/09/29/cpu-monitor/)

# 需求

最近玩minecraft的时候电脑CPU似乎很累，所以决定动手做一个监控，放自己笔记本和服务器上看看使用cpu的情况

初步打算是influxdb+grafana

当我怀揣着想法上网搜解决方案的时候，发现这两个组合似乎广泛使用


> 你能想到的绝大部分很先进的东西，别人早就想到了。
-- 真理

不过自己动手，丰衣足食，头铁就行。最后我还是花了一个多小时把这个demo弄出来了



效果如图(效果图不是玩MC的时候截的)



![](http://static.scuseek.com/20180929-201339.png)


![](http://static.scuseek.com/20180929-202458.png)


# 需要的环境

- influxdb
- grafana
- docker


# 使用方法

1. 存数据库的服务器上
  ```
  docker-compose up -d
  ```

2. 需要监控的服务器上 

   ```bash
   pip3 install -r requirements.txt
   python3 main.py
   ```
3. grafana默认账户密码admin admin, 登录进去鼠标点点点点点点点设定data source 
![](http://static.scuseek.com/20180929-202723.png)

4. 添加折线图设定一番即可
   ![](http://static.scuseek.com/20180929-202635.png)


# 缺点

本来就带不动游戏了，现在还需要带influxdb和grafana, 可行的解决方案是把这俩货放在其他服务器上，把clinet丢到mc服上面。

# 跋

开源万岁，感谢这些开源项目的作者。

Les1ie

2018年9月29日20:16:25

# refer:

- https://github.com/influxdata/influxdb-python

- https://github.com/nicolargo/docker-influxdb-grafana/blob/master/docker-compose.yml