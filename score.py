class Score:
    
    
    def __init__(self, data):
        items = data.split(',')

        self._sid = items[0]
        self._name = items[1]
        self._kor = float(items[2])
        self._eng = float(items[3])
        self._mat = float(items[4])
    
    @property
    def sid(self):
        return self._sid

    @property
    def name(self):
        return self._name

    @property
    def kor(self):
        return self._kor

    @property
    def eng(self):
        return self._eng

    @property
    def mat(self):
        return self._mat

    @property
    def total(self):
        return self._kor + self._eng + self._mat

    @property
    def avg(self):
        return (self._kor + self._eng + self._mat) / 3