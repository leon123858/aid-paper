# aid-paper

this is my master paper in NTU.

## How to download this paper

[click here](https://leon123858.github.io/aid-paper/)

## What does my paper talking about?

本研究探討了將自主概念應用於數位身分管理的方法，提出「自主身分」（Autonomous Identity，AID）系統。該系統使每位使用者在具備道德標準的身分系統中自由的管理自己，旨在解決當前身分管理模式的固有限制。

## contribution

- 世界上存在著可以自己證明自己身分正確性的機制，且廣泛被使用著，舉例就是公私鑰簽章在 ssh server 上的使用。
- 但其不能被應用到一般性的身分管理系統，如 google login, FB login ......等等。我們認為是因為基本功能的匱乏，其沒辦法承擔廣泛且具有變化的使用者需求。
- 我們發展的 AID，透過 block chain 把驗證所需資訊 bind 到 uuid 上，藉此達成上面的缺憾。
  - 舉例來說: 把公鑰和 UUID 上鏈，接著找到任意一個人向他聲明自己是 UUID 的指向對象，最後私下交付可以被鏈上公鑰驗證的簽名即可證明自己的聲明。

## related work

implementations of the paper in github: [link](https://github.com/leon123858/aid)
