# -*- coding: utf-8 -*-
# ХЭММИНГ КОДЫ — УНИВЕРСАЛДЫ БАҒДАРЛАМА
# Python 3. Әдепкі 2-нұсқа үшін екі сұрақта да Enter басыңыз.

info = input("Ақпараттық биттер [0111]: ").strip() or "0111"
error = int(input("Қате разряд нөмірі [5]: ") or "5")

if not info or any(bit not in "01" for bit in info):
    raise ValueError("Ақпарат тек 0 және 1 сандарынан тұруы керек!")

k = len(info)
r = 0

while 2**r < k + r + 1:
    r += 1

n = k + r
parity = [2**i for i in range(r)]

if not 0 <= error <= n:
    raise ValueError(f"Қате орны 0 мен {n} арасында болуы керек!")

print("\n===== 1-ЕСЕП: ХЭММИНГ КОДЫ =====")
print("Ақпарат:", info)
print("Ақпараттық биттер саны:", k)
print("Бақылау биттер саны:", r)
print("Жалпы биттер саны:", n)
print("Бақылау позициялары:", parity)

code = ["_"] * (n + 1)
j = 0

for i in range(1, n + 1):
    if i not in parity:
        code[i] = info[j]
        j += 1

print("Бастапқы макет:", "".join(code[1:]))

print("\nБақылау биттерін есептеу:")

for p in parity:
    positions = [
        i for i in range(1, n + 1)
        if i & p and i != p
    ]

    values = [int(code[i]) for i in positions]
    code[p] = str(sum(values) % 2)

    formula = " ⊕ ".join(f"a{i}" for i in positions)
    nums = " ⊕ ".join(map(str, values))

    print(f"a{p} = {formula}")
    print(f"   = {nums} = {code[p]}")

C = "".join(code[1:])
print("\nДұрыс код C =", C)

print("\n===== 2-ЕСЕП: ҚАТЕНІ ТАБУ =====")

received = code.copy()

if error != 0:
    received[error] = str(1 - int(received[error]))

C_star = "".join(received[1:])
print("Қабылданған C* =", C_star)

syndrome = 0
checks = []

print("\nТексеру теңдеулері:")

for j, p in enumerate(parity, 1):
    positions = [
        i for i in range(1, n + 1)
        if i & p
    ]

    values = [int(received[i]) for i in positions]
    e = sum(values) % 2
    checks.append(e)
    syndrome += e * p

    formula = " ⊕ ".join(f"a{i}" for i in positions)
    nums = " ⊕ ".join(map(str, values))

    print(f"E{j} = {formula}")
    print(f"   = {nums} = {e}")

binary = "".join(map(str, reversed(checks)))

print("\nСиндром S =", binary, "(екілік)")
print("Синдром S =", syndrome, "(ондық)")

corrected = received.copy()

if syndrome == 0:
    print("Қате анықталмады.")
elif syndrome <= n:
    print("Қате разряд:", syndrome)
    corrected[syndrome] = str(1 - int(corrected[syndrome]))
else:
    print("Синдром жарамды разрядты көрсетпейді.")

result = "".join(corrected[1:])
decoded = "".join(
    corrected[i]
    for i in range(1, n + 1)
    if i not in parity
)

print("\nТүзетілген код =", result)
print("Қалпына келген ақпарат =", decoded)
print("Бастапқы кодпен сәйкес:", result == C)
