import numpy as np
# Ocak - Haziran ayları satışları (6 ay)
sales_h1 = np.array([120, 135, 140, 155, 160, 175])

# Temmuz - Aralık ayları satışları (6 ay)
sales_h2 = np.array([180, 190, 185, 200, 210, 225])

full_year = np.hstack((sales_h1, sales_h2))
matrix_2x6 = full_year.reshape(2,6)
matrix_3xX = full_year.reshape(3,-1)

print("Full year sales:", full_year)
print("Matris of 2x6:", matrix_2x6)
print("Matris of 3:", matrix_3xX)
