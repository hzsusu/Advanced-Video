# Beauty-Android-Java

这个开源示例项目演示了如何快速集成 网易云信 新一代（G2）音视频 SDK，实现美颜的功能。

 在这个示例项目中包含了以下功能：

- 加入通话和离开通话
-  打开美颜和关闭美颜
- 切换前置摄像头和后置摄像头

## 环境准备

- Android Studio 3.4 +

- Android真机设备

- 支持模拟器运行，但是部分功能无法使用

## 运行示例项目

这个段落主要讲解了如何编译和运行实例程序。

#### 获取云信APPKey

在编译和启动实例程序前，您需要首先获取一个可用的App Key：

1. 若您已经与专属客户经理取得联系，可直接向他获取Appkey

2. 若您并未与专属客户经理取得联系那么请按后续步骤获取Appkey

3. 首先在 [网易云信](https://id.163yun.com/register?h=media&t=media&clueFrom=nim&from=bdjjnim0035&referrer=https://app.yunxin.163.com/?clueFrom=nim&from=bdjjnim0035) 注册账号

4. 然后在「应用」一栏中创建您的项目
5. 等待专属客户经理联系您，并向他获取Appkey

6. 将AppKey填写进config.cpp


```
std::string appKey = "set your appkey here";
```
####获取相芯SDK 的证书
1.由于本sample美颜的功能是使用相芯SDK实现的。所以您在使用前需要的获取相芯的证书。

2.复制authpack.java文件到com.faceunity包下

3.详细参考相芯[集成文档](https://github.com/Georgedamu/FULiveDemoDroid/blob/master/docs/Android_Nama_SDK_%E9%9B%86%E6%88%90%E6%96%87%E6%A1%A3.md)

#### 运行项目

1. 点击 Sync 按钮，同步一下工程。或者 Build-->Make Projects。

 2.点击 Run 按钮运行，部署到手机上。

## 功能实现

1.云信接口提供：

   ```
//设置视频采集数据回调，用于美颜等操作
        NERtcEx.getInstance().setVideoCallback(neRtcVideoFrame -> {
            if(openFilter) {
                //此处可自定义第三方的美颜实现
                neRtcVideoFrame.textureId = mFuRender.onDrawFrame(neRtcVideoFrame.data,neRtcVideoFrame.textureId,
                        neRtcVideoFrame.width,neRtcVideoFrame.height);
            }
            return openFilter;
        },true);
   ```

2.faceunity model为相芯美颜功能实现，您也可以替换成自己接入的第三方方案。相芯美颜功能具体参看[相芯接入文档](https://github.com/Georgedamu/FULiveDemoDroid/blob/master/docs/Android_Nama_SDK_%E9%9B%86%E6%88%90%E6%96%87%E6%A1%A3.md)
   

   

