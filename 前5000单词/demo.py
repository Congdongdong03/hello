def filter_words(file_a, file_b, output_file):
    with open(file_a, 'r', encoding='utf-8') as f_a:
        words_a = set(f_a.read().split())

    with open(file_b, 'r', encoding='utf-8') as f_b:
        words_b = f_b.read()

    # 使用集合操作过滤掉a文本中的单词
    filtered_words_b = '\n'.join(word for word in words_b.split() if word not in words_a)

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write(filtered_words_b)

# 文件路径
file_a_path = '/Users/wesley/Desktop/杂七杂八/自学代码练习/常用5000.txt'
file_b_path = '/Users/wesley/Desktop/杂七杂八/自学代码练习/Longman Communication 3000 (1).txt'
output_file_path = 'filtered_b.txt'

# 调用函数进行过滤
filter_words(file_a_path, file_b_path, output_file_path)

print("文本过滤完成!")
