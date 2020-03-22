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
        first = True
        out = "["
        for row in self.rows:
            if first:
                out += "["
                first = False
            else:
                out += "\n ["
            out += (", ".join(str(cell) for cell in row)) + "]"
        return out + "]"

class Mat1x2f(Matf):
    """ TODO: mas
    """

    def __init__(self,
        m00: float, m01):
       
        self.m00 = m00
        self.m01 = m01

    def transpose(self):
        return Mat2x1f(
                self.m00,
                self.m01
            )

class Mat2x1f(Matf):

    def __init__(self,
        m00: float,
        m10: float):
        
        self.m00 = m00
        self.m10 = m10

class Mat1x3f(Matf):

    def __init__(self,
        m00: float, m01: float, m02: float):
        
        self.m00 = m00
        self.m01 = m01
        self.m02 = m02

class Mat2x3f(Matf):

    def __init__(self,
        m00: float, m01: float, m02: float,
        m10: float, m11: float, m12: float):
        
        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12

    def transpose(self):
        return Mat3x2f(
            self.m00, self.m10,
            self.m01, self.m11,
            self.m02, self.m12)

class Mat3x1f(Matf):

    def __init__(self, m00:float, m10: float, m20: float):
        
        self.m00 = m00
        self.m10 = m10
        self.m20 = m20

class Mat3x2f(Matf):

    def __init__(self, m00: float, m01: float, m10: float, m11: float, m20: float, m21: float):
        
        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11
        self.m20 = m20
        self.m21 = m21

class Mat1x4(Matf):

    def __init__(self, m00: float, m01: float, m02: float, m03:float):

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m03 = m03

class Mat2x4(Matf):

    def __init__(self, m00: float, m01: float, m10: float, m11: float, m20: float, m21: float,
        m30: float, m31: float):

        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11
        self.m20 = m20
        self.m21 = m21

class Mat3x4(Matf):

    def __init__(self, m00: float, m01: float, m02: float, m10: float, m11: float, m12: float,
        m20: float, m21: float, m22: float, m30: float, m31: float, m32: float):

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22
        self.m30 = m30
        self.m31 = m31
        self.m32 = m32
        
class Mat4x1(Matf):

    def __init__(self, m00: float, m10: float, m20: float, m30:float):

        self.m00 = m00
        self.m10 = m10
        self.m20 = m20
        self.m30 = m30

class Mat4x2(Matf):

    def __init__(self, m00: float, m01: float, m10: float, m11: float, m20: float, m21: float,
        m30: float, m31: float):

        self.m00 = m00
        self.m01 = m01
        self.m10 = m10
        self.m11 = m11
        self.m20 = m20
        self.m21 = m21
        self.m30 = m30
        self.m31 = m31

class Mat4x3(Matf):

    def __init__(self, m00: float, m01: float, m02: float, m10: float, m11: float, m12: float,
        m20: float, m21: float, m22: float, m30: float, m31: float, m32: float):

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22
        self.m30 = m30
        self.m31 = m31
        self.m32 = m32

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

        self.row0 = [self.m00, self.m01]
        self.row1 = [self.m10, self.m11]
        self.col0 = [self.m00, self.m10]
        self.col1 = [self.m01, self.m11]

        self.rows.append(self.row0)
        self.rows.append(self.row1)
        self.cols.append(self.col0)
        self.cols.append(self.col1)

class Mat3x3f(Matf):

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
			TODO
        """
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22

        self.row0 = [self.m00, self.m01, self.m02]
        self.row1 = [self.m10, self.m11, self.m12]
        self.row2 = [self.m20, self.m21, self.m22]
        self.col0 = [self.m00, self.m10, self.m20]
        self.col1 = [self.m01, self.m11, self.m21]
        self.col2 = [self.m02, self.m12, self.m22]

        self.rows.append(self.row0)
        self.rows.append(self.row1)
        self.rows.append(self.row2)
        self.cols.append(self.col0)
        self.cols.append(self.col1)
        self.cols.append(self.col2)

class Mat4x4f(Matf):

    def __init__(self,
        m00 : float, m01 : float, m02 : float, m03: float,
        m10 : float, m11 : float, m12 : float, m13: float,
        m20 : float, m21 : float, m22 : float, m23: float,
        m30 : float, m31 : float, m32 : float, m33: float
		):
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
			TODO
        """
        super().__init__()

        self.m00 = m00
        self.m01 = m01
        self.m02 = m02
        self.m03 = m03
        self.m10 = m10
        self.m11 = m11
        self.m12 = m12
        self.m13 = m13
        self.m20 = m20
        self.m21 = m21
        self.m22 = m22
        self.m23 = m23
        self.m30 = m30
        self.m31 = m31
        self.m32 = m32
        self.m33 = m33

        self.row0 = [self.m00, self.m01, self.m02, self.m03]
        self.row1 = [self.m10, self.m11, self.m12, self.m13]
        self.row2 = [self.m20, self.m21, self.m22, self.m23]
        self.row3 = [self.m30, self.m31, self.m32, self.m33]

        self.col0 = [self.m00, self.m10, self.m20, self.m30]
        self.col1 = [self.m01, self.m11, self.m21, self.m31]
        self.col2 = [self.m02, self.m12, self.m22, self.m32]
        self.col3 = [self.m03, self.m13, self.m23, self.m33]

        self.rows.append(self.row0)
        self.rows.append(self.row1)
        self.rows.append(self.row2)
        self.rows.append(self.row3)
        self.cols.append(self.col0)
        self.cols.append(self.col1)
        self.cols.append(self.col2)
        self.cols.append(self.col3)