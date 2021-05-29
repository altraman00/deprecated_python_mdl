import tensorflow as tf
# from nets import nets_factory
from Alexnet import Network

tf.reset_default_graph()
# 字符数量
CHAR_NUM = 10
# 图片高度和宽度
IMAGE_HEIGHT = 60
IMAGE_WIDTH = 160
# 批次
BATCH_SIZE = 10
TFRECORD_FILE = "./image/tfrecord/train.tfrecords"
CHECKPOINT_DIR = './ckpt/'

# placeholder
x = tf.placeholder(tf.float32, [None, 224, 224])
y0 = tf.placeholder(tf.float32, [None])
y1 = tf.placeholder(tf.float32, [None])
y2 = tf.placeholder(tf.float32, [None])
y3 = tf.placeholder(tf.float32, [None])

lr = tf.Variable(0.0003, dtype=tf.float32)


# 从tfrecord中读取数据
def read_and_decode(filename):
    # 根据文件名生成队列
    filename_queue = tf.train.string_input_producer([filename])
    reader = tf.TFRecordReader()
    # 返回文件名和文件
    _, serialized_example = reader.read(filename_queue)
    features = tf.parse_single_example(serialized_example, features={'image': tf.FixedLenFeature([], tf.string),
                                                                     'label0': tf.FixedLenFeature([], tf.int64),
                                                                     'label1': tf.FixedLenFeature([], tf.int64),
                                                                     'label2': tf.FixedLenFeature([], tf.int64),
                                                                     'label3': tf.FixedLenFeature([], tf.int64)
                                                                     })
    # 获取图片数据
    image = tf.decode_raw(features['image'], tf.uint8)
    # tf.train.shuffle_batch必须确定shape
    image = tf.reshape(image, [224, 224])
    # 图片预处理归一化(-1,1)
    image = tf.cast(image, tf.float32) / 255.0
    image = tf.subtract(image, 0.5)
    image = tf.multiply(image, 2.0)
    # 获取labels
    label0 = tf.cast(features['label0'], tf.int32)
    label1 = tf.cast(features['label1'], tf.int32)
    label2 = tf.cast(features['label2'], tf.int32)
    label3 = tf.cast(features['label3'], tf.int32)
    return image, label0, label1, label2, label3


# 获取图片数据和标签
image, label0, label1, label2, label3 = read_and_decode(TFRECORD_FILE)

# 使用shuffle_batch可以随机的打乱
image_batch, label_batch0, label_batch1, label_batch2, label_batch3 = tf.train.shuffle_batch(
    [image, label0, label1, label2, label3], batch_size=BATCH_SIZE, \
    capacity=1075, min_after_dequeue=1000, num_threads=128)

# 定义网络结构
# train_network_fn = nets_factory.get_network_fn('alexnet_v2', num_classes=CHAR_NUM, \
#                                                weight_decay=0.0005, is_training=True)
train_network_fn = Network(num_classes=CHAR_NUM,weight_decay=0.0005, is_training=True)

# gpu_options = tf.GPUOptions(allow_growth=True)

# with tf.Session(config=tf.ConfigProto(log_device_placement=False,allow_soft_placement=True,gpu_options=gpu_options)) as sess:
#     gpu_options = tf.GPUOptions(allow_growth=True)
#     tf.Session(config=tf.ConfigProto(log_device_placement=False,allow_soft_placement=True,gpu_options=gpu_options))

with tf.Session() as sess:
    X = tf.reshape(x, [BATCH_SIZE, 224, 224, 1])

    # 训练以后得到的输出值
    logits0, logits1, logits2, logits3, end_pintos = train_network_fn.construct(X)

    # 把标签打成one_hot形式
    one_hot_labels0 = tf.one_hot(indices=tf.cast(y0, tf.int32), depth=CHAR_NUM)
    one_hot_labels1 = tf.one_hot(indices=tf.cast(y1, tf.int32), depth=CHAR_NUM)
    one_hot_labels2 = tf.one_hot(indices=tf.cast(y2, tf.int32), depth=CHAR_NUM)
    one_hot_labels3 = tf.one_hot(indices=tf.cast(y3, tf.int32), depth=CHAR_NUM)

    # 四部分的loss
    loss0 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits0, labels=one_hot_labels0))
    loss1 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits1, labels=one_hot_labels1))
    loss2 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits2, labels=one_hot_labels2))
    loss3 = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits3, labels=one_hot_labels3))
    # 总的loss
    total_loss = (loss0 + loss1 + loss2 + loss3) / 4.0
    # 优化起
    optimizer = tf.train.AdamOptimizer(learning_rate=lr).minimize(total_loss)

    # 计算四部分的准确率
    correct_prediction0 = tf.equal(tf.argmax(one_hot_labels0, 1), tf.argmax(logits0, 1))
    accuracy0 = tf.reduce_mean(tf.cast(correct_prediction0, tf.float32))

    correct_prediction1 = tf.equal(tf.argmax(one_hot_labels1, 1), tf.argmax(logits1, 1))
    accuracy1 = tf.reduce_mean(tf.cast(correct_prediction1, tf.float32))

    correct_prediction2 = tf.equal(tf.argmax(one_hot_labels2, 1), tf.argmax(logits2, 1))
    accuracy2 = tf.reduce_mean(tf.cast(correct_prediction2, tf.float32))

    correct_prediction3 = tf.equal(tf.argmax(one_hot_labels3, 1), tf.argmax(logits3, 1))
    accuracy3 = tf.reduce_mean(tf.cast(correct_prediction3, tf.float32))

    # 保存模型
    saver = tf.train.Saver()
    sess.run(tf.global_variables_initializer())
    # saver.restore(sess, './ckpt/crack_captcha-10000.ckpt')
    # sess.run(tf.local_variables_initializer())
    # 创建一个协调器来管理线程
    coord = tf.train.Coordinator()
    # 启动QueueRunner,此时文件名列队已经进队
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)

    for i in range(10001):
        # 获取一个批次的数据和标签
        b_image, b_label0, b_label1, b_label2, b_label3 = sess.run(
            [image_batch, label_batch0, label_batch1, label_batch2, label_batch3])
        # 优化模型
        sess.run(optimizer, feed_dict={x: b_image, y0: b_label0, y1: b_label1, y2: b_label2, y3: b_label3})

        # 每100次计算一次loss和准确路
        if i % 100 == 0:
            # 每10000次降低一次学习率
            if i % 5000 == 0:
                sess.run(tf.assign(lr, lr / 3))
            acc0, acc1, acc2, acc3, loss_ = sess.run([accuracy0, accuracy1, accuracy2, accuracy3, total_loss],
                                                     feed_dict={x: b_image, y0: b_label0,
                                                                y1: b_label1,
                                                                y2: b_label2,
                                                                y3: b_label3})
            learning_rate = sess.run(lr)
            print("Iter: %d , Loss:%.3f , Accuracy:%.3f, %.3f, %.3f, %.3f  Learning_rate:%.7f" % (
            i, loss_, acc0, acc1, acc2, acc3, learning_rate))

            # if acc0 > 0.9 and acc1 > 0.9 and acc2 > 0.9 and acc3 > 0.9 :

            if i % 5000 == 0:
                # saver.save(sess,'./ckpt/crack_captcha.ckpt', global_step=1)
                saver.save(sess, CHECKPOINT_DIR + 'crack_captcha-' + str(i) + '.ckpt')
                print('----保存第 %d 次模型----' % i)
                continue
    # 通知其他线程关闭
    coord.request_stop()
    # 其他所有线程关闭之后,这一函数才能返回
    coord.join(threads)
