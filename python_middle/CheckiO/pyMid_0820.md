# Week 1
## [01 - Say Hi](https://py.checkio.org/en/mission/say-history/)
```python
def say_hi(name: str, age: int) -> str:
#    return "Hi. My name is Alex and I'm 32 years old"

    say_hi_arr = "Hi. My name is "
    say_hi_arr += name
    say_hi_arr += " and I'm "
    say_hi_arr += str(age)
    say_hi_arr += " years old"
```

* 왼손님 코드
```python
return "Hi, My name is { }  and I'm { } years old".format(name, age)
```

## [02 - Correct Sentence](https://py.checkio.org/en/mission/correct-sentence/)

```python
def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]
    if(text[(len(text))-1] != "."):
        text += "."
    return text
```
* 왼손님 코드
```python
   if not text.endswith('.'):
   	    text += '.'
   return text
```

---

# 앞으로의 계획
* 다양한 파이썬 내장 함수에 대해 공부해야겠다.
* pythonic 하게 쓰도록 노력해야겠다.


    