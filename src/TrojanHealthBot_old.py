class TrojanHealthBot:
    weights = []
    bias = 0
        
    def train(self, filename, numFeatures):
        self.weights = [0] * numFeatures
        self.bias = 0
        for run in range(0, 100):
            trainFile = open(filename)
            for line in trainFile:
                vals = line.split(',')
                y = int(vals[0])
                act = 0
                
                for i in range(0, numFeatures):
    ##                print(str(vals[i + 1]), end=' ')
                    act = act + (int(vals[i + 1]) * self.weights[i]) + self.bias
    ##            print(str(act))
    ##            print(y)
    ##            print(act * y)
                    
                if act * y <= 0:
                    for i in range(0, numFeatures):
                        self.weights[i] = self.weights[i] + int(vals[i + 1]) * y
                    self.bias = self.bias + y
                    
            for i in range(0, numFeatures):
                print(self.weights[i], end=' ')
            print('')
            print('self.bias: ' + str(self.bias))


    def test(self, filename, numFeatures):
        testFile = open(filename)
        linecount = 0
        correct = 0
        incorrect = 0
        for line in testFile:
            linecount = linecount + 1
            vals = line.split(',')
            y = int(vals[0])
            act = 0
            
            for i in range(0, numFeatures):
                act = act + (int(vals[i + 1]) * self.weights[i]) + self.bias

            if act * y <= 0:
                print('line: ' + str(linecount) + '  \tpredicted: ' + str(act) + '\t\tactual: ' + str(y) + 'no')
                incorrect = incorrect + 1
            else:
                print('line: ' + str(linecount) + '  \tpredicted: ' + str(act) + '\t\tactual: ' + str(y) + 'yes')
                correct = correct + 1
                
        print('correct: ' + str(correct) + '\tincorrect: ' + str(incorrect))
        
    
    def __init__(self):
        config = open('../config.txt')
        numFeatures = int(config.readline().strip())
        trn = '..\\' + config.readline().strip()
        tst = '..\\' + config.readline().strip()
        self.train(trn, numFeatures)
        self.test(tst, numFeatures)

TrojanHealthBot()
