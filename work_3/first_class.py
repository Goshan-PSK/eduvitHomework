class MusicBand:
    genre: str = "Rock"
    originCountry: str = "USA"

    def __init__(self, name: str, memberCount: int, formedYear: int, albumList: list[str], isActive: bool) -> None:
        self.name: str = name
        self.memberCount: int = memberCount
        self.formedYear: int = formedYear
        self.albumList: list[str] = albumList
        self.isActive: bool = isActive

    def __str__(self) -> str:
        return f"Music Band: {self.name} ({self.formedYear}) - {self.genre}"

    def getYearsActive(self, currentYear: int) -> int:
        return currentYear - self.formedYear if self.isActive else 0

    def addAlbum(self, albumName: str) -> None:
        self.albumList.append(albumName)

    def disband(self) -> None:
        self.isActive = False

    def changeGenre(self, newGenre: str) -> None:
        MusicBand.genre = newGenre


band1 = MusicBand("The Rolling Codes", 4, 1990, ["Syntax & Harmony", "Loops of Love"], True)
band2 = MusicBand("Null Pointers", 3, 2005, ["Crash the Beat", "Segfault Symphony"], True)

print(band1)
print(band2.getYearsActive(2025))

band1.addAlbum("Variable Vibes")
band2.disband()
band1.changeGenre("Alternative Rock")

print(band1.albumList)
print(f"Band2 active: {band2.isActive}")
print(f"New genre for all bands: {MusicBand.genre}")