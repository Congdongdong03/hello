import re

def is_english_word(word):
    # 使用正则表达式检查是否为英文单词
    return bool(re.match('^[a-zA-Z]{2,}$', word))

def filter_text_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as f_in:
            lines = f_in.readlines()
    except FileNotFoundError:
        print(f"Error: {input_file} not found.")
        return
    except Exception as e:
        print(f"Error reading {input_file}: {e}")
        return

    print(f"Original lines:")
    for line in lines:
        print(line.strip())

    # 过滤出单词是英文且长度大于等于2的行
    filtered_lines = [line.strip() for line in lines if all(is_english_word(word) for word in line.split())]
    print(f"\nFiltered lines:")
    for line in filtered_lines:
        print(line)

    if not filtered_lines:
        print("\nNo lines left after filtering.")
        return

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write('\n'.join(filtered_lines))

    print(f"\nFiltered lines saved to {output_file}")

if __name__ == '__main__':
    input_file = 'b.txt'  # 输入的txt文件名
    output_file = 'output.txt'  # 输出的txt文件名

    filter_text_file(input_file, output_file)