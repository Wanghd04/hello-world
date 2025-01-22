import requests
from bs4 import BeautifulSoup
import time
from fake_useragent import UserAgent

def scrape_google():
    try:
        # 创建随机 User-Agent
        ua = UserAgent()
        headers = {
            'User-Agent': ua.random
        }
        
        # 发送 GET 请求到 Google
        url = 'https://www.google.com'
        response = requests.get(url, headers=headers, timeout=10)
        
        # 检查响应状态
        if response.status_code == 200:
            # 使用 BeautifulSoup 解析页面
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # 获取页面标题
            title = soup.title.string
            print(f'页面标题: {title}')
            
            # 获取所有链接
            links = soup.find_all('a')
            print('\n找到的链接:')
            for link in links:
                href = link.get('href')
                if href and not href.startswith('#'):
                    print(href)
            
            # 保存页面内容到文件
            with open('google_page.html', 'w', encoding='utf-8') as f:
                f.write(response.text)
            print('\n页面内容已保存到 google_page.html')
            
        else:
            print(f'请求失败，状态码: {response.status_code}')
            
    except requests.exceptions.RequestException as e:
        print(f'发生错误: {e}')

if __name__ == '__main__':
    print('开始爬取 Google 首页...')
    scrape_google()
