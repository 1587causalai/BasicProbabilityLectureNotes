# 处理 Docsify 中数学公式与 Markdown 强调渲染疑难杂症指南

当我的 Docsify 网站上的数学公式或 Markdown 强调（特别是加粗）没有按预期显示时，我会按照以下步骤来排查和解决问题。这些是我在解决实际问题时总结的经验，希望能帮助你（或者未来的我）更快定位并修复它们。

## 一、数学公式渲染问题（通常与 KaTeX 或 MathJax 有关）

如果页面上的 LaTeX 公式没有正确渲染（例如，显示的是原始 LaTeX 代码或者乱码），我会检查以下几点：

1.  **检查 `docs/index.html` 配置**：
    *   **是否引入了数学渲染库？** 确保 `<head>` 中有 KaTeX 的 CSS 链接，并且在 `<body>` 底部有 KaTeX 的 JS 和相应的 Docsify 插件（如 `docsify-katex` 或 `docsify-latex`）的 JS 链接。
        *   例如，对于 KaTeX，应该有类似：
            ```html
            <!-- KaTeX CSS -->
            <link rel="stylesheet" href="//cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.css" />
            <!-- KaTeX JS and Docsify Plugin -->
            <script src="//cdn.jsdelivr.net/npm/katex@latest/dist/katex.min.js"></script>
            <script src="//cdn.jsdelivr.net/npm/docsify-latex@0"></script> <!-- 或者 docsify-katex -->
            ```
    *   **`window.$docsify` 配置是否正确？** 特别是 `latex` 或 `katex` 相关的配置，要确保内联公式（如 `$...$` 或 `\(...\)`) 和块级公式（如 `$$...$$` 或 `\[...\]`) 的定界符设置正确。
        ```javascript
        window.$docsify = {
          // ...其他配置...
          latex: {
            inlineMath: [['$', '$'], ['\\(', '\\)']], // 注意JS字符串中反斜杠需要转义
            displayMath: [['$$', '$$'], ['\\[', '\\]']] // 注意JS字符串中反斜杠需要转义
          }
        };
        ```

2.  **检查 Markdown 文件中的公式写法**：
    *   确认所有的数学公式都使用了在 `index.html` 中配置的正确定界符。
    *   内联公式：例如 `$E=mc^2$`
    *   块级公式：例如 `$$\sum_{i=1}^{n} x_i$$` 或 `\[ \frac{a}{b} \]`
    *   避免在公式中直接使用 Markdown 的特殊字符，除非它们是 LaTeX 命令的一部分。

3.  **网络与缓存**：
    *   确保 CDN 链接有效且可访问。
    *   **强制刷新浏览器**（通常是 Ctrl+Shift+R 或 Cmd+Shift+R）以清除缓存，确保加载的是最新的 `index.html` 和 JS 插件。

## 二、Markdown 强调（尤其是加粗 `**...**`）渲染问题

如果 Markdown 中的加粗 `**...**` 或 `__...__` 没有生效，反而显示出了原始的星号或下划线，特别是在涉及中英文混合或标点符号时，我会考虑以下情况：

1.  **中文字符与英文括号之间缺少空格**：
    *   **问题模式**：`中文(English)`，例如 `进行**连续性修正(Continuity Correction)**`。
    *   **原因**：Markdown 解析器可能因为中文字符和英文左括号紧挨着而无法正确识别强调的边界。
    *   **手动修复**：在中文和英文左括号之间加一个空格，例如 `进行**连续性修正 (Continuity Correction)**`。

2.  **强调标记的结束符与后续标点符号之间缺少空格**：
    *   **问题模式**：`**强调文本**标点`，例如 `**公理**：` 或 `**搞定**。`
    *   **原因**：Markdown 解析器可能因为强调的结束标记 `**` 后面紧跟着一个标点符号而无法正确识别强调的结束。
    *   **手动修复**：在结束的 `**` 和标点符号之间加一个空格，例如 `**公理** ：` 或 `**搞定** 。`

3.  **使用自定义 Docsify 插件进行自动修复（推荐方案）**：
    *   如果上述问题普遍存在，手动修复会很繁琐。这时，我会考虑在 `docs/index.html` 中添加一个小型的自定义 Docsify 插件，在 Markdown 内容被解析前，通过正则表达式自动修正这些模式。
    *   **插件逻辑示例**（这个是我们一起完善的版本）：
        ```javascript
        function autoFixMarkdownRenderingPlugin(hook, vm) {
          hook.beforeEach(function (markdown) {
            let tempMarkdown = markdown;

            // 规则1: 修正 "中文(English)" -> "中文 (English)"
            // 例如: "字(E" -> "字 (E"
            const rule1Regex = /([\u4e00-\u9fff])(\((?=[A-Za-z0-9]))/g;
            tempMarkdown = tempMarkdown.replace(rule1Regex, '$1 $2');

            // 规则2: 修正 "text**标点" -> "text** 标点" 或 "text__标点" -> "text__ 标点"
            // (支持 **...** 和 __...__，支持中英文常见标点)
            const punctuationSet = '[：。，；？！:.,;?!]'; // 中英文标点集合

            // 针对 **...**
            const rule2StrongRegex = new RegExp(\`([^\\\\s\\\\*])(\\\\*\\\\*)(\${punctuationSet})\`, 'g');
            tempMarkdown = tempMarkdown.replace(rule2StrongRegex, '$1$2 $3');
            
            // 针对 __...__ (如果使用)
            const rule2EmphasisRegex = new RegExp(\`([^\\\\s_])(__)(\${punctuationSet})\`, 'g');
            tempMarkdown = tempMarkdown.replace(rule2EmphasisRegex, '$1$2 $3');

            return tempMarkdown;
          });
        }

        // 注册插件 (确保这段代码在引入 Docsify 之后执行)
        if (window.$docsify && window.$docsify.plugins && Array.isArray(window.$docsify.plugins)) {
          window.$docsify.plugins.push(autoFixMarkdownRenderingPlugin);
        } else {
          window.$docsify = window.$docsify || {};
          window.$docsify.plugins = [autoFixMarkdownRenderingPlugin];
        }
        ```
    *   **注意**：正则表达式的编写和调试可能需要反复尝试，确保它能准确匹配目标模式，并且不会错误地修改其他内容。从简单开始，逐步完善。

4.  **检查 Markdown 源文件**：
    *   仔细核对出问题的 Markdown 片段，确保没有多余的空格、不可见字符，或者 `**`、`__` 标记不成对等问题。

## 三、通用排查步骤

1.  **强制刷新浏览器**：这是首要步骤，排除缓存干扰 (通常 Ctrl+Shift+R 或 Cmd+Shift+R)。
2.  **最小化复现**：如果问题复杂，尝试在一个全新的、最简单的 Markdown 文件中复现问题，这有助于隔离干扰因素。
3.  **检查控制台错误**：打开浏览器开发者工具的控制台（通常按 F12），看看是否有 JavaScript 错误，这可能指向插件加载失败或其他脚本问题。

希望这份指南能帮到你！处理这些渲染细节确实需要耐心和细致的排查。 