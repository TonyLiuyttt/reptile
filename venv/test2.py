
def spe_analyse(str):
    str1 = str.split('>', 3)
    print(str1)
    str2 = str1[3].split('<', 1)
    return str2[0]

str = '[<span><i class="icon dtIcon"></i>距2号线观水路步行316m</span>]'
a =spe_analyse(str)
print(a)




