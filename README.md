### 调用 tinypng API 批量自动压缩图片（png或jpg格式）
环境：python

- 申请key，并配置到wrapper.py (tinify.key)
- https://tinypng.com/developers（一个邮箱可压缩500张图片）
- wrapper.py置于待压缩图片的文件夹中
（或在代码中通过glob.glob指定文件夹位置，脚本只处理png和jpg类型的文件，排除.9.png格式）
- 执行 python3 wrapper.py
- 成功后，原始图片被替换为新的压缩后的图片
