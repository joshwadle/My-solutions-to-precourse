class Complex(object):

    def __init__(self, real, imaginary):
        self.type = 'a complex number'
        self.real = real
        self.imaginary = imaginary

    def print_complex(self):
        '''
        prints the complex in a standard format 'a + bi'
        with 'a' the real part and 'b' the imaginary one
        if b = 0: 'a'
        if a = 0: 'b'
        else: 'a + bi'
        a and b: rounded to 2 decimal
        '''
        if self.imaginary == 0:
            complex_number = "{:.2f}".format(self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                complex_number = "{:.2f}i".format(self.imaginary)
            else:
                complex_number = "-{:.2f}i".format(abs(self.imaginary))
        elif self.imaginary > 0:
            complex_number = \
                    "{:.2f} + {:.2f}i".format(self.real, self.imaginary)
        else:
            complex_number = \
                    "{:.2f} - {:.2f}i".format(self.real, abs(self.imaginary))
        return complex_number

    def conjugate(self):
        '''
        the complex conjugate of the number z = a + bi is defined to be a - bi.

        return
        ------
        (r,i) the real and imaginary part of the complex conjugate of complex_1
        '''
        return (self.real, -self.imaginary)

    def __add__(self, other_complex):
        '''
        add two complexes together

        return
        ------
        (r,i) the real and imaginary part of the complex obtained by adding the
        other complex

        '''
        (r_1, i_1) = self.real, self.imaginary
        (r_2, i_2) = other_complex.real, other_complex.imaginary
        return Complex(r_1 + r_2, i_1 + i_2)

    def __str__(self):
        '''
        prints the complex in a standard format 'a + bi'
        with 'a' the real part and 'b' the imaginary one
        if b = 0: 'a'
        if a = 0: 'b'
        else: 'a + bi'
        a and b: rounded to 2 decimal
        '''
        if self.imaginary == 0:
            complex_number = "{:.2f}".format(self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                complex_number = "{:.2f}i".format(self.imaginary)
            else:
                complex_number = "-{:.2f}i".format(abs(self.imaginary))
        elif self.imaginary > 0:
            complex_number = \
                    "{:.2f} + {:.2f}i".format(self.real, self.imaginary)
        else:
            complex_number = \
                    "{:.2f} - {:.2f}i".format(self.real, abs(self.imaginary))
        return complex_number
