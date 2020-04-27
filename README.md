# hexo_album_process
用于获取本地图像文件夹信息，预处理与json文件整合

### 使用方法

> 修改配置文件 config.py

- Image_Root_Path = 你的相册主文件夹根目录

- Hexo_Root_Path = Hexo根目录

- Hexo_Sub_Dir_to_Photos = hexo 中 photos 的相对目录

- Uploading_Temp_Image_Path = 存放压缩图像与json信息的临时文件夹目录

- Image_Url_Prefix = 你的图像链接前缀

> 需要在图像文件夹内配有 readme.json，内容如下

  ```json
  {
  	"time":
  	{
  		"year":2016,
  		"month":1,
  		"day":31
  	},
  	"type":"雪景",
  	"model":"",
  	"position":
  	{
  		"city":"吉林",
  		"street":"乌拉"
  	},
  	"title":"寒冬中的暖色调",
  	"balabala":
  		"不管多冷,还是喜欢暖色调。"
  }
  ```

- 配置好后程序会自动抓取信息

- 需要配置好qshell[Next -22- 添加相册系列 -2- 使用七牛云qshell同步图像目录](https://www.zywvvd.com/2020/03/31/next/22_qiniuyun_qshell/qiniuyun-qshell/)

> 运行 main.py 文件

- 在 Uploading_Temp_Image_Path 中查看运行结果