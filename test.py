from ai.qwen_client import QwenClient


def main():
    print("正在测试 API 连接...")

    # 1. 初始化客户端
    client = QwenClient()

    # 2. 构造测试消息
    messages = [
        {"role": "system", "content": "你是一个只会输出 JSON 的测试助手。"},
        {"role": "user", "content": "请告诉我你的名字，并以 JSON 格式返回，例如 {'name': 'Qwen'}"}
    ]

    # 3. 发送请求
    print("\n发送请求中...")
    response = client.query(messages, json_mode=True)

    # 4. 打印结果
    print(f"\n最终结果类型: {type(response)}")
    print(f"最终结果内容: {response}")


if __name__ == "__main__":
    main()