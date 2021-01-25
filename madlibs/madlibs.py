# # String concatenation - (Como coocar strings juntas)
# # Vamos supor que você quira criar uma String que diga "Subscribe to ______"
youtuber = "Denis Claudiano"  # Alguma variável string

# # Alguns modos de se fazer isso!
# print("Subscribe to " + youtuber)
# print("Subscribe to {}".format(youtuber))
# print(f"Subscribe to {youtuber}")
adj = input("Adjetivo: ")
verb1 = input("Verbo: ")
verb2 = input("Verbo: ")
pessoa_famosa = input("Pessoa famosa: ")


madlib = f"Desenvolvimento de software é tão {adj}! Isso me deixa animado o tempo todo porque eu \
amo muito {verb1}. Me manten Focado e {verb2} como se eu fosse {pessoa_famosa}!"

print(madlib)
