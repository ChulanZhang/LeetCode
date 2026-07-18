# -*- coding: utf-8 -*-
import os
import sys
import subprocess

# 将当前目录和根目录加入 sys.path
SCRATCH_DIR = os.path.dirname(os.path.abspath(__file__))
WORKSPACE_ROOT = os.path.dirname(SCRATCH_DIR)
sys.path.append(SCRATCH_DIR)

# 动态计算本地 file:/// 路径头以适配任意移动后的路径
FILE_URL_ROOT = "file:///" + WORKSPACE_ROOT.replace("\\", "/")

import plan_database

def clean_filename(name):
    return name.lower().replace(" ", "_").replace("-", "_").replace("(", "").replace(")", "").replace(".", "")

def generate_markdown_plan():
    print("Step 1: Generating Markdown version of the plan...")
    plan_dir = os.path.join(WORKSPACE_ROOT, "sprint_plan")
    os.makedirs(plan_dir, exist_ok=True)
    
    md_path = os.path.join(plan_dir, "30_day_sprint_plan.md")
    
    content = []
    content.append("# 30-Day Algorithm Sprint Plan (Customized for MLSys PhDs)\n")
    content.append("> **Coach's Note**: Specially customized for MLSys backgrounds. While strengthening core algorithms like two pointers, binary search, trees, and graphs, we deeply integrate systems-level mechanics (LRU/LFU cache, ring buffers, concurrency, bit quantization) to build high-performance whiteboard muscle memory.\n")
    content.append("## 30-Day Panorama Roadmap\n")
    
    # Overview Table
    content.append("| Phase | Day | Core Theme | Daily Volume |")
    content.append("|---|---|---|---|")
    for idx, phase in enumerate(plan_database.PHASES):
        phase_name = phase["name"]
        for day, info in phase["days"].items():
            content.append(f"| {phase_name.split(':')[0]} | Day {day:02d} | {info['theme']} | {len(info['problems'])} Qs |")
    content.append("\n---\n")
    
    # Detailed Content
    for phase in plan_database.PHASES:
        content.append(f"## {phase['name']}")
        content.append(f"**Phase Target**: {phase['target']}\n")
        
        for day, info in sorted(phase["days"].items()):
            content.append(f"### 📅 Day {day:02d} - {info['theme']}\n")
            
            for prob in info["problems"]:
                lc_url = f"https://leetcode.com/problems/{clean_filename(prob['name']).replace('_', '-')}/"
                template_name = f"day{day:02d}_q{int(prob['id']):03d}_{clean_filename(prob['name'])}.py"
                content.append(f"- **LeetCode {prob['id']}**: [{prob['name']}]({lc_url}) | **[{prob['difficulty']}]**")
                content.append(f"  - 🔑 **Key Points**: {prob['key']}")
                content.append(f"  - 💻 **Local Template**: [sprint_plan/templates/{template_name}]({FILE_URL_ROOT}/sprint_plan/templates/{template_name})")
                content.append(f"  - 🧠 **MLSys Connection**: {prob['systems_note']}\n")
            content.append("---")
            
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
    print(f"  Markdown plan successfully written to {md_path}")

def generate_templates():
    print("Step 2: Generating Python template stubs for all 90+ questions...")
    templates_dir = os.path.join(WORKSPACE_ROOT, "sprint_plan", "templates")
    os.makedirs(templates_dir, exist_ok=True)
    
    count = 0
    for phase in plan_database.PHASES:
        for day, info in phase["days"].items():
            for prob in info["problems"]:
                filename = f"day{day:02d}_q{int(prob['id']):03d}_{clean_filename(prob['name'])}.py"
                filepath = os.path.join(templates_dir, filename)
                
                template_content = f"""# -*- coding: utf-8 -*-
# LeetCode {prob['id']} - {prob['name']} ({prob['difficulty']})
# Key Points: {prob['key']}
#
# MLSys System/Low-Level Mapping:
# {prob['systems_note']}
#
# ==========================================
# 🧠 Interview Review Area
# (After getting Accepted on LeetCode web, paste your code and write comments below)
# ==========================================
# 1. Where did you get stuck or how long did you spend debugging?
# 
# 2. Time/Space Complexity Derivation & Memory Locality Analysis:
# 
# 3. Edge Cases & Trap Test Cases:
# 
# ==========================================

class Solution:
    # TODO: Paste your Accepted code here
    pass
"""
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(template_content)
                count += 1
                
    print(f"  Successfully created {count} template stub files in {templates_dir}")

def generate_html_plan():
    print("Step 3: Compiling study guide to HTML for PDF rendering...")
    plan_dir = os.path.join(WORKSPACE_ROOT, "sprint_plan")
    html_path = os.path.join(plan_dir, "30_day_sprint_plan.html")
    
    html_header = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>30-Day Algorithm Whiteboard Sprint Plan (MLSys PhD Exclusive)</title>
    <style>
        body {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            line-height: 1.6;
            color: #333333;
            max-width: 960px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: #fafafa;
        }
        h1 {
            text-align: center;
            font-size: 32px;
            color: #1a1a1a;
            margin-bottom: 5px;
            font-weight: 800;
            background: linear-gradient(120deg, #1e3c72 0%, #2a5298 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .subtitle {
            text-align: center;
            font-size: 16px;
            color: #666;
            margin-bottom: 40px;
        }
        .phase-card {
            background: #ffffff;
            border-radius: 12px;
            padding: 24px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.05);
            border-left: 6px solid #1e3c72;
        }
        .phase-title {
            font-size: 22px;
            color: #1e3c72;
            margin-top: 0;
            margin-bottom: 10px;
            font-weight: 700;
        }
        .phase-target {
            background-color: #f0f4f8;
            padding: 12px 16px;
            border-radius: 8px;
            font-size: 14px;
            color: #2c5282;
            margin-bottom: 20px;
        }
        .day-section {
            margin-top: 25px;
            border-top: 1px solid #eef2f6;
            padding-top: 20px;
        }
        .day-title {
            font-size: 18px;
            color: #2d3748;
            margin-top: 0;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
        }
        .day-badge {
            background: #2a5298;
            color: white;
            padding: 2px 10px;
            border-radius: 20px;
            font-size: 12px;
            margin-right: 10px;
            font-weight: bold;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-bottom: 15px;
        }
        th, td {
            text-align: left;
            padding: 12px;
            font-size: 14px;
            border-bottom: 1px solid #eef2f6;
        }
        th {
            background-color: #f7fafc;
            color: #4a5568;
            font-weight: 600;
        }
        .difficulty-Easy { color: #2f855a; font-weight: bold; }
        .difficulty-Medium { color: #dd6b20; font-weight: bold; }
        .difficulty-Hard { color: #e53e3e; font-weight: bold; }
        .systems-box {
            font-size: 12.5px;
            background: #fffaf0;
            border-left: 3px solid #dd6b20;
            padding: 8px 12px;
            margin-top: 5px;
            color: #7b341e;
            border-radius: 0 4px 4px 0;
        }
        .page-break {
            page-break-after: always;
        }
    </style>
</head>
<body>
    <h1>30-Day Algorithm Whiteboard Sprint Plan</h1>
    <div class="subtitle">Tailored for MLSys PhDs & Low-Level Hardware Systems Mapping</div>
"""
    
    html_body = []
    for p_idx, phase in enumerate(plan_database.PHASES):
        html_body.append(f'<div class="phase-card">')
        html_body.append(f'  <div class="phase-title">{phase["name"]}</div>')
        html_body.append(f'  <div class="phase-target"><strong>Phase Target: </strong>{phase["target"]}</div>')
        
        for day, info in sorted(phase["days"].items()):
            html_body.append(f'  <div class="day-section">')
            html_body.append(f'    <div class="day-title"><span class="day-badge">Day {day:02d}</span> {info["theme"]}</div>')
            html_body.append(f'    <table>')
            html_body.append(f'      <thead>')
            html_body.append(f'        <tr>')
            html_body.append(f'          <th style="width: 10%;">ID</th>')
            html_body.append(f'          <th style="width: 30%;">Problem</th>')
            html_body.append(f'          <th style="width: 15%;">Difficulty</th>')
            html_body.append(f'          <th style="width: 45%;">Key Points & MLSys Low-Level Systems Mapping</th>')
            html_body.append(f'        </tr>')
            html_body.append(f'      </thead>')
            html_body.append(f'      <tbody>')
            
            for prob in info["problems"]:
                html_body.append(f'        <tr>')
                html_body.append(f'          <td>{prob["id"]}</td>')
                html_body.append(f'          <td><strong>{prob["name"]}</strong></td>')
                html_body.append(f'          <td><span class="difficulty-{prob["difficulty"]}">{prob["difficulty"]}</span></td>')
                html_body.append(f'          <td>')
                html_body.append(f'            <div><strong>Key Points: </strong>{prob["key"]}</div>')
                html_body.append(f'            <div class="systems-box">⚡ <strong>MLSys Connection: </strong>{prob["systems_note"]}</div>')
                html_body.append(f'          </td>')
                html_body.append(f'        </tr>')
                
            html_body.append(f'      </tbody>')
            html_body.append(f'    </table>')
            html_body.append(f'  </div>')
            
        html_body.append(f'</div>')
        # 给各 Phase 之间强制加分页，保证 PDF 打印不拥挤
        if p_idx < len(plan_database.PHASES) - 1:
            html_body.append('<div class="page-break"></div>')
            
    html_footer = """
</body>
</html>
"""
    
    full_html = html_header + "\n".join(html_body) + html_footer
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"  HTML compilation done at {html_path}")

def render_pdf():
    print("Step 4: Attempting to render HTML to PDF via Edge Headless...")
    edge_paths = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"
    ]
    
    edge_exec = None
    for path in edge_paths:
        if os.path.exists(path):
            edge_exec = path
            break
            
    if not edge_exec:
        print("  WARNING: Could not find msedge.exe in default Windows directories. PDF cannot be rendered automatically.")
        return
        
    print(f"  Found Edge executable: {edge_exec}")
    html_path = os.path.join(WORKSPACE_ROOT, "sprint_plan", "30_day_sprint_plan.html")
    pdf_path = os.path.join(WORKSPACE_ROOT, "30_day_sprint_plan.pdf")
    
    cmd = [
        edge_exec,
        "--headless",
        "--disable-gpu",
        f"--print-to-pdf={pdf_path}",
        html_path
    ]
    
    try:
        subprocess.run(cmd, check=True)
        print(f"  SUCCESS: PDF study guide generated at: {pdf_path}")
    except Exception as e:
        print(f"  ERROR: Edge execution failed: {e}")

if __name__ == "__main__":
    generate_markdown_plan()
    generate_templates()
    generate_html_plan()
    render_pdf()
    print("All tasks finished successfully!")
