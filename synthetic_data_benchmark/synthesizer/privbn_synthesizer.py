from .synthesizer_base import SynthesizerBase, run
import json
import numpy as np
import os
import subprocess
import shutil
from .synthesizer_utils import CONTINUOUS, ORDINAL, CATEGORICAL

def try_mkdirs(dir):
    try:
        os.makedirs(dir)
    except:
        pass

class PrivBNSynthesizer(SynthesizerBase):
    """docstring for IdentitySynthesizer."""
    def __init__(self):
        assert os.path.exists("privbayes/privBayes.bin")

    def train(self, train_data):
        self.train_data = train_data

    def generate(self, n):
        try_mkdirs("__privbn_tmp/data")
        try_mkdirs("__privbn_tmp/log")
        try_mkdirs("__privbn_tmp/output")
        shutil.copy("privbayes/privBayes.bin", "__privbn_tmp/privBayes.bin")
        d_cols = []
        with open("__privbn_tmp/data/real.domain", "w") as f:
            for id_, info in enumerate(self.meta):
                if info['type'] in [CATEGORICAL, ORDINAL]:
                    print("D", end='', file=f)
                    counter = 0
                    for i in range(info['size']):
                        if i > 0 and i % 4 == 0:
                            counter += 1
                            print(" {", end='', file=f)
                        print("", i, end='', file=f)
                    print(" }" * counter, file=f)
                    d_cols.append(id_)
                else:
                    minn = info['min']
                    maxx = info['max']
                    d = (maxx - minn）* 0.03
                    minn -= d
                    maxx += d
                    print("C", minn, maxx, file=f)

        with open("__privbn_tmp/data/real.dat", "w") as f:
            for raw in self.train_data:
                for id_, col in enumerate(raw):
                    if id_ in d_cols:
                        print(int(col), end=' ', file=f)
                    else:
                        print(col, end=' ', file=f)
                print(file=f)

        privbayes = os.path.realpath("__privbn_tmp/privBayes.bin")
        subprocess.call([privbayes, "real", str(n), "1", "5"], cwd="__privbn_tmp")
        subprocess.call([privbayes, "real", str(n), "1", "10"], cwd="__privbn_tmp")

        d1 = np.loadtxt("__privbn_tmp/output/syn_real_eps10_theta5_iter0.dat")
        d2 = np.loadtxt("__privbn_tmp/output/syn_real_eps10_theta10_iter0.dat")

        return [(5, d1), (10, d2)]

    def init(self, meta, working_dir):
        self.meta = meta


if __name__ == "__main__":
    run(PrivBNSynthesizer())
