import json
import os

def run_skill(member_name):
    if member_name not in ["刘丹彤", "陈磊"]:
        return f"系统提示：未找到成员 {member_name}，请检查名字是否输入正确。"
    
    # 读取指标数据
    with open(f"/Users/liudantong/WorkBuddy/身体健康/members/dantong/timeline.json", "r") as f:
        data = json.load(f)
    
    # 模拟情感化反馈
    if data.get("TSH", 0) < 0.35:
        return f"【健康关怀】亲爱的{member_name}，检测到您的 TSH 指标 (0.04) 偏低。请注意，这可能是药物调节的结果。建议结合甲状腺彩超复查，记得保持好心情，这周多休息哦。"
    
    return "解析完成，暂未发现严重指标异常。"

if __name__ == "__main__":
    print(run_skill("刘丹彤"))
