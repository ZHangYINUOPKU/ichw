# ichw

### 问题一
停机问题（halting problem）是逻辑数学中可计算性理论的一个问题。停机问题即是：是否存在一个算法，对于任意给定的图灵机都能判定任意的初始格局是否会导致停机。图灵证明了这个算法是不存在的，即停机问题是不可判定的，从而使之成为解决许多不可判定性问题的基础。

### 问题二
补码定义：计算机中二进制形式的补数。在日常生活中，把时钟里的分钟顺时针调整40分钟和逆时针调整20分钟，分针最后的位置是一样的，此时20和40就是补数。计算机也可以看成一个与时钟类似的计量器，所以在计算机之中，使用补码可以使减法变为加法，以此来简化逻辑算术单元设计。所以现在的计算机之中没有减法器，只有加法器。  

补码计算法定义：非负数的补码是其原码本身；负数的补码是其原码最高位符号位不变，其它位取反，再加1。负数原码求补码时，如果反码不加一，不看符号位，其补码与原码相加其他所有位上都为一，比模少了1，所以负数求补码时最后要加一。例子：计算7-3，在二进制位数n为4时，7的原码是0111，补码是0111，-3的原码是0011，再对其原码求补码得到1101，所以-3用二进制形式为1101将两数补码相加，得到0100，换成十进制是4，结果正确。

### 问题三
#### IEEE 754的16 bit 浮点数表示
| Sign | Exp | Frac | Value |
| ----- | :----: | :----: | -----:|
| * | 0000000 | 00000000 | ±0.0 |
| 0 | 0111111 | 00000000 | 1.0 |
| 1 | 0111111 | 00000000 | -1.0 |
| * | 1111111 | 00000000 | ±∞ |
| * | 1111111 | non zero | NaN |
| * | 0000000 | 00000001 | ±2^-62×2^-8 |
| * | 0000000 | 11111111 | ±2^-62×(1-2^-8) |
| * | 0000001 | 00000000 | ±2^-62 | 
| * | 1111110 | 11111111 | ±2^63×(2-2^-8) |
