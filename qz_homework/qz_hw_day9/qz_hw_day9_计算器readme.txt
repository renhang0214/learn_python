"1 - 2 * ( (60-30 +(-40.0/5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"

用re模块取得最里面的括号内的表达式进行计算并拿到结果，一次递归得到最后的结果

对括号内的表达式进行处理，
    根据算法口诀先对×÷进行判断，×÷计算后再进行＋－的计算并得出最终结果