# Azure_Dall-e-3-WebPage
# 臺大醫院雲林分院圖片生成器
![](/img/123.jpg)
這是一個使用 [Azure OpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/) 與 [DALL·E 3 模型](https://openai.com/dall-e) 所建立的圖片生成器，前端介面採用 [Streamlit](https://streamlit.io/) 開發，使用者可以輸入文字提示詞（Prompt），並生成高品質的圖片。

---

## 🚀 功能介紹

- ✅ 使用 Azure OpenAI DALL·E 3 生成圖片
- ✅ 自動處理無效或違規提示詞
- ✅ Streamlit 界面簡潔好用
- ✅ 支援本地封面圖片
- ✅ 響應式圖片展示與下載連結

---

## 🧑‍💻 安裝與使用教學

### 1️⃣ 安裝相依套件

請先確保你已安裝 Python 3.9 或以上版本，然後安裝相依套件：

```bash
pip install -r requirements.txt
```
建議 requirements.txt 檔案內容如下：

```bash
streamlit
python-dotenv
openai>=1.0.0
```
### 2️⃣ 設定 .env 環境變數
請在專案根目錄建立 .env 檔案，填入以下內容：

```bash
OPENAI_API_BASE=https://YOUR_RESOURCE_NAME.openai.azure.com/
OPENAI_API_KEY=your_azure_openai_key
OPENAI_API_VERSION=2024-02-01
DALLE_DEPLOYMENT_NAME=dall-e-3
```
請將 YOUR_RESOURCE_NAME 與 your_azure_openai_key 替換成你在 Azure OpenAI 中的實際值。

### 3️⃣ 啟動應用程式
在終端機輸入以下指令：
```bash
streamlit run app.py
```
預設會在本地瀏覽器開啟：http://localhost:8501


### ⚠️ 注意事項
- 圖片生成需要連接 Azure OpenAI API，請確認網路可連線，且金鑰與部署名稱正確。

- 若提示詞違反內容政策（如暴力、色情等），將無法生成圖片，請改寫提示內容。

- 若圖片未成功顯示，請確認 image_url 有回傳並可正常存取。

### 📄 授權條款
本專案僅作為學術與展示用途。圖片產出請遵守 Azure OpenAI 使用條款。

### 🙋‍♀️ 聯絡與貢獻
作者：MattChiang

部落格：[麥特資料探險](https://mattdataadventures.com/)

若你對此專案有想法或改善建議，歡迎提交 PR 或 Issue 讓我們一起讓專案變得更好！📬
=======
