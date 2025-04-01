import streamlit as st
from PIL import Image
import base64
from io import BytesIO
import numpy as np
import time
import cv2
def 获取背景图片_base64(img):
    """将PIL图片转换为base64编码"""
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def 设置页面背景(img_base64):
    """设置页面背景图片"""
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{img_base64}");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def 创建生日背景():
    """创建带有彩色背景的图片"""
    # 创建渐变背景
    width, height = 800, 600
    image = np.zeros((height, width, 3), dtype=np.uint8)
    
    # 创建粉色渐变背景
    for i in range(height):
        factor = i / height
        r = int(255 - factor * 50)
        g = int(192 - factor * 100)
        b = int(203 - factor * 50)
        image[i, :] = [r, g, b]
    
    # 添加一些随机彩色气球效果
    for _ in range(50):
        x = np.random.randint(0, width)
        y = np.random.randint(0, height)
        radius = np.random.randint(5, 20)
        color = np.random.randint(0, 255, 3)
        cv2.circle(image, (x, y), radius, color.tolist(), -1)
    
    return Image.fromarray(image)

def 主页面():
    """显示生日祝福主页面"""
    st.markdown(
        """
        <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
            <div style="text-align: center; background-color: rgba(255, 255, 255, 0.7); padding: 30px; border-radius: 15px; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);">
                <h1 style="font-size: 50px; color: #FF69B4; text-shadow: 2px 2px 4px #000000;">露露生日快乐！</h1>
                <h2 style="font-size: 30px; color: #FF1493;">祝你天天开心，年年有今日！</h2>
                <p style="font-size: 20px; color: #8B008B;">愿你的生日充满欢乐和惊喜！</p>
                <div style="margin-top: 20px;">
                    <span style="font-size: 40px;">🎂</span>
                    <span style="font-size: 40px;">🎁</span>
                    <span style="font-size: 40px;">🎉</span>
                    <span style="font-size: 40px;">🎈</span>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

def 显示气球动画():
    """显示飘动的气球动画"""
    st.markdown(
        """
        <style>
        @keyframes float {
            0% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(5deg); }
            100% { transform: translateY(0) rotate(0deg); }
        }
        
        .balloon {
            position: fixed;
            font-size: 50px;
            animation: float 3s ease-in-out infinite;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # 添加多个气球
    for i in range(10):
        delay = i * 0.3
        left = i * 10
        st.markdown(
            f"""
            <div class="balloon" style="left: {left}%; animation-delay: {delay}s;">🎈</div>
            """,
            unsafe_allow_html=True
        )

def 主函数():
    """主函数"""
    st.set_page_config(
        page_title="露露生日快乐",
        page_icon="🎂",
        layout="wide"
    )
    
    # 尝试导入cv2，如果不可用则使用纯色背景
    try:
        import cv2
        背景图片 = 创建生日背景()
    except ImportError:
        # 创建简单的粉色背景
        背景图片 = Image.new("RGB", (800, 600), (255, 192, 203))
    
    背景图片_base64 = 获取背景图片_base64(背景图片)
    设置页面背景(背景图片_base64)
    
    显示气球动画()
    主页面()
    
    # 显示分享信息
    st.sidebar.markdown("### 分享这个生日祝福")
    st.sidebar.info("复制浏览器地址栏中的URL分享给朋友们！")
    
    # 添加音乐播放器（可选）
    st.sidebar.markdown("### 生日歌")
    st.sidebar.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3", format="audio/mp3")

if __name__ == "__main__":
    主函数()