from openai import OpenAI
import config
import json
import sys


class QwenClient:
    def __init__(self):
        print(f"[*] 初始化 QwenClient (Model: {config.LLM_MODEL})...")
        self.client = OpenAI(
            api_key=config.DASHSCOPE_API_KEY,
            base_url=config.LLM_API_BASE,
        )
        self.model = config.LLM_MODEL

    def query(self, messages, json_mode=True):
        """
        发送请求给 LLM。
        """
        try:
            # 移除 enable_thinking，依靠 System Prompt 引导思考
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=True
            )

            full_content = []

            # print("\n" + "=" * 20 + " AI 生成中 " + "=" * 20)

            for chunk in completion:
                delta = chunk.choices[0].delta
                if hasattr(delta, "content") and delta.content:
                    full_content.append(delta.content)
                    # print(delta.content, end="", flush=True) # 调试时可开启

            # print("\n" + "=" * 50)

            response_text = "".join(full_content).strip()

            if json_mode:
                return self._parse_json(response_text)
            return response_text

        except Exception as e:
            print(f"\n[Error] LLM 调用失败: {e}")
            # 返回空字典防止崩溃
            return {}

    def _parse_json(self, text):
        """尝试从文本中清洗并解析 JSON"""
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            try:
                start = text.find("```json")
                if start != -1:
                    end = text.find("```", start + 7)
                    if end != -1:
                        json_str = text[start + 7: end].strip()
                        return json.loads(json_str)

                start = text.find("{")
                end = text.rfind("}")
                if start != -1 and end != -1:
                    json_str = text[start: end + 1].strip()
                    return json.loads(json_str)

            except Exception:
                pass

            print(f"[Warning] JSON 解析失败，返回原始文本片段。\n{text[:50]}...")
            return {}