from django.http import HttpResponse


def about(request, city, up, love):
    return HttpResponse(f"""
<h2>Где родился, школа</h2>
<p>Я с города: {city}</p>
<p>Моя успеваемость в школе была: {up}</p>
<p>{love}</p>
""")


def contact(request, github, number, telegram):
    return HttpResponse(f"""
<h2>Мои контакты</h2>
<p>Мой аккаунт от github: {github}</p>
<p>Мой номер телефона: {number}</p>
<p>Мой телеграмм: {telegram}</p>
""")


def full_name(request, name, age, interests):
    return HttpResponse(f"""
<h2>О себе</h2>
<p>Фио: {name}</p>
<p>Мне {age} лет</p>
<p>Мои интересы: {interests}</p>                
""")
