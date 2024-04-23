import requests
from bs4 import BeautifulSoup
import re
from collections import Counter

def extract_words_from_website(url):
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to retrieve the webpage: {url}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    # 使用正则表达式提取单词
    words = re.findall(r'\b\w+\b', text)
    return words

def filter_words(words, filter_list):
    return [word for word in words if word.lower() not in filter_list]

def main():
    # 定义要提取单词的页面URL列表
    urls = [
        
        "https://react.dev/learn/thinking-in-react",
        "https://react.dev/learn/your-first-component",
        "https://react.dev/learn/importing-and-exporting-components",
        "https://react.dev/learn/adding-interactivity",
        "https://react.dev/learn/lifecycle-of-reactive-effects",
        "https://react.dev/learn/escape-hatches",
        "https://react.dev/learn/tutorial-tic-tac-toe",
        "https://react.dev/learn/reusing-logic-with-custom-hooks",
        "https://react.dev/learn/render-and-commit",
        "https://react.dev/learn/referencing-values-with-refs",
        "https://react.dev/learn/passing-data-deeply-with-context",
        "https://react.dev/learn/updating-objects-in-state",
        "https://react.dev/learn",
        "https://react.dev/learn/synchronizing-with-effects",
        "https://react.dev/learn/removing-effect-dependencies",
        "https://react.dev/learn/understanding-your-ui-as-a-tree",
        "https://react.dev/learn/managing-state",
        "https://react.dev/learn/passing-props-to-a-component",
        "https://react.dev/learn/editor-setup",
        "https://react.dev/learn/javascript-in-jsx-with-curly-braces",
        "https://react.dev/learn/scaling-up-with-reducer-and-context",
        "https://react.dev/learn/typescript",
        "https://react.dev/learn/reacting-to-input-with-state",
        "https://react.dev/learn/updating-arrays-in-state",
        "https://react.dev/learn/choosing-the-state-structure",
        "https://react.dev/learn/sharing-state-between-components",
        "https://react.dev/learn/state-as-a-snapshot",
        "https://react.dev/learn/you-might-not-need-an-effect",
        "https://react.dev/learn/keeping-components-pure",
        "https://react.dev/learn/extracting-state-logic-into-a-reducer",
        "https://react.dev/learn/writing-markup-with-jsx",
        "https://react.dev/learn/responding-to-events",
        "https://react.dev/learn/manipulating-the-dom-with-refs",
        "https://react.dev/learn/add-react-to-an-existing-project",
        "https://react.dev/learn/separating-events-from-effects",
        "https://react.dev/learn/describing-the-ui",
        "https://react.dev/learn/preserving-and-resetting-state",
        "https://react.dev/learn/installation",
        "https://react.dev/learn/rendering-lists",
        "https://react.dev/learn/start-a-new-react-project",
        "https://react.dev/learn/state-a-components-memory",
        "https://react.dev/learn/conditional-rendering",
        "https://react.dev/learn/react-developer-tools",
        "https://react.dev/learn/queueing-a-series-of-state-updates"
    ]

    # 读取过滤单词列表
    with open('/Users/wesley/Desktop/杂七杂八/自学代码练习/过滤React单词/demotxt.txt', 'r') as f:
        filter_list = [line.strip().lower() for line in f]

    all_words = []

    for url in urls:
        words = extract_words_from_website(url)
        filtered_words = filter_words(words, filter_list)
        all_words.extend(filtered_words)

    # 使用Counter统计单词出现的次数
    word_counts = Counter(all_words)

    # 按照出现的频率从高到低排序
    sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # 打印提取的单词和它们的频率
    for word, count in sorted_words:
        if count>1:
            print(f"{word}: {count}")
    with open('/Users/wesley/Desktop/杂七杂八/自学代码练习/过滤React单词/filtered_words.txt', 'w') as output_file:
        for word, count in sorted_words:
            if count > 1 and word.isalpha() and len(word) > 2:
                output_file.write(f"{word}: {count}\n")

    print("Filtered words saved to filtered_words.txt")
if __name__ == "__main__":
    main()
