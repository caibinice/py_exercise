import re
import requests
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import random

# 配置 Chrome 浏览器
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式（后台运行）
chrome_options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                            "like Gecko) Chrome/114.0.0.0 Safari/537.36")
chrome_options.add_argument("--disable-gpu")

# chromedriver 路径
service = Service("C:\\Program Files\\Google\\Chrome\\Application\\chromedriver-win64\\chromedriver.exe")

# 定义 POST 请求的 URL 和数据
url = "https://search.jscz.org.cn:7443/manda-app/api/app/search/v1/1f59ixu/search"
post_data = {
    "cid": "BwfvRlHMOA5OYbu44D3Dc2ubJ7kGzIYn",
    "uid": "BwfvRlHMOA5OYbu44D3Dc2ubJ7kGzIYn",
    "query": "建筑垃圾",
    "razor": "imgsearch",
    "current": 2,
    "size": 100,
    "disable_correction": False,
    "filter": [
        "view:xwzx"
    ],
    "input_type": "Input"
}

# 创建保存结果的目录
output_dir = "results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
info = []

# 发送 POST 请求
response = requests.post(url, json=post_data)
if response.status_code == 200:
    data = response.json()
    if data.get("success"):
        items = data["result"]["items"]
        for item in items:
            # 获取标题和 URL
            title = item["title"]["raw"]
            content_url = item["url"]["raw"]
            # 清理标题，移除非法文件名字符
            safe_title = re.sub(r'[\\/*?:"<>|]', "_", title)
            info.append({"title": safe_title, "content_url": content_url})

    else:
        print("请求失败，返回数据中 success 为 False")
else:
    print(f"POST 请求失败，状态码: {response.status_code}")


# def save_to_word(html_content, output_path):
#     """
#     将 HTML 内容保存为 Word 文件
#     """
#     try:
#         # 使用 BeautifulSoup 解析 HTML 内容
#         soup = BeautifulSoup(html_content, 'html.parser')
#
#         # 创建 Word 文档
#         doc = Document()
#
#         # 将 HTML 的文本内容写入 Word 文档
#         for paragraph in soup.find_all('p'):
#             doc.add_paragraph(paragraph.get_text())
#
#         # 保存 Word 文件
#         doc.save(output_path)
#         print(f"保存成功: {output_path}")
#     except Exception as e:
#         print(f"保存 Word 文件失败: {e}")


def batch_download_and_convert(url_content_list, output_dir):
    """
    批量下载 HTML 并转换为 txt 文件D
    """

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)  # 创建输出目录

    for i, subUrl in enumerate(url_content_list):
        print(f"正在处理第 {i + 101} 个链接: {subUrl['content_url']}")
        driver = webdriver.Chrome(service=service, options=chrome_options)
        try:
            driver.get(subUrl['content_url'])
            html_content = driver.page_source  # 获取页面 HTML 源代码
            if html_content:
                # 使用 BeautifulSoup 提取纯文本
                soup = BeautifulSoup(html_content, "html.parser")
                text_content = soup.get_text(separator="\n", strip=True)  # 提取纯文本内容
                # 保存到文件
                fileName = subUrl['title']
                if fileName:
                    fileName = fileName[:40] + ".txt"
                else:
                    fileName = f"text-{subUrl['content_url']}.txt"

                file_path_sub = os.path.join(output_dir, fileName)
                with open(file_path_sub, "w", encoding="utf-8") as file0:
                    file0.write(text_content)
                print(f"成功保存: {file_path_sub}")

        except Exception as e:
            print(f"处理链接 {subUrl['content_url']} 时出错: {e}")
        finally:
            driver.quit()
            time.sleep(random.uniform(15, 25))  # 随机等待


if __name__ == "__main__":
    # 示例链接列表（替换为你需要处理的链接）
    urls = [{"content_url": "http://www.zhonglou.gov.cn/html/czzl/2024/IBPAPQFQ_1008/364888.html", "title": "test1"}]

    # 输出目录
    output_dir = "output_txt_files"

    # 批量下载和转换
    batch_download_and_convert(info, output_dir)
