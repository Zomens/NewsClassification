def read_labelFile(file):
    label_w2n = {}
    label_n2w = {}
    with open(file, 'r', encoding='utf_8') as file:
        for line in file:
            line = line.strip()
            line = line.split(' ')
            name_w = line[0]
            name_n = int(line[1])
            label_w2n[name_w] = name_n
            label_n2w[name_n] = name_w
    return label_w2n, label_n2w

def get_worddict(file):
    with open(file, 'r', encoding='utf_8') as file:
        word2ind = {}
        for line in file:
            line = line.strip()
            line = line.split(' ')
            word2ind[line[0]] = int(line[1])
    
    ind2word = {word2ind[w]:w for w in word2ind}
    return word2ind, ind2word
