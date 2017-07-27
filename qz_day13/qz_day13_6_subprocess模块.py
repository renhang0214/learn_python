# /usr/local/bin/python
# -*- coding: utf-8 -*-
# Author: Ren Hang


import subprocess


# 简单命令call
subprocess.call("ls", shell=True)  # 执行系统命令
print(subprocess.check_call('ls', shell=True))  # 执行系统命令并获取返回值（执行状态吗），返回值为0则表示执行状态，否则为异常
print(subprocess.check_output('ls', shell=True))  # 执行系统命令，如果执行状态吗为0则返回执行结果，否则执行异常
# 参数shell:shell=True表示多行命令可以写在一起（"ls -l"）；shell=False表示多行命名必须分开写（"ls","-l"）

# 复杂命令Popen
# subprocess.Popen(self, args, bufsize=-1, executable=None,
#                  stdin=None, stdout=None, stderr=None,
#                  preexec_fn=None, close_fds=_PLATFORM_DEFAULT_CLOSE_FDS,
#                  shell=False, cwd=None, env=None, universal_newlines=False,
#                  startupinfo=None, creationflags=0,
#                  restore_signals=True, start_new_session=False,
#                  pass_fds=())
# 参数args：shell命令，可以是字符串或者序列类型（如：list，元组）
# 参数bufsize：指定缓冲。0 无缓冲,1 行缓冲,其他 缓冲区大小,负值 系统缓冲
# 参数stdin, stdout, stderr：分别表示程序的标准输入、输出、错误句柄
# 参数preexec_fn：只在Unix平台下有效，用于指定一个可执行对象（callable object），它将在子进程运行之前被调用
# 参数close_sfs：在windows平台下，如果close_fds被设置为True，则新创建的子进程将不会继承父进程的输入、输出、错误管道。所以不能将close_fds设置为True同时重定向子进程的标准输入、输出与错误(stdin, stdout, stderr)。
# 参数shell：同上
# 参数cwd：用于设置子进程的当前目录
# 参数env：用于指定子进程的环境变量。如果env = None，子进程的环境变量将从父进程中继承。
# 参数universal_newlines：不同系统的换行符不同，True -> 同意使用 \n
# 参数startupinfo与createionflags只在windows下有效参数将被传递给底层的CreateProcess()函数，用于设置子进程的一些属性，如：主窗口的外观，进程的优先级等等
a = subprocess.Popen("mkdir s2", shell=True)  # Popen执行简单的命令方法与call一样
# 1、输入即可得到输出
# obj1 = subprocess.Popen("mkdir t3", shell=True, cwd='目录路径', )  # 新建文件夹并放到指定的目录

# 2、输入进行某环境，依赖再输入
obj2 = subprocess.Popen("python", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        universal_newlines=True)  # 执行python命令，并设置输入、输出、错误、换行
obj2.stdin.write("print(1)\n")  # 将命令写入输出
obj2.stdin.write("print(2)")  # 将命令写入输出
obj2.stdin.close()  # 关闭输入

cmd_out = obj2.stdout.read()  # 输出输入的内容
obj2.stdout.close()  # 关闭输出
cmd_error = obj2.stderr.read()  # 错误时输出输入的内容
obj2.stderr.close()  # 关闭错误

print(cmd_out)  # 输出
print(cmd_error)  # 报错

# 与进程交互：将数据发送到stdin。 读取数据stdout和stderr，直到达到文件结尾。 等待过程终止。
# 1
obj3 = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        universal_newlines=True)
obj3.stdin.write("print(1)\n")
obj3.stdin.write("print(2)")

out_error_list = obj3.communicate()
print(out_error_list)
# 2
obj4 = subprocess.Popen(["python"], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                        universal_newlines=True)
out_error_list = obj4.communicate('print("hello")')
print(out_error_list)
