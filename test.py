import re

# 输入数据
data = """
(1) Chen Yadang; Jiang Ren; Zheng Yuhui; Sheng Bin; Yang ZhiXin; Wu Enhua; Dual Branch Multi-Level Semantic Learning for Few-Shot Segmentation, IEEE Transactions on Image Processing, 2024, 33：1432-1447. SCIE. 第一标注
(2) Zhang Guoqing; Liu Jie; Chen Yuhao; Zheng Yuhui; Zhang Hongwei; Multi-biometric Unified Network for Cloth-changing Person Re-Identification, IEEE Transactions on Image Processing, 2023, 32：4555-4566. 第一标注
(3) Shen Xiaobo; Zhou Yue; Yuan Yunhao; Yang xichen; Lan kong; Zheng Yuhui; Contrastive Transformer Hashing for Compact Video Representation, IEEE Transactions on Image Processing, 2023, 32：5992-6003. SCIE. 第一标注
(4) Zhang, Guoqing; Ge, Yu; Dong, Zhicheng; Wang, Hao; Zheng, Yuhui; Chen, Shengyong; Deep High-Resolution Representation Learning for Cross-Resolution Person Re-Identification, IEEE Transactions on Image Processing, 2021, 30：8913-8925. SCIE. 第一标注
(5) Guan Tuxin; Li Chaofeng; Zheng Yuhui; Wu Xiaojun; Bovik Alan C.; Dual-Stream Complex-Valued Convolutional Network for Authentic Dehazed Image Quality Assessment, IEEE Transactions on Image Processing, 2024, 33：466-478. SCIE. 第一标注
(6) Shen Xiaobo; Wu Wei; Wang Xiaxin; Zheng Yuhui; Multiple Riemannian Kernel Hashing for Large-Scale Image Set Classification and Retrieval, IEEE Transactions on Image Processing, 2024, 33：4261-4273. SCIE. 第一标注
(7) Sun Le; He Chengxun; Zheng Yuhui; Wu Zebin; Jeon Byeungwoo; Tensor Cascaded-Rank Minimization in Subspace: A Unified Regime for Hyperspectral Image Low-Level Vision, IEEE Transactions on Image Processing, 2023, 32：100-115. SCIE. 第一标注
(8) He Jianfeng; Zhang Tianzhu; Zheng Yuhui; Xu Mingliang; Zhang Yongdong; Wu Feng; Consistency Graph Modeling for Semantic Correspondence, IEEE Transactions on Image Processing, 2021, 30：4932-4946. SCIE. 第一标注
(9) Yu Qianqian; Fan Keqi; Zheng Yuhui; Domain Adaptive Transformer Tracking Under Occlusions, IEEE Transactions on Multimedia, 2023, 25：1452-1461. SCIE. 第一标注
(10) Zheng Yuhui; Zhang Yan; Xiao Bin; Target-Aware Transformer Tracking, IEEE Transactions on Circuits and Systems for Video Technology, 2023, 33(9)：4542-4551. SCIE. 第一标注
(11) Tian Qing; Sun Heyang; Peng Shun; Zheng Yuhui; Wan Jun; Zhang Lei; DCL: Dipolar Confidence Learning for Source-Free Unsupervised Domain Adaptation, IEEE Transactions on Circuits and Systems for Video Technology, 2024, 34(6)：4342-4353. SCIE. 第一标注
(12) Shen Xiaobo; Tang Yunpeng; Zheng Yuhui; Yuan YunHao; Sun Quan-Sen; Unsupervised Multiview Distributed Hashing for Large-Scale Retrieval, IEEE Transactions on Circuits and Systems for Video Technology, 2022, 32(12)：8837-8848. SCIE. 第一标注
(13) Zhang Guoqing; Yang Junchuan; Zheng Yuhui; Wang Ye; Wu Yi; Chen, Shengyong; Hybrid-attention guided network with multiple resolution features for person re-identification, Information Sciences, 2021, 578：525-538. SCIE. 第一标注
(14) Chen Yadang; Zhang Dingwei; Zheng Yuhui; Yang Zhi-Xin; Wu Enhua; Zhao Haixing; Boosting Video Object Segmentation via Robust and Efficient Memory Network, IEEE Transactions on Circuits and Systems for Video Technology, 2024, 34(5)：3340-3352. SCIE. 第一标注
(15) Shen Xiaobo; Ong Yew-Soon; Mao Zheng; Pan Shirui; Liu Weiwei; Zheng, Yuhui; Compact network embedding for fast node classification, Pattern Recognition, 2023, 136. SCIE. 第一标注
(16) He Chengxun; Sun Le; Huang Wei; Zhang Jianwei; Zheng Yuhui; Jeon Byeungwoo; TSLRLN: Tensor subspace low-rank learning with non-local prior for hyperspectral image mixed denoising, Signal Processing, 2021, 184. SCIE. 第一标注
(17) Wang Jinwei; Zhao Junjie; Yin Qilin; Luo Xiangyang; Zheng Yuhui; Shi YunQing; Jha Sunil Kr; SmsNet: A New Deep Convolutional Neural Network Model for Adversarial Example Detection, IEEE Transactions on Multimedia, 2022, 24：230-244. SCIE. 第一标注
(18) Zhang Guoqing; Luo Zhiyuan; Chen Yuhao; Zheng Yuhui; Lin Weisi; Illumination Unification for Person Re-Identification, IEEE Transactions on Circuits and Systems for Video Technology, 2022, 32(10)：6766-6777. SCIE. 第一标注
(19) Zheng Yuhui; Liu Xinyan; Xiao Bin; Cheng Xu; Wu Yi; Chen Shengyong; Multi-Task Convolution Operators with Object Detection for Visual Tracking, IEEE Transactions on Circuits and Systems for Video Technology, 2022, 32(10)：8204-8216. SCIE. 第一标注
(20) Wang Tao; Li Haochen; Zheng Yuhui; Sun Quan-sen; One-click-based Perception for Interactive Image Segmentation, IEEE Transactions on Neural Networks and Learning Systems, 2024, 35(10)：13975-13989. SCIE. 第一标注
(21) Ye, Qiaolin; Huang, Peng; Zhang, Zhao; Zheng, Yuhui; Fu, Liyong; Yang, Wankou; Multiview Learning With Robust Double-Sided Twin SVM, IEEE Transactions on Cybernetics, 2022, 52(12)：12745-12758. SCIE. 第一标注
(22) Guan Tuxin; Li Chaofeng; Gu Ke; Liu Hantao; Zheng Yuhui; Wu Xiao-jun; Visibility and Distortion Measurement for No-Reference Dehazed Image Quality Assessment via Complex Contourlet Transform, IEEE Transactions on Multimedia, 2023, 25：3934-3949. SCIE. 第一标注
"""

# 定义正则表达式，提取所需字段
pattern = r"\((\d+)\)\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);\s([A-Za-z\s,]+);"

# 匹配并提取数据
matches = re.findall(pattern, data)

# 输出结果
for match in matches:
    print(f"序号: {match[0]}")
    print(f"年份: {match[1]}")
    print(f"第一作者: {match[2]}")
    print(f"论文名: {match[3]}")
    print(f"期刊名: {match[4]}")
    print("-------------------")