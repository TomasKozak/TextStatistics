Funkcia citaj() dostáva ako parameter meno textového súboru. Funkcia tento súbor prečíta a do globálnej premennej tab si nejako zaznačí počet výskytov každého slova v súbore (napr. pre každé slovo dvojicu: reťazec a počet výskytov). Premenná tab by mala byť typu zoznam (list). Slová v súbore sú oddelené aspoň jednou medzerou alebo znakom konca riadkov. Nepoužívajte ďalšie globálne premenné ani ďalšie funkcie.

Ďalšie funkcie, ktoré by ste mali naprogramovať, spracujú informácie v premennej tab a vrátia zoznam nejakých slov (možno aj prázdny):

funkcia najcastejsie() vráti zoznam slov (list), ktoré boli v texte najčastejšie - buď je to zoznam s jedným slovom, alebo je to zoznam viacerých slov, ak mali rovnaký počet výskytov (zrejme maximálny)

funkcia len_pocet(n) vráti zoznam slov (list), ktoré sa v texte vyskytli presne n-krát - tento zoznam môže byť aj prázdny, keď v súbore nebolo ani jedno slovo s týmto počtom výskytov

funkcia najdlhsie() vráti zoznam slov (list), ktoré boli v texte najdlhšie - buď je to zoznam s jedným slovom, alebo je to zoznam viacerých slov, ak majú rovnakú maximálnu dĺžku

funkcia najkratsie() vráti zoznam slov (list), ktoré boli v texte najkratšie - buď je to zoznam s jedným slovom, alebo je to zoznam viacerých slov, ak majú rovnakú minimálnu dĺžku

funkcia len_dlzka(n) vráti zoznam slov (list), ktoré majú dĺžku presne n - tento zoznam môže byť aj prázdny, keď v súbore nebolo ani jedno slovo s touto dĺžkou

Žiadna z týchto funkcií nič nevypisuje, len vráti (return) nejaký zoznam slov. Funkcia citaj() nič nevracia.
