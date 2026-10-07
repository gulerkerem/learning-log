"""
2 - NumPy Indexing, Slicing & Boolean Indexing
Konu: 1D/2D dizilerde eleman seçimi, fancy indexing ve koşullu filtreleme.

Notlar:
- matrix[satir, sütun]: Matrislerde tek virgül ile boyut seçimi yapilir.
- matrix[:, 0]: Belirli bir sütunun tamamini çeker.
- arr[arr > 20]: Koşulu sağlayan elemanlari filtreler (Boolean Indexing).
"""
"""""
import numpy as np

# --- 1. 2D Array (Matris) İndeksleme ve Dilimleme ---
matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Tüm Matris:\n", matrix)
print("0. Satir 2. Sütun (30):", matrix[0, 2])
print("İlk 2 Satir, Son 2 Sütun:\n", matrix[:2, 1:])


# --- 2. Fancy Indexing ---
numbers = np.array([100, 200, 300, 400, 500])
selected = numbers[[0, 3, 4]]
print("\nSeçilen İndeksler (0, 3, 4):", selected)


# --- 3. Boolean Indexing (Filtreleme) ---
scores = np.array([45, 85, 90, 30, 72, 60])

# 60 ve üzeri alan başarili öğrenciler
passing_scores = scores[scores >= 60]
print("\nGeçer Notlar (>= 60):", passing_scores)

# Birden fazla koşul (& = AND, | = OR)
# 50 ile 80 arasindaki notlar
mid_range = scores[(scores >= 50) & (scores <= 80)]
print("50-80 Arasindaki Notlar:", mid_range)

"""

import numpy as np
temperatures = np.array([18, 22, 15, 29, 31, 24, 16])

warm_days = temperatures[temperatures > 20]
ideal_days = temperatures[(temperatures > 15) & (temperatures < 25)]

print(f"Warm Days Temperatures:{warm_days}\nIdeal Days Temperatures:{ideal_days}")


# Lines: Students (Student 0, Student 1, Student 2)
# Column: Lessons (0: Math, 1: Physique, 2: Chemistry)
grades = np.array([
    [85, 90, 78],  # Student 0
    [60, 45, 50],  # Student 1
    [95, 88, 92]   # Student 2
])

student_2 = grades[2]
phy_grade = grades[:, 1]
sub_grades = grades[0:2, 0:2]
print("Student 2 Grades:", student_2)
print("Physics Grades:", phy_grade)
print("Sub Matrix (Math & Physics for Student 0 & 1):\n", sub_grades)