#-*-coding:utf8-*-
#author : Lenovo
#date: 2019/1/6

#单例模式是一种常用的设计模式  在他的核心结构中只有一个被称为单例类的特殊类
# 这个模式的作用是可以保证系统中的这个类只有一个实例且这个实例容易被外界访问
#通过队实力个数的限制 从而达到节省资源的效果
# -------------------------------------------------------------------------------------------
# 方法一
#使用__new__方法

class Single:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,"instance"):
            cls.instance=super(Single, cls).__new__(cls)
        return cls.instance
s1=Single()
s2=Single()
print(s1 is s2)
# -----------------------------------------------------------------------------------------
#方法二 使用Import方法
class Single2:
    pass
s3=Single2()
# 然后将其放到单独的一个Py文件中 使用时直接from .. import 这个对象就可以保证只有一个实例
# -------------------------------------------------------------------------------------------

