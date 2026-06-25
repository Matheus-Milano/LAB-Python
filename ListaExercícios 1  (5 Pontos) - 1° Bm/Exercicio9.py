"""Nathan Mazzaro Pereira"""
class Musica:
    """Criar objetos"""
    def __init__(self, titulo, artista, duracao_segundos):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao_segundos
    
    def __repr__(self):
        return f"\nTítulo: {self.titulo}\nArtista: {self.artista}\nDuração(s): {self.duracao}"
    
class Playlist:
    """Criar objetos"""
    def __init__(self, nome_playlist):
        self.nome_play = nome_playlist
        self.musicas = []
        self.tempo_total = 0
    """Adicionar músicas a playlist"""
    def adicionar_musica(self, musica):
        self.musicas.append(musica)
    """Exibir tempo total das músicas em minutos"""
    def exibir_tempo_total(self):
        for musica in self.musicas:
            self.tempo_total += musica.duracao
        self.tempo_total /= 60
        print(f"Tempo total: {self.tempo_total:.2f} minutos")

estudos_python = Playlist("musicas curtidas")
Playlist.adicionar_musica(estudos_python, Musica("Thunderstruck", "AC/DC", 210))
Playlist.adicionar_musica(estudos_python, Musica("Back in Black", "AC/DC", 256))
Playlist.adicionar_musica(estudos_python, Musica("Highway to Hell", "AC/DC", 208))
Playlist.adicionar_musica(estudos_python, Musica("T.N.T.", "AC/DC", 215))
Playlist.exibir_tempo_total(estudos_python)
