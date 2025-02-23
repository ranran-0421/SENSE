# 📚 SENSE数据集
  SENSE数据集是为解决自主驾驶场景中突发变化和极端天气下目标检测模型性能下降的问题而设计。基于开源数据集，结合合成技术，构建了针对自动驾驶场景下图像数据分布突然性变化的高质量评测数据集。相比于传统的数据集，它不仅保留了主流数据集的优势，还在场景突变和极端天气的覆盖上进行了有针对性的优化。
  
# 📝 SENSE数据集分类 
## 1.真实图像
真实图像来自多个公开开源数据集，包括 **BDD100K**、**ONCE** 和 **SODA10M**，我们从中筛选出具有突发变化的场景，重点选取极端环境条件下的图像，如大雾、大雨、大雪等情境。详细的真实图像数据存储在`真实图像数据集`文件夹中。
## 2.合成数据集
合成数据部分涵盖五大类效果：  
1. **噪声添加**：通过加入高斯噪声、散粒噪声和脉冲噪声等，模拟低光照、信号干扰或传感器质量较差的情况下图像可能出现的噪点，提升模型在恶劣感知环境中的鲁棒性。  
2. **模糊处理**：包括散焦模糊、磨砂玻璃模糊、运动模糊和变焦模糊，模拟摄像头失焦、雨水附着、快速运动或变焦时产生的模糊现象，增强模型对图像质量下降的适应能力。  
3. **天气模拟**：通过合成雪、霜冻、雾霾等天气效果，模拟极端天气下的视觉挑战，帮助模型在雨雪、雾霾等复杂天气条件下保持较高的检测准确率。  
4. **属性调节**：调整图像的亮度、对比度，并应用弹性变形技术，模拟传感器和环境因素对图像质量的影响，提升模型对光照变化和环境干扰的适应能力。  
5. **降质处理**：包括像素化和JPEG压缩，模拟低带宽或图像传输中的压缩，帮助提升模型在低质量图像下的检测能力，确保在传输受限或网络不稳定的情况下有效工作。
   
# 🔍 目录说明：
- **test/**: 包含测试集数据，用于评估模型的性能。此目录下有两个子目录：
  - `images/`：存放测试集图像。
  - `labels/`：存放测试集的标签文件，通常为每张图片的标注信息。
- **train/**: 包含训练集数据，用于模型的训练过程。此目录也有两个子目录：
  - `images/`：存放训练集图像。
  - `labels/`：存放训练集的标签文件，用于监督学习。
