# aid-paper

this is my master paper in NTU.

## How to download this paper

[click here](https://leon123858.github.io/aid-paper/)

## How to setup vs-code as Latex editor

step

1. use docker pull Latex Image: `docker pull leon1234858/my-latex-live`
2. install extension named `James-Yu.latex-workshop` in vs-code.
3. Open your VS Code Settings(`setting.json`) and add the following lines.

note: original registry is `docker pull ghcr.io/xu-cheng/texlive-full`

```
"latex-workshop.docker.enabled": true,
"latex-workshop.docker.image.latex": "leon1234858/my-latex-live",
"latex-workshop.latex.recipe.default": "latexmk (xelatex)",
"latex-workshop.latex.outDir": "./.out",
"latex-workshop.latex.autoBuild.run": "never",
"[latex]": {
	"editor.defaultFormatter": "James-Yu.latex-workshop",
	"editor.wordWrap": "on"
}
```

compile

> When you open `*.tex` file the next time, you will see a little run icon, which will compile your latex project in a container. And output to project root/.out folder.

pre-view

you can use view button next to run icon above in `*.tex` files, it will be a pre-view tab in vs-code.

## What does my paper talking about?

本研究探討了將自主概念應用於數位身份管理的創新方法，提出「自主身份」（Autonomous Identity，AID）系統。該系統賦予每位用戶全面控制個人數位身份的能力，旨在解決當前身份管理模式的固有限制。

## related work

implementations of the paper in github: [link](https://github.com/leon123858/aid)
