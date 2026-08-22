# wind989.github.io 项目同步配置

这套配置已经按当前博客的 Jekyll 结构准备好：

- 项目列表固定展示 `RepoMind` 和 `TicketInsight`。
- GitHub Actions 每天自动读取两个公开仓库的 Releases。
- 发布信息会写入 `_data/releases.json`，博客首页的“项目与最新发布”区域会自动显示。
- Actions 页面支持手动运行一次同步。

## 放入博客仓库

将本目录中的文件复制到 `wind989.github.io` 仓库对应位置，并保留下面这些路径：

```text
_data/projects.json
_data/releases.json
_sass/custom.scss
index.md
scripts/sync_releases.py
.github/workflows/sync-project-releases.yml
```

然后提交并推送到博客仓库的 `main` 分支。GitHub Pages 会按现有设置重新构建页面。

## 第一次运行

打开博客仓库的 **Actions → Sync project releases → Run workflow**，手动运行一次即可验证。之后工作流每天自动运行；如果两个项目还没有公开 Release，页面会显示“暂无公开 Release”，等首次发布后会自动出现。

这套方案只读取公开仓库的 Release，不需要个人访问令牌，也不会读取或上传项目源代码。
