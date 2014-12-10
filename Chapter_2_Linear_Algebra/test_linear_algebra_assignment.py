import numpy as np
import nose.tools as n
import linear_algebra_assignment as problems


def test_one():
    answer = np.linspace(0, 100, 1)
    result = problems.one()
    n.assert_equal(result.shape, (100,))


def test_two():
    result = problems.two()
    n.assert_equal(result.shape, (100,1))


def test_three():
    answer = np.arange(36).reshape((6,6))
    result = problems.three()
    n.assert_equal(result.shape, answer.shape)


def test_four():
    answer = np.random.randint(10, size=(2,3))
    result = problems.four()
    n.assert_equal(result.shape, answer.shape)


def test_five():
    answer = np.identity(6)
    result = problems.five()
    n.assert_equal(result.all(), answer.all())


def test_six():
    answer = np.arange(0,100,1).reshape(10,10)
    result = problems.six()
    n.assert_equal(result.all(), answer.all())


def test_seven():
    M = np.arange(0,100,1).reshape(10,10)
    result = problems.seven(M)
    answer = M[:,:3]
    n.assert_equal(result.all(), answer.all())


def test_eight():
    M = np.arange(0,100,1).reshape(10,10)
    result = problems.six(M)
    answer = M[-2:]
    n.assert_equal(result.all(), answer.all())


def test_nine():
    answer = np.arange(0,10,1).reshape(1, 10)
    result = problems.nine()
    n.assert_equal(answer.all(), result.all())


def test_ten():
    V =  np.arange(0,10,1).reshape(1, 10)
    answer = V + [0.5]
    result = problems.ten(V)
    n.assert_equal(result.all() , answer.all())


def test_eleven():
    V =  np.arange(0,10,1).reshape(1, 10)
    answer = V * [-2]
    result = problems.eleven(V)
    n.assert_equal(result.all() , answer.all())


def test_twelve():
    V =  np.arange(0,10,1).reshape(1, 10)
    B = np.zeros(10)
    B.fill(0.5)
    B.reshape(10,1)
    answer = V + B
    result = problems.twelve(V)
    n.assert_equal(result.all() , answer.all())


def test_thirteen():
    answer_col = np.random.randint(10, size=(3, 1))
    answer_row = np.random.randint(10, size=(1, 3))
    answer_sq = np.random.randint(10, size=(3, 3))
    col, row, sq = problems.thirteen()
    n.assert_equal(col.shape, answer_col.shape)
    n.assert_equal(row.shape, answer_row.shape)
    n.assert_equal(sq.shape, answer_sq.shape)


def test_fourteen():
    answer_col = np.random.randint(10, size=(3, 1))
    answer_row = np.random.randint(10, size=(1, 3))
    answer_answer = answer_col * answer_row

    result = problems.fourteen(answer_col, answer_row)
    n.assert_equal(result, answer_answer)

def test_fifteen():
    c = np.random.randint(10, size=(3, 1))
    r = np.random.randint(10, size=(1, 3)) #row_vector = np.random.randint(10, size=(3,))
    s = np.random.randint(10, size=(3, 3))
    c_answer = s.dot(c)
    r_answer = r.dot(s)
    c_result, r_result = problems.fifteen(c, r, s)
    n.assert_equal(c_result, c_answer)
    n.assert_equal(r_result, r_answer)

def test_sixteen():
    c = np.random.randint(10, size=(3, 1))
    r = np.random.randint(10, size=(1, 3))
    answer = r.dot(c)
    result = problems.sixteen(c,r)
    n.assert_equal(result, answer)

def test_seventeen():
    a1 = False
    a2 = None
    a3 = True
    a4 = (4, 2)
    r1, r2, r3, r4 = problems.seventeen()
    n.assert_equal([r1, r2, r3, r4], [a1,a2,a3,a4])


def test_eighteen():
    a1 = np.random.randint(10, size=(3,6))
    a2 = np.reshape(a1 , (6,3))
    a3 = np.dot( a1, a2 )
    r1, r2, r3 = problems.eighteen()
    n.assert_equal([r1.shape, r2.shape, r3.shape], [a1.shape, a2.shape, a3.shape])


def test_nineteen():
    A = np.random.randint(10, size=(6,2))
    B = np.random.randint(10, size=(6,2))
    answer_square = np.square(A)
    answer_add  = A + B
    answer_subtract = A - B
    answer_multiply = A * B
    answer_divide =  A / B
    rsq, radd, rsub, rmult, rdiv = problems.nineteen()
    n.assert_equal([rsq.shape, radd.shape, rsub.shape, rmult.shape, rdiv.shape], [answer_square.shape, answer_add.shape, answer_subtract.shape, answer_multiply.shape, answer_divide.shape])


def test_twenty():
    A = np.arange(0,4).reshape(4,1)
    B = np.arange(0,3).reshape(1,3)
    answer = A + B
    result = problems.twenty()
    n.assert_equal(result.all(), answer.all() )

def test_twenty_one():
    answer = np.arange(0,100).reshape(10,10)
    result = problems.twenty_one
    n.assert_equal(result.shape, answer.shape)
