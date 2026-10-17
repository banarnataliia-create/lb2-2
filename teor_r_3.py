import math

losses = [300, 100, 200, 400]
probs = [0.2, 0.3, 0.1, 0.4]

m_x = sum(x * p for x, p in zip(losses, probs))

max_p_idx = probs.index(max(probs))
mo_x = losses[max_p_idx]


g_x = math.prod(x**p for x, p in zip(losses, probs))

variance = sum(p * ((x - m_x) ** 2) for x, p in zip(losses, probs))
sigma_x = math.sqrt(variance)


sv_x = sum(
    p * ((x - m_x) ** 2) for x, p in zip(losses, probs) if x > m_x
)
ssv_x = math.sqrt(sv_x)


cv_x = (sigma_x / m_x) * 100  
csv_x = (ssv_x / m_x) * 100  

print("=" * 55)
print("РЕЗУЛЬТАТИ РОЗРАХУНКУ ПОКАЗНИКІВ РИЗИКУ (ВАРІАНТ 3)")
print("=" * 55)
print(f"1. Сподівана величина збитків M(X):    {m_x:.2f} грош. од.")
print(f"2. Модальне значення Mo(X):           {mo_x:.2f} грош. од.")
print(f"3. Зважене середньогеометричне G(X): {g_x:.2f} грош. од.")
print(f"4. Дисперсія D(X):                   {variance:.2f}")
print(f"5. Середньоквадратичне відхилення σ:  {sigma_x:.2f} грош. од.")
print(f"6. Семіквадратичне відхилення SSV:    {ssv_x:.2f} грош. од.")
print(f"7. Коефіцієнт варіації CV:            {cv_x:.2f}%")
print(f"8. Коефіцієнт семіваріації CSV:       {csv_x:.2f}%")
print("=" * 55)