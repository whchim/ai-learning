快速创建日志并放在日志文件夹下
如果使用 PowerShell：
New-Item -Path "00-daily-logs\$(Get-Date -Format 'yyyy-MM-dd').md" -ItemType File
如果使用 Git Bash：
touch 00-daily-logs/$(date +%Y-%m-%d).md

更新github
git add .
git commit -m "2026-03-18更新"
git push -f origin main # 强制把本地内容更新在github仓库