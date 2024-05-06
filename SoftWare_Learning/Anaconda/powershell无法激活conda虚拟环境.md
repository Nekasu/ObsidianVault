原文链接：[CSDN博主「weixin_42613703」](https://blog.csdn.net/weixin_42613703/article/details/112169956)

- - - 

1. 选择管理员方式进入powershell
2. 执行`conda init powershell`
3. 重新打开powershell若显示base则成功了，可输入conda activate env_name(conda 不能省)。若不显示，转入第4步。
4. 执行get-ExecutionPolicy，若回复 Restricted，表示状态是禁止的。执行set-ExecutionPolicy RemoteSigned，在出现的结果中输入 Y 并回车，设置完毕。
5. 重新打开powershell，即可看到命令行开头有“（base）”，输入conda activate envs_name 命令即可激活相应的虚拟环境。
