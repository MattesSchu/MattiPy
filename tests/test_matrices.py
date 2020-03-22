from matti import helpers

import unittest

class TestMat1x2(unittest.TestCase):

    mat1x2f = helpers.Mat1x2f(1, 2)

    def test_indices(self):

        self.assertEqual(self.mat1x2f.m00, 1)
        self.assertEqual(self.mat1x2f.m01, 2)

    def test_transpose(self):

        mat2x1f = self.mat1x2f.transpose()

        self.assertEqual(mat2x1f.m00, 1)
        self.assertEqual(mat2x1f.m10, 2)

class TestMat2x2(unittest.TestCase):
    
    mat2x2f = helpers.Mat2x2f(
        1, 2,
        3, 4,
    )

    def test_mat_row(self):

        self.assertEqual(self.mat2x2f.row0, [1, 2])
        self.assertEqual(self.mat2x2f.row1, [3, 4])

    def test_mat_col(self):

        self.assertEqual(self.mat2x2f.col0, [1, 3])
        self.assertEqual(self.mat2x2f.col1, [2, 4])

    def test_mat_members(self):

        self.assertEqual(self.mat2x2f.m00, 1)
        self.assertEqual(self.mat2x2f.m01, 2)
        self.assertEqual(self.mat2x2f.m10, 3)
        self.assertEqual(self.mat2x2f.m11, 4)

    def test_mat_string(self):

        res = "[[1, 2]\n [3, 4]]" 

        self.assertEqual(str(self.mat2x2f), res)

class TestMat3x3(unittest.TestCase):

    mat3x3f = helpers.Mat3x3f(
        1, 2, 3,
        4, 5, 6,
        7, 8, 9)

    def test_mat_row(self):

        self.assertEqual(self.mat3x3f.row0, [1, 2, 3])
        self.assertEqual(self.mat3x3f.row1, [4, 5, 6])
        self.assertEqual(self.mat3x3f.row2, [7, 8, 9])

    def test_mat_col(self):

        self.assertEqual(self.mat3x3f.col0, [1, 4, 7])
        self.assertEqual(self.mat3x3f.col1, [2, 5, 8])
        self.assertEqual(self.mat3x3f.col2, [3, 6, 9])

    def test_mat_members(self):

        self.assertEqual(self.mat3x3f.m00, 1)
        self.assertEqual(self.mat3x3f.m01, 2)
        self.assertEqual(self.mat3x3f.m02, 3)
        self.assertEqual(self.mat3x3f.m10, 4)
        self.assertEqual(self.mat3x3f.m11, 5)
        self.assertEqual(self.mat3x3f.m12, 6)
        self.assertEqual(self.mat3x3f.m20, 7)
        self.assertEqual(self.mat3x3f.m21, 8)
        self.assertEqual(self.mat3x3f.m22, 9)

    def test_mat_string(self):

        res = "[[1, 2, 3]\n [4, 5, 6]\n [7, 8, 9]]" 

        self.assertEqual(str(self.mat3x3f), res)

class TestMat4x4(unittest.TestCase):

    mat4x4f = helpers.Mat4x4f(
             1,  2,  3,  4,
             5,  6,  7,  8,
             9, 10, 11, 12,
            13, 14, 15, 16,
        )

    def test_mat_row(self):

        self.assertEqual(self.mat4x4f.row0, [1, 2, 3, 4])
        self.assertEqual(self.mat4x4f.row1, [5, 6, 7, 8])
        self.assertEqual(self.mat4x4f.row2, [9, 10, 11, 12])
        self.assertEqual(self.mat4x4f.row3, [13, 14, 15, 16])

    def test_mat_col(self):

        self.assertEqual(self.mat4x4f.col0, [1, 5, 9, 13])
        self.assertEqual(self.mat4x4f.col1, [2, 6, 10, 14])
        self.assertEqual(self.mat4x4f.col2, [3, 7, 11, 15])
        self.assertEqual(self.mat4x4f.col3, [4, 8, 12, 16])

    def test_mat_members(self):

        self.assertEqual(self.mat4x4f.m00, 1)
        self.assertEqual(self.mat4x4f.m01, 2)
        self.assertEqual(self.mat4x4f.m02, 3)
        self.assertEqual(self.mat4x4f.m03, 4)
        self.assertEqual(self.mat4x4f.m10, 5)
        self.assertEqual(self.mat4x4f.m11, 6)
        self.assertEqual(self.mat4x4f.m12, 7)
        self.assertEqual(self.mat4x4f.m13, 8)
        self.assertEqual(self.mat4x4f.m20, 9)
        self.assertEqual(self.mat4x4f.m21, 10)
        self.assertEqual(self.mat4x4f.m22, 11)
        self.assertEqual(self.mat4x4f.m23, 12)
        self.assertEqual(self.mat4x4f.m30, 13)
        self.assertEqual(self.mat4x4f.m31, 14)
        self.assertEqual(self.mat4x4f.m32, 15)
        self.assertEqual(self.mat4x4f.m33, 16)

    def test_mat_string(self):

        res = "[[1, 2, 3, 4]\n [5, 6, 7, 8]\n [9, 10, 11, 12]\n [13, 14, 15, 16]]" 

        self.assertEqual(str(self.mat4x4f), res)

if __name__ == '__main__':
    unittest.main()
