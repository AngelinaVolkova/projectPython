class Post:
    name = 'Anime'
    text = 'text'
    genre = 'genre'
    data = 'data'


deathnote = Post()
deathnote.name = 'Тетрадь смерти'
deathnote.text = 'Жить человеку или не жить опредиляют боги смерти,' \
                 'рано или поздно внося его имя в собственную тетрадь. Одна из' \
                 'таких тетрадей попадает в мир людей на территорию современной ' \
                 'Японии. А что случится, если тетрадь бога Death Note окажется'\
                 'в руках человека? Ответ очевиден: он возомнит себя богом.' \
                 'Это происходит с Ягами Лайтом'
deathnote.genre = 'мистика, детектив, триллер и психология'
deathnote.data = '2006'


titan = Post()
titan.name = 'Attaka on titan'
titan.text = 'Загнанное в угол человечество пытается выжить.Выжившие ютятся за стенами крупного ' \
             'поселения с собственным правительством, представляющим последний оплот ' \
             'централизованной власти в мире. Там живёт и юноша по имени Эрен.' \
             'Он проводит детство в полной безопасности, пока не происходит событие' \
             'из ряда вон: титаны прорываются в город, уничтожая всё на своём пути.' \
             'После вторжения гигантов Эрен становится сиротой и клянётся уничтожить' \
             ' всех до единого титанов.'
titan.genre = 'приключения, боевик, драма, фэнтези и триллер'
titan.data = '2013'


tokyogul = Post()
tokyogul.name = 'Токийский гуль'
tokyogul.text = 'Япония, альтернативная реальность. В это мире параллельно с ' \
                'людьми существует раса гулей - созданий стоящих выше людей ' \
                'в пишевой цепи, то есть людоедов. Однажды обычный школьник ' \
                'Канеки, становится жертвой женщины-гуля. Чудом пережив' \
                'нападение, Канеки, узнаёт, что взамен утраченных человеческих ' \
                'органов ему пересадили органы гуля. Кто же он теперь человек' \
                'или гуль. Ему предстоит пройти долгий путь самоопределения и найти' \
                'своё место в мире.'
tokyogul.genre = 'боевик, драма, фантастика и триллер'
tokyogul.data = '2014'
print(titan.name, titan.data, titan.genre, titan.text)

