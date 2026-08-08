import os
from datetime import datetime


# 你的 GitHub Pages 地址
domain = "https://zhoumo-02.github.io/fashion-seo"


# 网站目录
site_dir = "../"


urls = []


# 查找所有 html
for root, dirs, files in os.walk(site_dir):

    for file in files:

        if file.endswith(".html"):

            path = os.path.join(root, file)

            # 去掉 ../
            path = path.replace("../", "")

            # 首页处理
            if path == "index.html":
                url = domain + "/"
            else:
                url = domain + "/" + path


            urls.append(url)



# 生成 sitemap
xml = """<?xml version="1.0" encoding="UTF-8"?>

<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">

%s

</urlset>
"""


items = ""


for url in urls:

    items += f"""
<url>
    <loc>{url}</loc>
    <lastmod>{datetime.now().strftime('%Y-%m-%d')}</lastmod>
</url>

"""


with open(
    "../sitemap.xml",
    "w",
    encoding="utf-8"
) as f:

    f.write(
        xml % items
    )


print(
    "sitemap.xml生成完成，共",
    len(urls),
    "个页面"
)
