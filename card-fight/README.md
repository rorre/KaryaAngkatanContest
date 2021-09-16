# Card Fight

> I have not translated the problem to English, apologies.

Dika dan Dina bermain suatu duel kartu, peraturannya berisi seperti berikut:

-   Dika selalu memiliki turn pertama.
-   Setiap pemain memiliki `m` kartu, `n` HP, 1 ATK, dan 1 DEF.
-   Pada setiap turn, pemain hanya dapat menggunakan satu kartu, lalu turn tersebut diberikan ke pemain lain.
-   Terdapat tiga jenis kartu:
    -   Attack, memberi serangan kepada musuh.
    -   Defense, menghalau serangan musuh.
    -   Support, menambah ATK dan DEF sebanyak 1. Kartu support dapat di-stack sebanyak mungkin.
-   Setelah kartu Attack/Defense digunakan, ATK dan DEF pemain akan reset menjadi 1.
-   Menggunakan kartu Attack/Support menghilangkan kondisi Defense.
-   Ketentuan damage yang diterima:
    -   Apabila pemain melakukan Defense, maka damage yang diterima yaitu `ATKMusuh - DEFPemain`.
    -   Selain itu, damage yang diterima yaitu `ATKMusuh`
-   Ketentuan pemenang:
    -   Jika salah satu pemain memiliki HP setara dengan 0 atau dibawahnya.
    -   Jika semua kartu telah digunakan, pemain dengan HP tertinggi memenangkan duel.
    -   Jika kedua HP yang dimiliki sama, print `Seri`.

Tentukan siapa yang memenangkan duel ini.

## Input Format

Baris pertama adalah jumlah kartu dan HP pemain, dibatasi dengan spasi. Baris kedua adalah kartu-kartu yang digunakan Dika. Baris ketiga adalah kartu-kartu yang digunakan Dina.

Format:

```
m n
AAASSSDDDD....xm
ASSDDSSAAS....xm
```

## Constraints

-   5 <= m <= 100
-   1 <= n <= 100

## Output Format

Nama pemenang dari duel tersebut, atau `Seri` jika seri.
