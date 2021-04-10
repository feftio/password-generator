class Password:

    def __init__(self, password, A=None, P=None, V=None, T=None):
        self.password = password
        self.L = len(password)
        self.A = A
        self.P = P
        self.V = V
        self.T = T
    
    def __str__(self):
        return self.password