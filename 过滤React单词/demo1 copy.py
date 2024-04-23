import requests
from bs4 import BeautifulSoup
import re

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

    all_words = []

    for url in urls:
        words = extract_words_from_website(url)
        all_words.extend(words)

    # 去重并排序
    unique_words = sorted(set(all_words))

    # 创建或打开一个.txt文件
    with open("extracted_words.txt", "w", encoding="utf-8") as file:
        # 将单词写入文件
        for word in unique_words:
            file.write(word + "\n")

    print("提取的单词已保存到 extracted_words.txt 文件中")

if __name__ == "__main__":
    main()
