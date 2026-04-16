import json

def get_demo_preview():
    demo_data = {
        "member": "刘丹彤 (示例)",
        "report_date": "2026-04-15",
        "key_findings": {
            "normal": ["血压 110/70", "空腹血糖 4.8"],
            "abnormal": [
                {"indicator": "总胆固醇", "value": "5.8", "unit": "mmol/L", "ref": "< 5.2", "note": "轻度偏高，注意低脂饮食"},
                {"indicator": "低密度脂蛋白", "value": "3.5", "unit": "mmol/L", "ref": "< 3.37", "note": "需加强有氧运动"}
            ]
        }
    }
    return json.dumps(demo_data, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    print("=== 首次录入演示 (Demo) ===")
    print("当你上传体检报告后，系统会自动抓取关键指标：")
    print(get_demo_preview())
    print("\n[系统提示]：请确认上述异常指标是否需要录入档案。")
