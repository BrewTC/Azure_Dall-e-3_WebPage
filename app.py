import os
import json
from dotenv import load_dotenv
from openai import AzureOpenAI
import streamlit as st
import base64

# 載入 .env 環境變數
load_dotenv()

# === 從 .env 讀取必要參數 ===
endpoint = os.getenv("OPENAI_API_BASE")
api_key = os.getenv("OPENAI_API_KEY")
api_version = os.getenv("OPENAI_API_VERSION", "2024-02-01")
dalle_deployment = os.getenv("DALLE_DEPLOYMENT_NAME", "dall-e-3")

# 建立 Azure OpenAI 客戶端
client = AzureOpenAI(
    api_key=api_key,
    api_version=api_version,
    azure_endpoint=endpoint,
)

# 生成圖片函數
def generate_image(prompt):
    if not prompt or prompt.strip() == "":
        st.error("🚫 無效提示詞，已取消圖片生成。")
        return None
    try:
        result = client.images.generate(
            model=dalle_deployment,
            prompt=prompt,
            n=1,
            style="vivid",
            quality="standard",
            size="1024x1024"
        )
        # 取得生成的圖片 URL
        image_url = json.loads(result.model_dump_json())['data'][0]['url']
        return image_url
    except Exception as e:
        # 判斷是否是內容政策違規
        if "content_policy_violation" in str(e).lower():
            st.error("❌ 你的提示詞違反微軟內容政策，請改寫你的提示詞。")
        else:
            st.error(f"❌ 圖片生成失敗:\n{e}")
        return None

# === Streamlit UI ===
st.set_page_config(page_title="臺大醫院雲林分院圖片生成器", page_icon="🚀", layout="wide")

# 標題
# st.title("🚀 臺大醫院雲林分院圖片生成器")
st.markdown(
    """
    <h1 style='text-align: center; font-size: 2.5em; line-height: 1.2; word-break: break-word;'>
        臺大醫院雲林分院圖片生成器
    </h1>
    """,
    unsafe_allow_html=True
)


# 響應式封面圖片
def get_base64_image(image_path):
    with open(image_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

image_base64 = get_base64_image("img/123.jpg")

st.markdown(
    f"""
    <div style="text-align: center;">
        <img src="data:image/jpeg;base64,{image_base64}" alt="封面圖片" style="width: 100%; max-width: 600px; height: auto;">
    </div>
    """,
    unsafe_allow_html=True
)


# 使用者輸入
prompt = st.text_area("請輸入想生成的提示詞 : \n", "一隻穿著太空衣的柴犬站在火星上", height=100)

# 生成圖片按鈕
if st.button("生成圖片"):
    if prompt.strip() == "":
        st.warning("⚠️ 請先輸入提示詞")
    else:
        with st.spinner("⏳ 正在生成圖片..."):
            image_url = generate_image(prompt)
            if image_url:
                # 響應式顯示生成圖片
                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        <img src="{image_url}" alt="生成圖片" style="width: 100%; max-width: 600px; height: auto;">
                        <p>🎨 生成圖片</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
                # 顯示短網址按鈕
                st.success("✅ 圖片生成完成")
                st.markdown(
                    f"""
                    <div style="text-align: center;">
                        <a href="{image_url}" target="_blank" style="color: #ffffff; background-color: #4CAF50; padding: 10px 20px; text-decoration: none; border-radius: 5px;">🔗 點擊這裡查看圖片</a>
                    </div>
                    """,
                    unsafe_allow_html=True
                )