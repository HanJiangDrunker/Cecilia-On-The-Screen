#from curses.ascii import SP
import os
import sys
import random
import time
import subprocess
#import datetime
#import speech
import pyttsx3
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from plyer import notification

class DesktopPet(QWidget):
    def __init__(self, parent=None, **kwargs):
        super(DesktopPet, self).__init__(parent)
        # 窗体初始化
        self.init()
        # 托盘化初始
        self.initPall()
        # 宠物静态gif图加载
        self.initPetImage()
        # 宠物正常待机，实现随机切换动作
        #self.petNormalAction()
        #self.time()
        #self.Text()

        # 窗体初始化
    def init(self):
        # 初始化
        # 设置窗口属性:窗口无标题栏且固定在最前面
        # FrameWindowHint:无边框窗口
        # WindowStaysOnTopHint: 窗口总显示在最上面
        # SubWindow: 新窗口部件是一个子窗口，而无论窗口部件是否有父窗口部件
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.SubWindow)
        # setAutoFillBackground(True)表示的是自动填充背景,False为透明背景
        self.setAutoFillBackground(False)
        # 窗口透明，窗体空间不透明
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 重绘组件、刷新
        self.repaint()

        
    # 托盘化设置初始化
    def initPall(self):
        # 导入准备在托盘化显示上使用的图标
        icons = os.path.join('tigerIcon.jpg')
        # 设置右键显示最小化的菜单项
        # 菜单项退出，点击后调用quit函数
        quit_action = QAction('退出', self, triggered=self.quit)
        # 设置这个点击选项的图片
        quit_action.setIcon(QIcon(icons))
        # 菜单项显示，点击后调用showing函数
        showing = QAction(u'显示', self, triggered=self.showwin)
        #版本号显示
        V = QAction('版本：1.3.5 Release', self)
        # 新建一个菜单项控件
        self.tray_icon_menu = QMenu(self)
        # 在菜单栏添加一个无子菜单的菜单项‘退出’
        self.tray_icon_menu.addAction(quit_action)
        # 在菜单栏添加一个无子菜单的菜单项‘显示’
        self.tray_icon_menu.addAction(showing)
        # 在菜单栏添加一个无子菜单的菜单项‘版本’
        self.tray_icon_menu.addAction(V)
        # QSystemTrayIcon类为应用程序在系统托盘中提供一个图标
        self.tray_icon = QSystemTrayIcon(self)
        # 设置托盘化图标
        self.tray_icon.setIcon(QIcon(icons))
        # 设置托盘化菜单项
        self.tray_icon.setContextMenu(self.tray_icon_menu)
        # 展示
        self.tray_icon.show()

    # 退出操作，关闭程序
    def quit(self):
        self.close()
        sys.exit()

    # 显示宠物
    def showwin(self):
        # setWindowOpacity（）设置窗体的透明度，通过调整窗体透明度实现宠物的展示和隐藏
        i = 0.0
        while i<=1:
            self.setWindowOpacity(i)
            i = i + 0.1;
            time.sleep(0.02)

    # 宠物静态gif图加载
    def initPetImage(self):
        # 对话框定义
        self.talkLabel = QLabel(self)
        # 对话框样式设计
        self.talkLabel.setStyleSheet("font:15pt '楷体';border-width: 1px;color:blue;") 
        # 定义显示图片部分
        self.image = QLabel(self)
        # QMovie是一个可以存放动态视频的类，一般是配合QLabel使用的,可以用来存放GIF动态图
        self.movie = QMovie("normal.gif")
        # 设置标签大小
        self.movie.setScaledSize(QSize(130, 250))
        # 将Qmovie在定义的image中显示
        self.image.setMovie(self.movie)
        self.movie.start()
        self.resize(1024, 1024)
        # 调用自定义的randomPosition，会使得宠物出现位置随机
        self.randomPosition()
        # 展示
        #self.setWindowOpacity(0)
        self.show()
        '''
        # 将宠物正常待机状态的动图放入pet1中
        self.pet1 = []
        for i in os.listdir("normal"):
            self.pet1.append("normal/" + i)
        # 将宠物正常待机状态的对话放入pet2中
        self.dialog = []
        # 读取目录下dialog文件
        with open("dialog.txt", "r") as f:
            text = f.read()
            # 以\n 即换行符为分隔符，分割放进dialog中
            self.dialog = text.split("\n")
        '''

    # 指定位置
    def randomPosition(self):
        # screenGeometry（）函数提供有关可用屏幕几何的信息
        screen_geo = QDesktopWidget().screenGeometry()
        # 获取窗口坐标系
        pet_geo = self.geometry()
        width = (screen_geo.width() - pet_geo.width()) * random.random()
        height = (screen_geo.height() - pet_geo.height()) * random.random()
        #self.move(1715,820)
        #self.move(1820,775)  #1920x1080
        self.move(0,0)  #00

 # 宠物右键点击交互
    def contextMenuEvent(self, event):
        # 定义菜单
        menu = QMenu(self)
        # 定义菜单项
        #quitAction = menu.addAction("退出")
        hide = menu.addAction("隐藏")
        WebSite = menu.addMenu("站点")
        CMD = menu.addMenu("指令")
        #Love = menu.addAction("Love You.")
        #二级菜单
        Baidu = WebSite.addAction("百度")
        BiliBili = WebSite.addAction("BiliBili")
        ICO = WebSite.addAction("ICO转换器")
        CPU_Z = WebSite.addAction("CPU-Z")

        Taskmgr = CMD.addAction("任务管理器")
        Slidetoshutdown = CMD.addAction("滑动关机")
        Control = CMD.addAction("控制面板")
        Cleanmgr = CMD.addAction("垃圾整理")
        Explorer = CMD.addAction("资源管理器")
        Winver = CMD.addAction("系统信息")
        # 使用exec_()方法显示菜单。从鼠标右键事件对象中获得当前坐标。mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action = menu.exec_(self.mapToGlobal(event.pos()))
        # 点击事件为退出
        '''
        if action == quitAction:
            qApp.quit()
        '''
        # 点击事件为隐藏
        if action == hide:
            # 通过设置透明度方式隐藏宠物
            i = 1;
            while i>=0:
                self.setWindowOpacity(i)
                i = i - 0.1;
                time.sleep(0.02)
        if action == Baidu:
            os.system("start www.baidu.com")
            CREATE_NO_WINDOW = 0x08000000
            #subprocess.call('taskkill /F /IM exename.exe', creationflags=CREATE_NO_WINDOW)
            #subprocess.call(['cmd'])
        if action == BiliBili:
            os.system("start www.bilibili.com")
        if action == ICO:
            os.system("start www.icoconverter.com")
        if action == CPU_Z:
            os.system("start www.cpuid.com")
        if action == Taskmgr:
            os.system("taskmgr")
        if action == Slidetoshutdown:
            os.system("slidetoshutdown")
        if action == Control:
            os.system("control")
        if action == Explorer:
            os.system("explorer")
        if action == Winver:
            os.system("winver")
        if action == Cleanmgr:
            os.system("cleanmgr")
        if action == Love:
            os.system("start https://music.163.com/#/song?id=431551064")

    def mousePressEvent(self, event):
        # 更改宠物状态为点击
        #self.condition = 1
        # 更改宠物对话状态
        #self.talk_condition = 1
        # 即可调用对话状态改变
        #self.talk()
        # 即刻加载宠物点击动画
        #self.randomAct()
        if event.button() == Qt.LeftButton:
            self.is_follow_mouse = True
        # globalPos() 事件触发点相对于桌面的位置
        # pos() 程序相对于桌面左上角的位置，实际是窗口的左上角坐标
        self.mouse_drag_pos = event.globalPos() - self.pos()
        event.accept()
        # 拖动时鼠标图形的设置
        #self.setCursor(QCursor(Qt.OpenHandCursor))
 
    # 鼠标移动时调用，实现宠物随鼠标移动
    def mouseMoveEvent(self, event):
        # 如果鼠标左键按下，且处于绑定状态
        if Qt.LeftButton and self.is_follow_mouse:
            # 宠物随鼠标进行移动
            self.move(event.globalPos() - self.mouse_drag_pos)
        event.accept()
 
    # 鼠标释放调用，取消绑定
    def mouseReleaseEvent(self, event):
        self.is_follow_mouse = False
        # 鼠标图形设置为箭头
        #self.setCursor(QCursor(Qt.ArrowCursor))
    """
    def test(self):
        #self.timer = QTimer(self) #初始化一个定时器
        #self.timer.timeout.connect(self.test) #计时结束调用operate()方法
        #print("-")
        time = QDateTime.currentDateTime()
        # 设置系统时间的显示格式
        timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
        #print(time.toLocalTime().tm_hour)
        hour = datetime.datetime.now().strftime("%H")
        #print(hour)
        minute = datetime.datetime.now().strftime("%M")
        second = datetime.datetime.now().strftime("%S")
        #print(timeDisplay)
        if hour == '21':
            if minute == '00':
                if second == '00':
                    notification.notify(title = '十点啦！',
                                message = '屏幕边的塞西莉亚提醒你早休息~',
                                app_icon = None,
                                timeout = 5)
        

    def time(self):
        self.timer = QTimer(self) #初始化一个定时器
        self.timer.timeout.connect(self.test) #计时结束调用operate()方法
        self.timer.start(1000) #设置计时间隔并启动
    """
    '''
    def Text(self):
        #self.mylabel = QLabel(self).setText("Hello QLabel")  # 创建一个QLabel并写入文字
        #w=QWidget()
        #lab=QLabel(w)
        #lab.setGeometry(10,60,210,130)
        #lab.setText('我自横刀向天笑，去留肝胆两昆仑。222222222222222222222222222222')

        self.talkLabel = QLabel(self)
        # 对话框样式设计
        self.talkLabel.setStyleSheet("font:15pt '楷体';border-width: 1px;color:blue;")
        self.dialog = "Hello"
        self.talkLabel.setText(random.choice(self.dialog))
        self.talkLabel.setStyleSheet(
                "font: bold;"
                "font:25pt '楷体';"
                "color:white;"
                "background-color: white"
                "url(:/)"
            )
        self.talkLabel.adjustSize()

        self.talkLabel.setText("别点我")
        self.talkLabel.setStyleSheet(
                "font: bold;"
                "font:25pt '楷体';"
                "color:white;"
                "background-color: red"
                "url(:/)"
            )
        self.talkLabel.adjustSize()
    '''


if __name__ == '__main__':

    #获取系统时间
    #time = QDateTime.currentDateTime()
    #timeDisplay = time.toString('yyyy-MM-dd hh:mm:ss dddd')
    #print(timeDisplay)

    # 创建了一个QApplication对象，对象名为app，带两个参数argc,argv
    # 所有的PyQt5应用必须创建一个应用（Application）对象。sys.argv参数是一个来自命令行的参数列表。

    app = QApplication(sys.argv)
    # 窗口组件初始化
    pet = DesktopPet()
    # 1. 进入时间循环；
    # 2. wait，直到响应app可能的输入；
    # 3. QT接收和处理用户及系统交代的事件（消息），并传递到各个窗口；
    # 4. 程序遇到exit()退出时，机会返回exec()的值。
    sys.exit(app.exec_())