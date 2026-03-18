快速创建日志并放在日志文件夹下
如果使用 PowerShell：
New-Item -Path "00-daily-logs\$(Get-Date -Format 'yyyy-MM-dd').md" -ItemType File
如果使用 Git Bash：
touch 00-daily-logs/$(date +%Y-%m-%d).md