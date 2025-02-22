import os
from PIL import Image

# 配置路径
base_dir = r"F:\Sense_database_Advance-Edition"
images_dir = {
    'train': os.path.join(base_dir, "images", "train"),
    'val': os.path.join(base_dir, "images", "val")
}
labels_dir = {
    'train': os.path.join(base_dir, "labels", "train"),
    'val': os.path.join(base_dir, "labels", "val")
}
valid_classes = set(range(6))  # 有效类别索引 (0 到 5)

# 检查图片和标签是否一一对应
def check_image_label_matching(images_dir, labels_dir):
    for split in ['train', 'val']:
        print(f"\n检查 {split} 数据集：")
        image_files = {os.path.splitext(f)[0] for f in os.listdir(images_dir[split]) if f.endswith(('.jpg', '.png', '.jpeg'))}
        label_files = {os.path.splitext(f)[0] for f in os.listdir(labels_dir[split]) if f.endswith('.txt')}

        missing_labels = image_files - label_files
        missing_images = label_files - image_files

        if missing_labels:
            print(f"❌ {split} 数据集缺少标签文件的图片: {missing_labels}")
        else:
            print(f"✔ {split} 数据集所有图片都有对应的标签文件！")

        if missing_images:
            print(f"❌ {split} 数据集缺少图片的标签文件: {missing_images}")
        else:
            print(f"✔ {split} 数据集所有标签文件都有对应的图片！")

# 检查空标签文件
def check_empty_labels(labels_dir):
    for split in ['train', 'val']:
        print(f"\n检查 {split} 数据集空标签文件...")
        empty_labels = []
        for root, _, files in os.walk(labels_dir[split]):
            for file in files:
                label_path = os.path.join(root, file)
                if os.path.getsize(label_path) == 0:
                    empty_labels.append(label_path)

        if empty_labels:
            print(f"❌ {split} 数据集以下标签文件为空: {empty_labels}")
            for label_path in empty_labels:
                os.remove(label_path)
                print(f"已删除空标签文件: {label_path}")
        else:
            print(f"✔ {split} 数据集没有空标签文件！")

# 检查标签文件格式
def check_label_format(labels_dir, valid_classes):
    for split in ['train', 'val']:
        print(f"\n检查 {split} 数据集标签文件格式...")
        invalid_labels = []
        for root, _, files in os.walk(labels_dir[split]):
            for file in files:
                label_path = os.path.join(root, file)
                with open(label_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        parts = line.strip().split()
                        if len(parts) != 5:
                            invalid_labels.append((label_path, line.strip()))
                            break
                        class_id, *coords = parts
                        if not class_id.isdigit() or int(class_id) not in valid_classes:
                            invalid_labels.append((label_path, line.strip()))
                            break
                        if not all(p.replace('.', '', 1).isdigit() for p in coords):
                            invalid_labels.append((label_path, line.strip()))
                            break

        if invalid_labels:
            print(f"❌ {split} 数据集以下标签文件格式不正确:")
            for path, line in invalid_labels:
                print(f"  文件: {path}, 错误内容: {line}")
        else:
            print(f"✔ {split} 数据集所有标签文件格式正确！")

# 检查图片文件有效性
def check_image_validity(images_dir):
    for split in ['train', 'val']:
        print(f"\n检查 {split} 数据集图片文件是否有效...")
        invalid_images = []
        for root, _, files in os.walk(images_dir[split]):
            for file in files:
                image_path = os.path.join(root, file)
                try:
                    with Image.open(image_path) as img:
                        img.verify()  # 验证图片是否有效
                except Exception as e:
                    invalid_images.append((image_path, str(e)))

        if invalid_images:
            print(f"❌ {split} 数据集以下图片文件无效:")
            for path, error in invalid_images:
                print(f"  文件: {path}, 错误: {error}")
                os.remove(path)
                print(f"已删除无效图片: {path}")
        else:
            print(f"✔ {split} 数据集所有图片文件有效！")

# 检查类别覆盖性
def check_class_coverage(labels_dir, valid_classes):
    for split in ['train', 'val']:
        print(f"\n检查 {split} 数据集类别覆盖情况...")
        class_counts = {cls: 0 for cls in valid_classes}
        for root, _, files in os.walk(labels_dir[split]):
            for file in files:
                label_path = os.path.join(root, file)
                with open(label_path, 'r') as f:
                    lines = f.readlines()
                    for line in lines:
                        class_id = int(line.strip().split()[0])
                        if class_id in class_counts:
                            class_counts[class_id] += 1

        for cls, count in class_counts.items():
            if count == 0:
                print(f"❌ {split} 数据集类别 {cls} 在标签中没有出现！")
            else:
                print(f"✔ {split} 数据集类别 {cls} 出现次数: {count}")

# 删除旧的缓存文件
def clear_cache(cache_dirs):
    for cache_file in cache_dirs:
        if os.path.exists(cache_file):
            os.remove(cache_file)
            print(f"已删除缓存文件: {cache_file}")
        else:
            print(f"✔ 缓存文件不存在: {cache_file}")

# 主函数
if __name__ == "__main__":
    # 清除缓存路径
    cache_files = [
        r"F:/Sense_database_Advance-Edition/labels/images_train.cache",
        r"F:/Sense_database_Advance-Edition/labels/images_val.cache"
    ]

    check_image_label_matching(images_dir, labels_dir)
    check_empty_labels(labels_dir)
    check_label_format(labels_dir, valid_classes)
    check_image_validity(images_dir)
    check_class_coverage(labels_dir, valid_classes)
    clear_cache(cache_files)

    print("\n✅ 数据集检查和修复完成！")
