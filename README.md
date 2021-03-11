# KeepNodesOn
## 假装节点都在线
> 此程序只支持SSPanel

## 安装
0. 安装python3 和 requests库
1. 直接复制 keep.py 中的内容到你的服务器
2. 修改 4 处
  - 面板域名
  - 面板密码
  - 假装在线节点号区间起始值（包含）
  - 假装在线节点号区间结束值（不包含）

4. 运行命令 
```shell
nohup python3 keep.py > /dev/null 2>&1 &
```
如有需要，自行替换python3为你机器上的python3解释器名称
