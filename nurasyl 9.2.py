# -*- coding: utf-8 -*-
# ПРЕФИКСТІК КОД — УНИВЕРСАЛДЫ БАҒДАРЛАМА
# Python 3. Әдепкі 2-нұсқа үшін екі сұрақта да Enter басыңыз.

N = int(input("Алфавиттегі символ саны [47]: ") or "47")

message = (
    input("Екілік хабар [011011110]: ").strip()
    or "011011110"
)

# Қажет болса кодтарды өзгертуге болады
codes = {
    "A": "0",
    "B": "10",
    "C": "110",
    "D": "111"
}

if N < 1:
    raise ValueError("N оң сан болуы керек!")

if not message or any(x not in "01" for x in message):
    raise ValueError("Хабар тек 0 және 1 сандарынан тұруы керек!")

print("\n===== 1-ЕСЕП: БІРКЕЛКІ КОД =====")

k = 0

while 2**k < N:
    k += 1

print("Алфавит қуаты N =", N)
print("Шарт: 2^k >= N")
print(f"2^{k} = {2**k} >= {N}")

if k > 0:
    print(f"2^{k-1} = {2**(k-1)} < {N}")

print("Ең аз бит саны:", k)

print("\n===== 2-ЕСЕП: ФАНО ШАРТЫ =====")

for symbol, code in codes.items():
    print(f"{symbol} = {code}")

words = list(codes.values())

fano = (
    len(set(words)) == len(words)
    and all(
        not b.startswith(a)
        for a in words
        for b in words
        if a != b
    )
)

print("\nФано шарты:", "Орындалады" if fano else "Орындалмайды")

if not fano:
    raise ValueError("Код префикстік емес!")

print("\nБерілген хабар:", message)

decoded = []
parts = []
i = 0

while i < len(message):
    found = False

    for symbol, code in codes.items():
        if message.startswith(code, i):
            decoded.append(symbol)
            parts.append(code)
            i += len(code)
            found = True
            break

    if not found:
        raise ValueError(
            f"{i+1}-биттен бастап хабар декодталмайды!"
        )

print("\nКодтарға бөлу:")
print(" | ".join(parts))

print("\nДекодталған символдар:")
print(" ".join(decoded))

print("\nСоңғы жауап:", "".join(decoded))
