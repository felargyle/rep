#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from .. import loader, utils

import logging
import random


logger = logging.getLogger(__name__)


@loader.tds
class InsultMod(loader.Module):
    """Shouts at people"""
    strings = {"name": "Insulter"}

    @loader.unrestricted
    async def insultcmd(self, message):
        """Use when angry"""
        # TODO localisation?
        adjectives_start = ["вонючий", "жирный", "чертов", "говняный", "тупой", "блядский", "омежный", "мелкий"
                           "блядский", "жидоебский", "многопиздный", "пиздецкий", "пиздоебищный", "шароебищийся", "хуйовый", "уебищенский", "уебский", 
                          "распиздяйский", "далбаеб", "свинья", "педофил", "омеган", "нижний", "мудак", "жополиз", "куколд",
                            "ХУЙ", "хуеголовый", "флейтист", "идиот", "пидарас", "лузер", "хуесос", "додик", "козлоебище",
                            "еблан", "гомик", "пидр", "пидар", "очкошник", "аутист", "даун", "сука", "гандон", "дерьмохеропиздократ" ]
        adjectives_mid = ["маленький", "выебистый", "тупой", "аутсайдер", "козлоебский", "ебаный", "пиздабольский",
                         "далбаеб", "свинья", "педофил", "омеган", "нижний", "мудак", "жополиз", "куколд",
                 "ХУЙ", "хуеголовый", "флейтист", "идиот", "пидарас", "лузер", "хуесос", "додик", "козлоебище",
                "еблан", "гомик", "пидр", "пидар", "очкошник", "аутист", "даун", "сука", "гандон", "дерьмохеропиздократ" ]
        nouns = ["далбаеб", "свинья", "педофил", "омеган", "нижний", "мудак", "жополиз", "куколд",
                 "ХУЙ", "хуеголовый", "флейтист", "идиот", "пидарас", "лузер", "хуесос", "додик", "козлоебище",
                "еблан", "гомик", "пидр", "пидар", "очкошник", "аутист", "даун", "сука", "гандон", "дерьмохеропиздократ",]
        starts = ["Ты", "Отъебись", "Когда ты сдохнешь,", "Слушай ты,", 
                  "Что с тобой не так", "Съеби", "Пососи", "Поешь говна", "Папей говна", "Мудак,", "Слушай сюда уебище", "Я тебя выебу ты", "Далбаеб ты", "Я твою мамашу ебал ты сукин сын и", "Я твою мамашу ебал ты", "Слушай сюда",  ]
        ends = ["!!!!", "!", "", ")))", ")", "=)"] 
        start = random.choice(starts)
        adjective_start = random.choice(adjectives_start)
        adjective_mid = random.choice(adjectives_mid)
        noun = random.choice(nouns)
        end = random.choice(ends)
        insult = start + " " + adjective_start + " " + adjective_mid + (" " if adjective_mid else "") + noun + end
        logger.debug(insult)
        await utils.answer(message, insult)
