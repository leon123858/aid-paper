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

提出了一種全新的第三方登入機制, 透過每一次用戶行為的時空特徵來作為驗證的基礎。這種機制不僅可以提供更高的安全性, 也可以提供更好的用戶體驗。以下條列部分差異化的特點:

- 簡單易用: 支援可以重複的帳號與密碼, 這樣可以讓使用者更容易記住帳號與密碼。
- 帳號救援: 透過使用者的時空作為救援判斷基礎, 例如忘記密碼等。
- 自主獨立: 去中心化的驗證中心, 使用者可以自行選擇驗證中心。
- 隱私保護: 使用者的個人資訊可以存放在自己的設備上, 不會被第三方機構擁有。
- 高安全性: 透過時空特徵的驗證, 可以提供更高的安全性。
- GDPR 遵循: 透過使用者的同意, 可以提供更好的隱私保護。
- 公開透明: 透過開放的 API, 可以讓第三方應用程式更容易接入。
- 單向驗證: 服務 ID 不公開映射到使用者 ID, 這樣可以提供更好的隱私保護。
- 高可用性: 透過多個驗證中心, 可以提供更高的可用性。

## related work

implementations of the paper in github: [link](https://github.com/leon123858/aid)
