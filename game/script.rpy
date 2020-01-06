﻿define gendalf = Character('Гендальф', color="#009900")
define frodo = Character('Фродо', color="#990000")

transform mid_left:
    xalign 0.3
    yalign 0.85

transform mid_right:
    xalign 0.7
    yalign 0.85

transform left:
    xalign 0.05
    yalign 0.85

transform right:
    xalign 0.95
    yalign 0.85

label start:
    play music "audio/in-the-dark.mp3"
    scene bg road
    with fade

    "Хранители провели в пути весь день."

    scene bg entrance-2
    with fade

    "Только под вечер, в пасмурных сумерках, остановились усталые путники на отдых. Багрово-черная громада
    Баразинбара дышала вниз холодом - дул порывистый ветер."

    scene bg entrance
    with fade

    "Гэндальф пустил свою термокружку по кругу, и все Хранители сделали по глотку."

    scene bg fire
    with fade

    "После ужина они собрались на совет."

    show gendalf2 at right
    with dissolve

    gendalf "Сегодня ночью мы отдохнем"

    show frodo at mid_right
    with dissolve

    frodo "А куда мы пойдем потом?"

    gendalf """
    У Хранителей есть только две дороги, назад в Раздол или вперед к Белой горе.
    """

label swamp:
    play music "audio/mountain lake.mp3"
    scene bg swamp-3
    with fade

    "Хранители пришли к древнему горному озеру. Гуляет ветер. Вдалеке слышно, как что-то журчит, булькает и капает."

label swamp_tree:
    play music "audio/swamp-sounds.mp3"
    scene bg swamp

    "Хранители обошли озеро, на тонком перешейке двух чаш озера росло развесистое подгнивающее дерево.
    Фродо было ужасно интересно и он заглянул в дупло дерева. В дупле лежал ключ."

label swamp_dead:
    play sound "audio/end-cut.mp3"
    scene bg swamp-2

    "Группа решила пробираться по затопленной местности во что бы то ни стало.
    Чем они пробирались дальше, тем становилось глубже."

    "В конце концов они столкнулись с Бамбр Смотритель Болота. Все погибли. Плохая концовка."

label mountain_path:
    stop sound
    play music "audio/blizzard snow.mp3"

    scene bg snow
    with fade

    "Хранители забрались на перевал."

    scene bg mountains-path-2
    with fade
    play music "audio/rock_breaking.flac"

    "Прямо над вами разверглось небо."

    play music "audio/blizzard snow2.mp3"

    "Полил дождь, потом пошел снег, поднялся ураган."


label door:
    play music "audio/in-the-dark.mp3"
    scene bg mountains-path-3
    with fade

    "Хранителям удалось пробиться сквозь перевал. Вы спустились чуть ниже и вышли к очередному подьему."

    scene bg door-2
    with fade

    "В самом конце подьема вас ждала отвесная стена. Гэндальф внимательно посмотрел на стену."

    "В середине между сторожевыми дубами она была неестественно гладкой,
    и Гэндальф, приблизившись к ней вплотную, начал ощупывать ее руками, бормоча  какие-то непонятные слова."

    show gendalf2 at right
    with dissolve

    gendalf "Потом, отступив, спросил своих спутников: - А теперь? Теперь вы что-нибудь видите?"

    scene bg door-3
    with fade

    "Гендальф начал опять бормотать что-то себе под нос. Он сел у ворот в отчаянии и закурил трубку."

    "Стену осветила  взошедшая  луна, но Хранители  не  заметили  никаких изменений."

    "А потом на поверхности cтены появились тонкие серебристые  линии, стали постепенно ярче,
отчетливей, и  вскоре глазам изумленных путников открылся искусно выполненный рисунок."

    show frodo at left

    frodo "- Замочная скважина! - воскликнул Фродо, показав на еле заметное углубление в стени."

    """Гэндальф подошел к стене, вставил ключ в скажину и с трудом повернул его.
    Дверь со скрипом поддалась и отворилась."""

label final:

    play music "audio/happy-end.mp3" fadeout 1.0 fadein 1.0
    scene bg moria
    with fade

    "Счастливый конец первой части! До новых встречь!"
