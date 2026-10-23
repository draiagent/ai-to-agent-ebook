"""把電子書 PDF 轉成網頁用的圖片與文字資料（data.js）。
用法：python build.py
"""
import json, re, io, sys, pathlib
import pymupdf
from PIL import Image

HERE = pathlib.Path(__file__).parent
PDF = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else HERE.parent / "AI_to_Agent_學習教材_全書.pdf"
IMG = HERE / "img"
IMG.mkdir(exist_ok=True)

PARTS = [
    {"id": 1, "name": "第一篇", "title": "知識原理", "tag": "懂原理", "color": "blue", "chapters": [1, 7]},
    {"id": 2, "name": "第二篇", "title": "任務設計", "tag": "會設計", "color": "teal", "chapters": [8, 14]},
    {"id": 3, "name": "第三篇", "title": "實作應用", "tag": "能落地", "color": "gold", "chapters": [15, 21]},
]
CHAPTERS = [
    (1, "用了 AI，為什麼事情還是自己做？", "從 AI 到 Agent", 3),
    (2, "AI 怎麼會一本正經地亂答？", "LLM 與 Token", 16),
    (3, "為什麼 AI 越聊越笨？", "Context 與 Prompt", 28),
    (4, "資料一大堆，AI 抓不到重點？", "資料整理｜Gemini Notebook", 40),
    (5, "AI 為什麼只會說、不會做？", "外掛程式：從聊天走到工作", 53),
    (6, "每次都要重教 AI 一遍？", "MCP 與 Skill：下載工具、建立技能", 66),
    (7, "每一步都要你盯，AI 不能自己辦完？", "Agent：從單純工作到複雜任務", 80),
    (8, "這件事該交給哪種 AI？", "TRC-3D：先診斷任務，再配置能力", 90),
    (9, "事情太複雜，說不清楚？", "VAD：和 AI 共用同一套工作流程", 102),
    (10, "好東西都在網路上，卻不會用？", "GitHub：天下英才皆我所用", 114),
    (11, "別人的好方法怎麼拿來用？", "RE:Agent：看懂、沿用、重組", 126),
    (12, "每次都要重新交代，累不累？", "Promptless：少寫提示詞，把流程寫清楚", 138),
    (13, "AI 做的成果，能信嗎？", "決策治理與品質驗收", 151),
    (14, "交代的事，怎麼變成一張卡？", "VAC：從 VAD 到 VAD-8A", 165),
    (15, "公司的老問題怎麼解？", "VAD-8A 企業實作", 183),
    (16, "做出來的圖風格不一致？", "VSA：視覺設計代理", 196),
    (17, "人和 AI 怎麼一起工作？", "整合實作", 208),
    (18, "一個人也能帶一整個團隊？", "從 Personal Agent OS 到公司 aOS", 220),
    (19, "讓 AI 做事，安全嗎？", "企業自主資安系統", 233),
    (20, "公司導入 AI，從哪開始？", "企業導入 AI：先做得成，再做得省", 247),
    (21, "工具一直換，什麼才不會變？", "以人為本，回歸需求", 259),
]
EPILOGUE_START = 275

FOOTER = re.compile(r"益力康陳董|^\d+\s*/\s*\d+$|^\d+$|^AI TO AGENT$|^第.篇：|^CHAPTER")
ASCII_GAP = re.compile(r"(?<=[A-Za-z0-9\-:.]) (?=[A-Za-z0-9\-:.])")


def clean(text):
    lines = [l.strip() for l in text.split("\n")]
    # 投影片字距拉寬會變成「L L M 與 To k e n」，把英數之間的空格收掉
    lines = [ASCII_GAP.sub("", l) if re.search(r"\b\w \w \w\b", l) else l for l in lines]
    return [l for l in lines if l and not FOOTER.search(l)]


def main():
    doc = pymupdf.open(PDF)
    pages = {}
    for i, page in enumerate(doc):
        n = i + 1
        pix = page.get_pixmap(dpi=144)  # 1920x1080
        im = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
        im.thumbnail((1600, 900))  # PDF 為 1440x810
        im.save(IMG / f"p{n:03d}.webp", "WEBP", quality=72, method=6)
        pages[n] = clean(page.get_text())
        print(n, end=" ", flush=True)

    chapters = []
    for idx, (no, title, sub, start) in enumerate(CHAPTERS):
        end = (CHAPTERS[idx + 1][3] if idx + 1 < len(CHAPTERS) else EPILOGUE_START) - 1
        chapters.append({"no": no, "title": title, "sub": sub, "start": start, "end": end})
    data = {
        "parts": PARTS,
        "chapters": chapters,
        "epilogue": {"start": EPILOGUE_START, "end": len(doc)},
        "pages": {str(k): v for k, v in pages.items()},
        "total": len(doc),
    }
    (HERE / "data.js").write_text(
        "window.BOOK=" + json.dumps(data, ensure_ascii=False, separators=(",", ":")) + ";",
        encoding="utf-8",
    )
    print("\ndone")


if __name__ == "__main__":
    main()
