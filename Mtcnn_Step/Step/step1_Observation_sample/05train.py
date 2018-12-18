# 训练
# 可分开训练 可同时训练

# 训练者类
# 1 # 1.1 传入需要被训练的网络
# 7 # 1.2 训练数据保存路径
# 2 # 1.3 数据集路径
# 8 # 1.4 是否使用cuda net.cuda()
# 8 # 1.5 如果有当前的权重就加载进来接着训练 如果没有就不执行
# 6 # 1.6 无限训练
# 3 # 1.7 取出数据集
# 8 # 1.8 如果使用cuda就使用gpu计算 如果不使用cpu计算
# 4 # 1.9 使用网络进行前向计算  返回置信度和偏移
# 5 # 1.10 计算损失 (置信度损失 + 偏移损失)  (分类损失 正样本和负样本交叉熵损失 + 偏移量损失 正样本和中间样本的平方差损失)
# 6 # 1.11 优化器清零 总损失反向传播 调整权重
# 7 # 1.12 保存权重


# P-Net train
# 1.1 创建Net对象
# 1.2 传入网络给 训练者的类
# 1.3 传入训练数据
# 1.4 保存网络训练的参数