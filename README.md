# 寸箋
BibTeX 添加管理工具。
「寸箋」本來指短信和名刺，用 BibTeX 記錄文獻恰如給文獻貼名片，故名。

## 特色
* 開源跨平臺。能裝 Python 就能用。
* 旣可以直接從別處複製粘貼人家做好的 BibTeX ，也可以自己根據每一項來塡寫。

## 使用
1. 下載 BibInT.pyw 和 BibTeX.png
2. 安裝 [Python 3](https://www.python.org/downloads/) 環境、模塊 (cmd 執行 pip install bibtexparser) 。
3. 編輯 BibInT.pyw ，塡寫文件夾和默認存儲文獻的文件。
4. 運行 BibInT.pyw 。

## ChangeLog:
2015/10/07: 用 PyQt 畫框架，未放置功能。  
2015/10/08: 引入 bibtexparser ，渲染 BibTeX 文件並顯示在列表。  
2015/10/10: 「添加文獻」功能，添加時會刷新列表、備份現有 .bib 文件。  
2015/10/13: 實現刪除、編輯、搜索。至此基礎功能全部完成，開發狀態記爲 alpha 。  