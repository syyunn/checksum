import hashlib


def check_sha1(filename):
    sha1 = hashlib.sha1()
    buf_size = 65536  # lets read stuff in 64kb chunks!
    with open(filename, 'rb') as f:
        while True:
            data = f.read(buf_size)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()


if __name__ == "__main__":
    from os import listdir
    from os.path import isfile, join

    path = '/Users/suyeol/Downloads/PATSTAT 2020 AUTUMN'
    files = sorted([f for f in listdir(path) if isfile(join(path, f)) and f.endswith('.zip')])
    texts = sorted([t for t in listdir(path) if isfile(join(path, t)) and t.endswith('.txt')])

    for file, text in zip(files, texts):
        sha1 = check_sha1(join(path, file))
        text = open(join(path, text), "r").read()

        print(sha1.upper(), text)
        assert sha1.upper() == text, "NOT SAME"
        pass
