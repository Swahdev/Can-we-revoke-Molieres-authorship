
import os
import glob


def each_cons(iterable, n):
    return [iterable[i:i + n] for i in range(len(iterable) - n + 1)]


def construction_graphes(filenames, filename_to_compare, ngram=4):
    batch_counts = {}

    with open(filename_to_compare, 'r') as file_to_compare:
        compares_lines = file_to_compare.readlines()
        compares_batchs = each_cons(compares_lines, ngram)
        for filename in filenames:
            print("processing", filename)
            with open(filename, 'r') as file:
                lines = file.readlines()
                for line_batch in each_cons(lines, ngram):
                    for compare_batch in compares_batchs:
                        if line_batch == compare_batch:
                            tuple_line_batch = tuple(line_batch)
                            batch_counts[tuple_line_batch] = batch_counts.get(
                                tuple_line_batch, 0) + 1

    print("new text is similar at :", len(
        batch_counts.keys()) / len(compares_batchs) * 100, "%")


def main():
    dossier = 'Code/fichier2'
    filenames = glob.glob(os.path.join(dossier, '*.txt'))

    construction_graphes(filenames, "Fichiers_Pretraitement/moliere_avare.txt")


if __name__ == '__main__':
    main()
