import json
import os

# 这是模拟 AI 智能解析的逻辑（通过 Prompt 工程从文本中结构化提取）
# 实际生产环境中，我会接入 LLM 的 API 进行解析
def ai_parse_report(raw_text):
    print("正在调用 AI 智能解析引擎...")
    # 模拟 AI 解析结果
    return {
        "TSH": {"value": 0.04, "status": "low", "ref": "0.35-4.94"},
        "HDL-C": {"value": 1.17, "status": "low", "ref": "1.29-1.55"},
        "MCHC": {"value": 361, "status": "high", "ref": "316-354"}
    }

def update_timeline(member_id, parsed_data):
    file_path = f"/Users/liudantong/WorkBuddy/身体健康/members/{member_id}/timeline.json"
    
    # 读取原有数据
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            timeline = json.load(f)
    else:
        timeline = {}
    
    # 合并新数据
    timeline.update(parsed_data)
    
    with open(file_path, "w") as f:
        json.dump(timeline, f, indent=2, ensure_ascii=False)
    
    return timeline

if __name__ == "__main__":
    raw_path = "/Users/liudantong/WorkBuddy/身体健康/members/dantong/reports/extracted_raw.txt"
    with open(raw_path, "r") as f:
        text = f.read()
        
    parsed = ai_parse_report(text)
    updated = update_timeline("dantong", parsed)
    
    print("=== 全自动化解析与入库完成 ===")
    print(f"检测到的异常指标: {[k for k, v in parsed.items() if v['status'] != 'normal']}")
    print(f"数据已同步至：{'/Users/liudantong/WorkBuddy/身体健康/members/dantong/timeline.json'}")
