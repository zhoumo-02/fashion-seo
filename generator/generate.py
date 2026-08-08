import os
from datetime import datetime


BASE_URL = "https://zhoumo-02.github.io/fashion-Tips-and-Tricks"


keyword_file = "keywords.txt"

output_dir = "../articles"


os.makedirs(output_dir, exist_ok=True)


with open(keyword_file,"r",encoding="utf-8") as f:
    keywords = [
        x.strip()
        for x in f.readlines()
        if x.strip()
    ]


for keyword in keywords:

    filename = keyword + ".html"

    filepath = os.path.join(
        output_dir,
        filename
    )


    html = f"""
<!DOCTYPE html>

<html>

<head>

<meta charset="UTF-8">

<title>{keyword}</title>


<meta name="description"
content="{keyword}相关介绍和详细说明">


</head>


<body>


<h1>
{keyword}
</h1>


<p>
本文介绍{keyword}相关内容，
提供详细说明、操作流程和常见问题。
</p>


<h2>
常见问题
</h2>


<p>
用户可以查看相关信息。
</p>


<h2>
相关文章
</h2>


<a href="../index.html">
返回首页
</a>


</body>


</html>
"""


    with open(filepath,"w",encoding="utf-8") as f:
        f.write(html)


print(
    "生成完成:",
    len(keywords),
    "篇文章"
)
