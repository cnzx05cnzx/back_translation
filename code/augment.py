import utils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input", required=True, type=str, help="原始数据的输入文件目录")
ap.add_argument("--output", required=False, type=str, help="增强数据后的输出文件目录")
args = ap.parse_args()


def back_trans(train_orig, output_file):
    writer = open(output_file, 'w', encoding='utf-8')
    lines = open(train_orig, 'r', encoding='utf-8').readlines()

    print("正在使用回译生成增强语句...")
    for i, line in enumerate(lines):
        parts = line[:-1].split('\t')  # 使用[:-1]是把\n去掉了
        # print(parts)
        label = parts[0]
        sentence = parts[1]
        aug_sentences = utils.all_trans(sentence)
        for aug_sentence in aug_sentences:
            writer.write(label + "\t" + aug_sentence + '\n')

    writer.close()
    print("已生成增强语句!")


if __name__ == "__main__":
    back_trans(args.input, args.output)
