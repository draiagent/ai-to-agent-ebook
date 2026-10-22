# AI to Agent 學習教材｜互動電子書

#從學員痛點出發、用Agent解決問題

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)](CHANGELOG.md)

> 《AI to Agent 學習教材：知識原理、任務設計與實作應用》的手機互動式電子書，針對新手與長者設計，可一鍵放大字體。

**線上閱讀：** https://draiagent.github.io/ai-to-agent-ebook/

## 功能

- 首頁：作者介紹、全書目錄、繼續上次閱讀
- 三篇分開學習：第一篇 知識原理（01–07 章）、第二篇 任務設計（08–14 章）、第三篇 實作應用（15–21 章）
- 「小／中／大」字體按鈕，手機會記住設定
- 大按鈕翻頁、左右滑動翻頁、點投影片全螢幕放大
- 每頁附「大字文字版」
- 提問頁可直接作答（只存在讀者自己的手機）
- 記住閱讀進度與已讀章節

## 專案結構

```text
ai-to-agent-ebook/
├─ index.html      # 電子書網頁（單一檔案）
├─ data.js         # 目錄與每頁文字（由 build.py 產生）
├─ img/            # 每頁投影片圖片 p001.webp ~ p292.webp
├─ build.py        # 從 PDF 重新產生 img/ 與 data.js
├─ .nojekyll
├─ README.md
├─ LICENSE
├─ VERSION
└─ CHANGELOG.md
```

## 更新內容

把新版 `AI_to_Agent_學習教材_電子書.pdf` 放在本資料夾的上一層，執行：

```bash
python build.py
```

## 授權

CC BY-SA 4.0，詳見 [LICENSE](LICENSE)。

## Version

**v1.0.0 — 2026-10-22**

**AI Coach 益力康陳董 x CGM Coach 血糖教練 | 2026 AI to Agent | 2027 AI to AGI Agent**
