# mbot2
Makeblock mbot2 (aka mbot neo)

- [CyberPi Series User Manual - Руководство Пользователя по CyberPi](./cyberpi-go-kit-iot-uzivatelsky-navod.pdf)
- [Python API Documentation for CyberPi - Документация по доступным методам для платформы (робота) mbot2](./mBot2_API_cyberpi.pdf)

# Questions and Answers - Вопросы и Ответы

1. Вопрос: можно ли объявлять несколько одноименных функций, но анонсированных разным

Ответ: да, можно:
```python
@event.is_press('b')
def is_btn_press():
    cyberpi.console.println("кнопка B нажата")

@event.is_press('a')
def is_btn_press():
    cyberpi.console.clear()

```