whole = 7
fraction = 3.75
text_number = "25"
text_decimal = "2.5"
empty = ""
print( type(whole) , type(text_number) , type(text_decimal) , type(empty) ,sep="\n")
fraction_after = int(fraction)
whole_after = float(whole)
text_number_after = int(text_number)
text_decimal_after = float(text_decimal)
whole_after = str(whole)
print( "typ fraction po przemianie wartości to" , type(fraction_after) , "typ whole po przemianie wartości to" , type(whole_after) ,sep="\n")
print(bool(0) , bool(1) , bool(empty) , bool(text_number) ,sep="\n")
print(int(True) , float(False))
int(text_decimal)
int(fraction) == round(fraction)

