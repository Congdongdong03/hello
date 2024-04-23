import re

# 打开原始txt文件
with open('/Users/wesley/Desktop/杂七杂八/自学代码练习/过滤React单词/filtered_words.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# 使用正则表达式替换所有数字、冒号、空格为一个换行符
filtered_content = re.sub(r'\d+|:|\s+', '\n', content)

# 将过滤后的内容写入新的txt文件
with open('filtered_no_numbers.txt', 'w', encoding='utf-8') as f:
    f.write(filtered_content)
