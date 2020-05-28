#! /usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(8,6))
plt.title('scatter')
#Generating a Gaussion dataset:
#creating random vectors from the multivariate normal distribution
#given mean and covariance
mu_vec1=np.array([0,0])
cov_mat1=np.array([[1,0],[0,1]])
X=np.random.multivariate_normal(mu_vec1,cov_mat1,500)
R=X**2
R_sum=R.sum(axis=1)
plt.scatter(X[:,0], X[:,1], color='green', marker='o',
            s=32.*R_sum, edgecolor='black', alpha=0.5)

plt.show()

'''
scatter(x, y, s=None, c=None, marker=None, cmap=None, norm=None, \
        vmin=None, vmax=None, alpha=None, linewidths=None, \
        verts=None, edgecolors=None, hold=None, data=None, **kwargs)

x，y：array_like，shape(n，)
        输入数据

s： shape 标量或array_like，shape(n，)，可选
    大小以点数^ 2。默认是`rcParams ['lines.markersize'] ** 2`。

c：颜色，顺序或颜色顺序，可选，默认：'b'
    `c`可以是单个颜色格式的字符串，也可以是一系列颜色
    规范的长度为`N`，或一系列`N`数字
    使用通过kwargs指定的`cmap`和`norm`映射到颜色
    (见下文)。请注意，`c`不应该是单个数字RGB或
    RGBA序列，因为这与数组无法区分
    值将被彩色映射。 `c`可以是一个二维数组，其中的
    行是RGB或RGBA，但是，包括单个的情况
    行为所有点指定相同的颜色。

marker：`~matplotlib.markers.MarkerStyle`，可选，默认值：'o'
    请参阅`~matplotlib.markers`以获取有关不同的更多信息
    标记分散支持的样式。 `marker`可以是
    该类的实例或特定文本的简写
    标记。

cmap：`~matplotlib.colors.Colormap`，可选，默认：无
    一个`~matplotlib.colors.Colormap`实例或注册名称。
    `cmap`仅在`c`是浮点数组时使用。如果没有，
    默认为rc`image.cmap`。

norm：`~matplotlib.colors.Normalize`，可选，默认：无
    `~matplotlib.colors.Normalize`实例用于缩放
    亮度数据为0,1。`norm`只有在`c`是一个数组时才被使用
    彩车。如果`None'，则使用默认值：func：`normalize`。

vmin，vmax：标量，可选，默认值：无
    `vmin`和`vmax`与`norm`结合使用来标准化
    亮度数据。如果其中任何一个都是`无'，那么最小和最大的
    使用颜色数组。请注意，如果你通过一个“规范”实例，你的
    `vmin`和`vmax`的设置将被忽略。

alpha：标量，可选，默认值：无
    alpha混合值，介于0(透明)和1(不透明)之间，

linewidths：标量或array_like，可选，默认值：无
    如果无，则默认为(lines.linewidth，)。

verts：(x，y)的序列，可选
    如果`marker`为None，这些顶点将用于
    构建标记。标记的中心位于
    在(0,0)为标准化单位。整体标记重新调整
    由``s``完成。

edgecolors ：颜色或颜色顺序，可选，默认值：无
    如果无，则默认为'face'

    如果'face'，边缘颜色将永远是相同的
    脸色。

    如果它是'none'，补丁边界不会
    被画下来。

    对于未填充的标记，“edgecolors”kwarg
    被忽视并被迫在内部“面对”。
'''
