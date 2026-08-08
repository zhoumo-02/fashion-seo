import os
from datetime import datetime


# =========================
# 配置
# =========================

keyword_file = "keywords.txt"

template_file = "template.html"

article_dir = "../articles"

article_list_file = "../articles.html"



# =========================
# 读取关键词
# =========================

with open(
    keyword_file,
    "r",
    encoding="utf-8"
) as f:

    keywords = [
        line.strip()
        for line in f.readlines()
        if line.strip()
    ]


print("关键词数量:", len(keywords))



# =========================
# 读取模板
# =========================

with open(
    template_file,
    "r",
    encoding="utf-8"
) as f:

    template = f.read()



# =========================
# 创建文章目录
# =========================

os.makedirs(
    article_dir,
    exist_ok=True
)



today = datetime.now().strftime(
    "%Y-%m-%d"
)



article_links = []



# =========================
# 生成文章
# =========================

for index, keyword in enumerate(keywords):


    filename = keyword + ".html"


    filepath = os.path.join(
        article_dir,
        filename
    )



    # -------------------------
    # 生成相关文章
    # -------------------------

    related = ""

    count = 0


    for item in keywords:


        if item != keyword:


            related += f"""
<li>
<a href="{item}.html">
{item}
</a>
</li>
"""


            count += 1


            if count >= 3:

                break



    # -------------------------
    # 替换模板
    # -------------------------

    html = template



    html = html.replace(
        "{title}",
        keyword
    )


    html = html.replace(
        "{date}",
        today
    )


    html = html.replace(
        "{related}",
        related
    )



    # -------------------------
    # 写入HTML
    # -------------------------

    with open(
        filepath,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(html)



    print(
        "生成:",
        filepath
    )



    # -------------------------
    # 文章列表
    # -------------------------

    article_links.append(
        f"""
<li>
<a href="articles/{filename}">
{keyword}
</a>
</li>
"""
    )



# =========================
# 自动生成 articles.html
# =========================


articles_html = f"""
<!DOCTYPE html>

<html lang="zh-CN">


<head>

<meta charset="UTF-8">


<title>
腾龙公司文章中心
</title>


<meta name="description"
content="
腾龙公司企业介绍、品牌资讯、服务内容文章中心。
">


</head>



<body>


<h1>
腾龙公司文章中心
</h1>



<ul>

{''.join(article_links)}

</ul>



<br>


<a href="index.html">
返回首页
</a>



</body>


</html>
"""



with open(
    article_list_file,
    "w",
    encoding="utf-8"
) as f:

    f.write(
        articles_html
    )



print("======================")

print(
    "articles.html生成完成"
)


print(
    "生成文章数量:",
    len(keywords)
)
