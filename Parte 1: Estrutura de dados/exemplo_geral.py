from dataclasses import dataclass

@dataclass(frozen=True)
class Pet:
    nome: str
    dono: str

class Hotelzinho:
    def __init__(self, nome: str): #metodo init
        self.nome = nome
        self.hospedes: list[Pet] = []

    def __len__(self) -> int: #metodo len
        return len(self.hospedes)
    
    def __getitem__(self, cao): #metodo getitem
        return self.hospedes[cao]

    def __repr__(self) -> str: #metodo repr --> como a string vai ser representada
        return f'Hotelzinho {self.nome} com {len(self)} hóspedes'    

    def entrar(self, pet: Pet) -> None: #função para adicionar pet
        self.hospedes.append(pet)


#funções adicionais

def registrar_servico(pet: Pet, servico: str, historico: list[str]) -> None:
    if historico is None:
        historico = []
    historico.append(f"{pet.nome} serviço: {servico}")
    return historico

def listar_hospedes(hotel: Hotelzinho) -> None:
    for pet in hotel:
        print(f"{pet.nome} é hóspede do hotel {hotel.nome}, dono: {pet.dono}")

def main() -> None:
    loba = Pet(nome="Loba", dono="Rafaela")
    thor = Pet(nome="Thor", dono="Rafaela")

    hotel = Hotelzinho(nome="Hotel feliz")
    hotel.entrar(loba)
    hotel.entrar(thor)
    print(hotel)

    print("len(hotel):", len(hotel))
    print("hotel[0]:", hotel[0])
    print("hotel[1]:", hotel[1])
    print("slice:", hotel[:2])
    print("loba já esta no hotel?", loba in hotel)

    #dict 
    dias = {loba: 5, thor: 3}

    print("dias que loba esta hospedada:", dias[loba])
    print("dias que thor esta hospedado:", dias[thor])

    #str vs bytes
    anotacao = "Loba tomou banho"
    anotacao_bytes = anotacao.encode('utf-8')
    anotacao_volta = anotacao_bytes.decode('utf-8')
    print("ANotação Bytes:", anotacao_bytes)
    print("Anotação volta:", anotacao_volta)

    #mesma ref
    lista_a = ["banho"]
    lista_b = lista_a
    lista_b.append("tosa")
    print("Lista A:", lista_a)

if __name__ == "__main__":
    main()