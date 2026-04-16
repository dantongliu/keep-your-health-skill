import pdfplumber
import json
import os

def parse_dantong_report(pdf_path):
    # 此脚本重点在于测试 pdfplumber 的提取能力
    extracted_data = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                extracted_data.append(text)
    
    # 简易处理：将内容保存为 txt 供后续分析
    output_path = "/Users/liudantong/WorkBuddy/身体健康/members/dantong/reports/extracted_raw.txt"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(extracted_data))
    
    return output_path

if __name__ == "__main__":
    report_path = "/Users/liudantong/WorkBuddy/身体健康/202511-体检报告-丹彤.pdf"
    if os.path.exists(report_path):
        result = parse_dantong_report(report_path)
        print(f"解析完成，原始文本已保存至: {result}")
    else:
        print("未找到指定的 PDF 文件，请确认路径。")
