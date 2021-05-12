# self-manage
python wxpython
项目目的：
1.给自己提供一个简单的程序用来记录自己每日信息

项目功能：
1.提供每日打卡功能，记录早起等习惯的养成，记录每日的心情与身体状况
2.提供记账功能，以列表形式展示流水，图标形式展示每月收支
3.提供一些绘图板、图片转pdf之类小工具供自己使用
4.展示室内环境状况（待完成）


技术路径：
1.python作为主要开发语言
2.wxpython库用来实现gui界面
3.excel作为暂时数据储存介质，openpyxl库来操作excel表格
4.pyinstaller用来打包成可执行.exe文件


相关界面如下所示：
打开软件主界面如下所示：
![主界面展示](README_md_files%5C%E5%BC%80%E5%A7%8B%E7%95%8C%E9%9D%A2.png?v=1&type=image)

每日打卡界面：
![打卡成功](README_md_files%5C%E6%89%93%E5%8D%A1%E6%88%90%E5%8A%9F.PNG?v=1&type=image)
![重复打卡](README_md_files%5C%E6%AF%8F%E6%97%A5%E6%89%93%E5%8D%A11.png?v=1&type=image)

每月记录：
![每月打卡](README_md_files%5C%E6%AF%8F%E6%9C%88%E8%AE%B0%E5%BD%95.png?v=1&type=image)

每日支出：
![每日支出](README_md_files%5C%E6%AF%8F%E6%97%A5%E6%94%AF%E5%87%BA.png?v=1&type=image)

每日收入：
![每日收入](README_md_files%5C%E6%AF%8F%E6%97%A5%E6%94%B6%E5%85%A5.png?v=1&type=image)

消费流水：
![消费流水](README_md_files%5C%E6%B6%88%E8%B4%B9%E6%B5%81%E6%B0%B4.PNG?v=1&type=image)

月度情况：
![月度消费](README_md_files%5C%E6%9C%88%E5%BA%A6%E6%83%85%E5%86%B51.PNG?v=1&type=image)

年度消费：
![年度消费](README_md_files%5C%E5%B9%B4%E5%BA%A6%E6%B6%88%E8%B4%B92.PNG?v=1&type=image)

工具：

绘图板：
![绘图板](README_md_files%5C%E7%BB%98%E7%94%BB%E6%9D%BF.png?v=1&type=image)

二维码生成：
将输入的信息转化为二维码，若选择有图片，则生成的二维码中心会有该图片。

![二维码生成](README_md_files%5C%E4%BA%8C%E7%BB%B4%E7%A0%81%E7%94%9F%E6%88%90.png?v=1&type=image)

图片转PDF：
可选择多张图片，拼接成一份PDF文件

![输入图片描述](README_md_files%5C%E5%9B%BE%E7%89%87%E8%BD%ACPDF.png?v=1&type=image)

![输入图片描述](README_md_files%5C%E5%9B%BE%E7%89%87%E8%BD%ACPDF3.png?v=1&type=image)

电子时钟：
![输入图片描述](README_md_files%5C%E7%94%B5%E5%AD%90%E6%97%B6%E9%92%9F.png?v=1&type=image)

注：
1.因使用了pyzbar库，在进行打包会缺少libiconv.dll和libzbar-64.dll 文件，该两文件可在python安装目录下找到，需打包后复制到.exe文件同级目录下。
2.使用pyinstaller库进行打包时，建议首先使用pyinstaller -F -w xxx.py进行打包，这样会以命令行的方式启动看到打包后出现的错误。
3.dist目录下exe文件可直接使用
