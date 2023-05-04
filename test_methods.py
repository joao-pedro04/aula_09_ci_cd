import methods
 
def test_area():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the area
    output = methods.area_of_rectangle(width, height)

    # then the area should be 10
    assert output == 10
 
def test_perimeter():
    # given a width of 2 and a height of 5
    width = 2
    height = 5

    # when we calculate the perimeter
    output = methods.perimeter_of_rectangle(width, height)
    
    # then the perimeter should be 14
    assert output == 14

def test_calculator_sum():
    # given 2 numbers, n1 valuing 2 and n2 valuing 3
    n1 = 2
    n2 = 3

    # when we sum both of then
    output = methods.sum_of_numbers(n1,n2)

    # then the sum should be 5
    assert output == 5

def test_calculator_sub():
    # given 2 numbers, n1 valuing 15 and n2 valuing 22
    n1 = 15
    n2 = 22

    # when we subtract one by another 
    output = methods.sub_of_numbers(n1,n2)

    # then the sub should be 7 
    assert output == 7

def test_calculator_mul():
    # given 2 numbers, n1 valuing 322 and n2 valuing 225
    n1 = 322
    n2 = 225

    # when we multiply both of then 
    output = methods.mul_of_numbers(n1,n2)

    # then the multiplication should be 72.450
    assert output == 72450

def test_calculator_div():
    # given 2 numbers, n1 valuing 4 and n2 valuing 8
    n1 = 4
    n2 = 8

    # when we divide both of then
    output = methods.div_of_numbers(n1,n2)

    # then the division should be 2
    assert output == 2