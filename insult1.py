import random compliments_start = ["Ты", "Вы", "Твоя улыбка", "Ваша улыбка", "Ты прекрасный", "Вы прекрасный"] compliments_mid = ["замечательный", "потрясающий", "великолепный", "восхитительный", "превосходный", "невероятный"] nouns = ["человек", "парень", "девушка", "мужчина", "женщина", "приятель", "друг", "подруга", "любимый", "любимая", "коллега", "сосед", "знакомый", "незнакомец", "герой"] compliments_end = ["!", ")))", "😍", "😊", "👍", "👏", "🙌", "💖"] start = random.choice(compliments_start) compliment = start + " " + random.choice(compliments_mid) + " " + random.choice(nouns) + random.choice(compliments_end) print(compliment)
