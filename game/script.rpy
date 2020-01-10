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
    stop music fadeout 1.0
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

    "Гэндальф пустил свою трубку по кругу."

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
    У Хранителей есть только две дороги, вперед к Белой горе через перевал и направо к горному озеру.
    """

menu:
    "На перевал":
        jump mountain_path

    "К горному озеру":
        jump озеро

label озеро:
    play music "audio/mountain lake.mp3"
    play sound "audio/atmosbasement.mp3_.flac"
    scene bg swamp-3
    with fade

    "Хранители пришли к древнему горному озеру. Гуляет ветер. Вдалеке слышно, как что-то журчит, булькает и капает. "
    "Обогнув озеро пуники добрались до тонкого перешейка между двумя чашами озера."

    gendalf """
    Дальше у нас есть два варианта.
    """

    stop voice
    stop music

menu:

    "Пойти направо, спуститься вдоль ручья":
        jump swamp_tree

    "Пойти налево, углубляясь в заболоченную долину":
        jump swamp_dead


label swamp_tree:
    play music "audio/swamp-sounds.mp3"
    scene bg swamp

    "Хранители шли вдоль заболоченного ручья."
    "В 300 метрах ниже росло развесистое гниющее дерево. Фродо было ужасно интересно
    и он заглянул в дупло дерева. В дупле лежал ключ."

    jump mountain_path

label swamp_dead:
    play music "audio/atmosbasement.mp3_.flac"
    scene bg swamp dead
    with fade

    "Группа решила пробираться по затопленной местности и пройти сквозь долину во что бы то ни стало.
    Чем они пробирались дальше, тем становилось глубже."

    scene bg swamp-2
    with fade
    play sound "audio/end-cut.mp3"
    with vpunch

    "В конце концов они столкнулись с Бамбром, Смотрителем Горных Озер и Болот. Все погибли. Плохая концовка."

    stop sound
    stop music

    return

label mountain_path:
    stop sound
    play music "audio/blizzard snow.mp3"

    scene white
    show bg snow
    with fade

    "Хранители забрались на перевал."

    scene bg mountains-path-2
    with fade
    play audio "audio/rock_breaking.flac"
    with hpunch

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

    scene black
    show bg door-3 at right
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

    return
