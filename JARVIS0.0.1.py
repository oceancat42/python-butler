from datetime import datetime
import pyttsx3  #文本转语音第三方库
import requests
import random

# 定义计算器函数
def calculator(expression=None):
    # 如果没有传入表达式，就提示用户输入
    if expression is None:
        expression = input("请输入表达式:")

    # 处理中文运算符
    expression = expression.replace("加", "+").replace("减", "-").replace("乘", "*").replace("除", "/")
    # 自动补空格
    for op in ["+", "-", "*", "/"]:
        expression = expression.replace(op, f" {op} ")
    parts = expression.split()

    # 分割表达式为数字和运算符
    parts = expression.split()
    if len(parts) != 3:
        print("表达格式错误，请使用类似‘3+5’的格式")
        return

    a_str, op, b_str = parts  # 序列解包

    # 尝试转换为数字
    try:
        a = float(a_str)
        b = float(b_str)
    except ValueError:
        print("请输入有效的数字!")
        return

    # 计算并打印结果
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "/":
        if b == 0:
            print("错误：除数不能为零！")
            return
        result = a / b
    else:
        print("无效的运算符，请使用+,-,*,/")
        return

    print(f"{a} {op} {b} = {result}")


# 定义时间函数
def tell_time():
    #获取当前时间
    now = datetime.now()
    time_str = f"现在时间是{now.hour}点{now.minute}分{now.second}秒"

    #打印到屏幕
    print(f"🕒{time_str}")

    #语音播报
    engine = pyttsx3.init()
    engine.say(time_str)
    engine.runAndWait()


# 定义天气函数
def check_weather():
    print("天气模块开发中...")

# 定义表情函数
def emotion_mode():
    #颜文字字典
    emoticon_dict = {
        "开心": ['(´∀｀*)', '(๑´ڡ`๑)', '٩(◕‿◕｡)۶'],
        "伤心": ['(;_;)', '(Ｔ▽Ｔ)'],
        "震惊": ['Σ(°△°|||)︴', '(⊙ˍ⊙)']
    }
    #新增疑惑表情
    confused_emotion = "没有这个表情(￣.￣)?"
    #用户输入完整句子
    shuru = input("表情模块启动！\n请输入想获得的表情")


    found_emotion = None
    found = []  # 创建一个空列表，用来存放找到的所有情绪词
    for emotion in emoticon_dict:  # 遍历字典里每一个情绪词
        if emotion in shuru:  # 检查当前的词是否在用户的输入中
            found.append(emotion)  # 如果找到了，就把他放到found列表里

    if found:  # 判断是否找到了情绪词，#如果found列表不为空
        for em in found:  # 遍历found列表中每一个情绪词
            print(random.choice(emoticon_dict[em]))
    else:
        print(confused_emotion)


# 主程序
print("您好！我是您的python管家。")

while True:

    user_input = input("您有什么吩咐?")

    if "天气" in user_input:
        check_weather()
    elif "计算" in user_input or any(op in user_input for op in ["+", "-", "*", "/"]):
        print("计算器已启动")
        if user_input.startswith("计算"):
            calculator()
        else:
            calculator(user_input)
    elif "时间" in user_input:
        tell_time()
    elif "表情" in user_input:
        emotion_mode()
    elif "退出" in user_input or "再见" in user_input or "结束" in user_input:
        print("再见，主人！")
        break
    else:
        print("抱歉，我还没学过这个功能")
