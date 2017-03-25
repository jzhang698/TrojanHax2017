class TrojanHealthBot:
    weights = []
    bias = 0
        
    def train(self, filename, numFeatures):
        weights = [0] * numFeatures
        bias = 0
        trainFile = open(filename)
        for line in trainFile:
            vals = line.split(',')
            act = 0
            
            for i in range(0, numFeatures):
                if vals[i + 1] == 0:
                    vals[i + 1] = -1
                act = act + (int(vals[i + 1]) * weights[i]) + bias
                
            if vals[0] == 0:
                y = -1
            else:
                y = 1
                
            if act * y <= 0:
                for i in range(0, numFeatures):
                    weights[i] = weights[i] + int(vals[i + 1]) * y
                bias = bias + y
                
        for i in range(0, numFeatures):
            print(weights[i], end='')
        print('')
        print('bias: ' + str(bias))


    def test(self, filename, numFeatures):
        testFile = open(filename)
        
    
    def __init__(self):
        config = open('../config.txt')
        numFeatures = int(config.readline().strip())
        trn = '..\\' + config.readline().strip()
        tst = '..\\' + config.readline().strip()
        self.train(trn, numFeatures)
        self.test(tst, numFeatures)

TrojanHealthBot()
