#kitti数据集官方评价工具需要result文件中每个图片必须要有对应的结果文件txt 但是有的模型未检测到目标就不输出txt
#为解决此问题 制作填补工具
import os

folder_path = '/home/whut-4/Desktop/HXB/05-31/devkit_object/cpp/results/0531_1118_results/result_sha/data/'  # 文件夹路径
#              /home/whut-4/Desktop/HXB/05-31/devkit_object/cpp/results/0531_1118_results/result_sha/data/000001.txt
start_index = 0  # 起始编号
end_index = 7480  # 结束编号

for i in range(start_index, end_index + 1):
    filename = '{:06d}.txt'.format(i)  # 构造文件名
    file_path = os.path.join(folder_path, filename)  # 构造文件路径
    #print("file_path = {} \n".format(file_path))
    if not os.path.exists(file_path):  # 如果文件不存在
        print("add {:06d}.txt".format(i))
        with open(file_path, 'w') as file:  # 创建新文件
            pass  # 可以写入初始内容，这里留空

    # 可以在此处添加对新建文件的处理逻辑
    # 例如，你可以在新建文件时写入一些初始内容或者执行其他操作
