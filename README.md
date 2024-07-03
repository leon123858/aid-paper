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

自主身份系統, 寓意著『成為自己身份的主人』, 這是一個全新的身份系統, 透過特殊的技術與架構設計, 讓用戶可以自主管理自己的身份, 這個系統將帶來以下三個核心變化

- 便捷
  - 過去: 不斷的加入各個組織的身份系統, 甚至同一個組織還有多套身份方案。
  - 自主身份: 用戶管理自己的身份, 在需要時用同一個身份加入不同組織。
- 安全
  - 過去: 個人權限與數據完全受平台運營者的掌握, 只能仰賴他人的保護。
  - 自主身份: 用戶可以控制與限制自己的權限與數據，不再依賴平台運營者的自覺。
- 公平
  - 過去: 大型組織掌握大量用戶資源,容易形成壟斷,用戶處於弱勢地位。
  - 自主身份: 任何人都有權利管理自己的身份，不受特定組織的限制或控制。

## related work

implementations of the paper in github: [link](https://github.com/leon123858/aid)
