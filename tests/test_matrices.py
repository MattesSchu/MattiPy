from matti import matrices

import unittest

class TestMat1x2(unittest.TestCase):
    mat1x2f = matrices.Mat1x2f(1, 2)

    def test_transpose(self):
        mat2x1f = self.mat1x2f.transpose()
        self.assertEqual(mat2x1f.m00(), 1)
        self.assertEqual(mat2x1f.m10(), 2)

    def test_get_rows(self):
        rows = self.mat1x2f.get_rows()
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][0], 1)
        self.assertEqual(rows[0][1], 2)
    
    def test_get_cols(self):
        cols = self.mat1x2f.get_cols()
        self.assertEqual(len(cols), 2)
        self.assertEqual(cols[0][0], 1)
        self.assertEqual(cols[1][0], 2)

class TestMat2x1(unittest.TestCase):
    mat2x1f = matrices.Mat2x1f(1, 2)

    def test_transpose(self):
        mat1x2f = self.mat2x1f.transpose()
        self.assertEqual(mat1x2f.m00(), 1)
        self.assertEqual(mat1x2f.m01(), 2)

    def test_get_rows(self):
        rows = self.mat2x1f.get_rows()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0][0], 1)
        self.assertEqual(rows[1][0], 2)
    
    def test_get_cols(self):
        cols = self.mat2x1f.get_cols()
        self.assertEqual(len(cols), 1)
        self.assertEqual(cols[0][0], 1)
        self.assertEqual(cols[0][1], 2)

class TestMat2x2(unittest.TestCase):
    mat2x2f = matrices.Mat2x2f(
        1, 2,
        3, 4,
    )

    def test_transpose(self):
        mat2x2f_transposed = self.mat2x2f.transpose()
        self.assertEqual(mat2x2f_transposed.m00(), 1)
        self.assertEqual(mat2x2f_transposed.m01(), 3)
        self.assertEqual(mat2x2f_transposed.m10(), 2)
        self.assertEqual(mat2x2f_transposed.m11(), 4)

    def test_get_rows(self):
        rows = self.mat2x2f.get_rows()
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0][0], 1)
        self.assertEqual(rows[0][1], 2)
        self.assertEqual(rows[1][0], 3)
        self.assertEqual(rows[1][1], 4)
    
    def test_get_cols(self):
        cols = self.mat2x2f.get_cols()
        self.assertEqual(len(cols), 2)
        self.assertEqual(cols[0][0], 1)
        self.assertEqual(cols[0][1], 3)
        self.assertEqual(cols[1][0], 2)
        self.assertEqual(cols[1][1], 4)

    def test_dot_ones(self):
        ones = matrices.Mat2x2f(1,1,1,1)
        res = matrices.dot(ones, ones)
        self.assertEqual(res.m00(), 2)
        self.assertEqual(res.m01(), 2)
        self.assertEqual(res.m10(), 2)
        self.assertEqual(res.m11(), 2)

    def test_dot_zeroes(self):
        ones = matrices.Mat2x2f(0, 0, 0, 0)
        res = matrices.dot(ones, ones)
        self.assertEqual(res.m00(), 0)
        self.assertEqual(res.m01(), 0)
        self.assertEqual(res.m10(), 0)
        self.assertEqual(res.m11(), 0)

    def test_dot_easy(self):
        ones = matrices.Mat2x2f(1, 2, 3, 4)
        res = matrices.dot(ones, ones)
        self.assertEqual(res.m00(), 7)
        self.assertEqual(res.m01(), 10)
        self.assertEqual(res.m10(), 15)
        self.assertEqual(res.m11(), 22)

class TestMatricesMultiplication(unittest.TestCase):
    first = matrices.Mat3x1f(1, 2, 3)
    second = matrices.Mat1x3f(1, 2, 3)
    single = matrices.Mat1x1f(2)

    def test_3x1_dot_1x3(self):
        res = matrices.dot(self.first, self.second)
        self.assertEqual(res.col_dimension(), 3)
        self.assertEqual(res.row_dimension(), 3)
        self.assertEqual(res.m00(), 1)
        self.assertEqual(res.m01(), 2)
        self.assertEqual(res.m02(), 3)
        self.assertEqual(res.m10(), 2)
        self.assertEqual(res.m11(), 4)
        self.assertEqual(res.m12(), 6)
        self.assertEqual(res.m20(), 3)
        self.assertEqual(res.m21(), 6)
        self.assertEqual(res.m22(), 9)

    def test_1x3_dot_3x1(self):
        res = matrices.dot(self.second, self.first)
        self.assertEqual(res.col_dimension(), 1)
        self.assertEqual(res.row_dimension(), 1)
        self.assertEqual(res.m00(), 14)

    def test_1x1_dat_1x3f(self):
        res = matrices.dot(self.single, self.second)
        self.assertEqual(res.col_dimension(), 3)
        self.assertEqual(res.row_dimension(), 1)

class Test2Matrices(unittest.TestCase):
    first = matrices.Mat1x2f(1, 2)
    second = matrices.Mat1x2f(2, 1)

    def test_members(self):
        self.assertEqual(self.first.m00(), 1)
        self.assertEqual(self.first.m01(), 2)
        self.assertEqual(self.second.m00(), 2)
        self.assertEqual(self.second.m01(), 1)

    def test_add(self):
        sum_of_2 = self.first + self.second
        self.assertEqual(sum_of_2.m00(), 3)
        self.assertEqual(sum_of_2.m01(), 3) 

    def test_sub(self):
        sub_of_2 = self.first - self.second
        self.assertEqual(sub_of_2.m00(), -1)
        self.assertEqual(sub_of_2.m01(), 1)

if __name__ == '__main__':
    unittest.main()
