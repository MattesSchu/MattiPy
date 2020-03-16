from sys import float_info

class Matf:

    def __init__(self):
        """ Rows run horizontally, cols run vertically
            It is a row-major repesentation

            Example:   
                | 100 100 100 |    | m00 m01 m02 |
                | 200 200 200 | -> | m10 m11 m12 |
                | 300 300 300 |    | m20 m21 m22 |
                
                A[0][0] = m00
                A[0][1] = m01
                ...
                A[i][j] = mij
        """
        self.rows = []
        self.cols = []
        self.max = float_info.min
        self.min = float_info.max

    def __str__(self) -> str:
        """ Prints the Matrix
        """
        out = "[["
        for row in self.rows:
            out += (", ".join(str(cell) for cell in row)) + "]\n"
        return out + "]]"

class Mat2x2f(Matf):

    def __init__(self, 
        m00 : float, m01 : float,
        m10 : float, m11 : float):
        """Initialization of the 2x2 Matrix in column Major representation.
        
        Arguments:
            m00 {float} -- [description]
            m01 {float} -- [description]
            m10 {float} -- [description]
            m11 {float} -- [description]
        """
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11

        self.row0 = [m00, m01]
        self.row1 = [m10, m11]
        self.col0 = [m00, m10]
        self.col1 = [m01, m11]

        self.rows.append(self.row0)
        self.rows.append(self.row1)
        self.cols.append(self.col0)
        self.cols.append(self.col1)

class Mat3x3f:

    def __init__(self,
        m00 : float, m01 : float, m02 : float,
        m10 : float, m11 : float, m12 : float,
        m20 : float, m21 : float, m22 : float):
        """Initialization of the 3x3 Matrix in column Major representation.
        
        Arguments:
            m00 {float} -- [description]
            m01 {float} -- [description]
            m02 {float} -- [description]
            m10 {float} -- [description]
            m11 {float} -- [description]
            m12 {float} -- [description]
            m20 {float} -- [description]
            m21 {float} -- [description]
            m22 {float} -- [description]
        """
        super().__init__()



test = Mat2x2f(1, 2, 3, 4)

print(test)